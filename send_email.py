import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
class SendEmail:
    def __init__(self, sentTo, emailAddr, emailPass, subject, content):
        emailAddr = emailAddr   #sender email address
        emailPass = emailPass         # password for sender email

        smtpAddr = "smtp.gmail.com"      # smtp server. gmail의 경우, smtp.gmail.com를 입력합니다.
        smtpPort = 465
        emailMsg = MIMEMultipart()

        # isinstance는 Variable Type을 파악하기 위해 사용
        if isinstance(sentTo, list):
            emailMsg["To"] = ", ".join(sentTo)
            # STR.join(list): List에 있는 String 사이에 STR을 추가하여서 한 String으로 변경함
            # """ STRING """ (3개)를 사용하면 새로운 줄도 STRING에 포함
            # " STRING %s " % STR_VARIABLE을 사용하면 %s에 STR_VARIABLE이 들어감
        elif isinstance(sentTo, str):
            emailMsg["To"] = sentTo
        else:
            print("First parameter is unknown type")
            return
        emailMsg["From"] = emailAddr
        emailMsg["Subject"] = subject
        content = content + "\n\n by Myeonghak"
        tmp = MIMEText(content, "plain")
        emailMsg.attach(tmp)
        try:
            emailServer = smtplib.SMTP_SSL(smtpAddr, smtpPort)
            emailServer.ehlo()
            emailServer.login(emailAddr, emailPass)
            emailServer.sendmail(emailAddr, sentTo, emailMsg.as_string())
            emailServer.close()
            print("Success: Email is sent")
        except:
            print("Error: Could not send email")
