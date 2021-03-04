# 주식 종목 뉴스 요약 메일링

---


<center><img src="/asset/title.png" align="center" alt="drawing" width="400"/></center>    

<br/>


뉴스를 요약한 정보를 테이블 형태로 전달하는 파이썬 프로그램입니다. 이 프로그램은 [네이버 금융](https://finance.naver.com/item/main.nhn?code=005930)의 뉴스를 주기적으로 크롤링하여 [Pororo](https://github.com/kakaobrain/pororo)라는 멋진 라이브러리가 제공하는 [KoBART](https://github.com/SKT-AI/KoBART) summary 기능을 사용해, 뉴스 기사를 한눈에 파악하기 쉬운 짧은 문장으로 축약하여 사용자의 메일로 보내줍니다.

<br/>

<center><img src="/asset/example.png" align="center" alt="drawing" width="400"/></center>    

<br/>




Gmail에 연동하는 방식과 코드에 대한 설명은 [제 블로그](https://myeonghak.github.io/natural%20language%20processing/NLP-%EC%A3%BC%EC%8B%9D-%EB%89%B4%EC%8A%A4-%EC%9A%94%EC%95%BD-%EB%A9%94%EC%9D%BC%EB%A7%81-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8/)에서 찾아보실 수 있습니다.

레포 내부의 [주피터 노트북](/news_summary.ipynb)을 통해 실행할 수 있으며, 코랩 환경에서 사용하실 것을 권장드립니다.  


---
## references
https://www.youtube.com/watch?v=PtgnzgaURIM&list=LL&index=22
https://hengju.tistory.com/36
