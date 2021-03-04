from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import os


# os.chdir('자신의 디렉토리 주소')
# os.chdir('/content/drive/MyDrive/Colab Notebooks/news_feeder')



class news_crawler:
    
    def __init__(self, table_path):
        self.company_code_table = pd.read_csv(table_path, dtype=str, sep='\t')
    
    
    def crawler(self, company_code, num_article):
        
        done_page_num=0

        # page = 1 
        num_per_page=20 # naver serves 20 articles per page
        num_page,remainder=divmod(num_article,20)
        num_page+=1

        article_result=[]
        
        for page in range(done_page_num+1, done_page_num+num_page+1):
            try:
                url = 'https://finance.naver.com/item/news_news.nhn?code=' + str(company_code) + '&page=' + str(page) 
                source_code = requests.get(url).text
                html = BeautifulSoup(source_code, "lxml")
        
                
                # 뉴스 링크
                links = html.select('.title') 

                link_result =[]
                if page == num_page:
                    links=links[:remainder]

                for link in links: 
                    add = 'https://finance.naver.com' + link.find('a')['href']
                
                    link_result.append(add)
                print(f"{len(link_result)}개의 뉴스 크롤링..")
            except Exception:
                pass 

            
            # 뉴스 날짜 
            # dates = html.select('.date') 
            # date_result = [date.get_text() for date in dates] 
            
            # cnt=0
            for article_url in link_result: 
                try:
                    # cnt+=1
                    # if cnt%100==0:
                    #     print(f"{cnt}번째 기사 처리중")
                #    article_url = link_result[0] 
                    article_source_code = requests.get(article_url).text
                    article_html = BeautifulSoup(article_source_code, "lxml")
                    article_time = article_html.select('.tah')[0].get_text()

                    # 뉴스 내용
                    article_contents = article_html.select('.scr01')
                    article_contents=article_contents[0].get_text()
                    article_contents = re.sub('\n','',article_contents)
                    article_contents = re.sub('\t','',article_contents)
                    
                    # cut extra text after Copyright mark
                    if "ⓒ" in article_contents:
                        article_contents=article_contents[:article_contents.index("ⓒ")]
                    
                    # cut too long text to prevent CUDA OOM issue
                    if len(article_contents)>=1500:
                        article_contents=article_contents[:1500]

                    article_result.append([article_contents,article_time])

                    time.sleep(random.uniform(0.1,0.7))
                except Exception:
                    pass

            # print("다운 받고 있습니다------")

        return article_result




    def convert_company_to_code(self,company):

        # 종목코드 추출 
        company_name = self.company_code_table['회사명']
        keys = [i for i in company_name]    #데이터프레임에서 리스트로 바꾸기 
     
        company_code = self.company_code_table['종목코드']
        values = [j for j in company_code]
     
        dict_result = dict(zip(keys, values))  # 딕셔너리 형태로 회사이름과 종목코드 묶기 
        
        pattern = '[a-zA-Z가-힣]+' 
        
        if bool(re.match(pattern, company)) == True:
            company_code = dict_result.get(str(company))
            return company_code
        
        else:
            company_code = str(company)
            return company_code
    
    def crawl_news(self, company, max_num=5):
        print(f"{company} 종목 뉴스를 가져옵니다.")
        company_code=self.convert_company_to_code(company)

        if company_code:
                result=self.crawler(company_code, max_num)
                for i in range(len(result)):
                    result[i].append(company)
                return result

        else:
            print(f"{company} 종목이 존재하지 않습니다.")   
            return []