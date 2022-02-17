import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

smtpname = ""
smtpport = ""
sendemail = ""
password = ""
recvemails = [""]


for recvemail in recvemails :
        
    title = ""
    content = ""

    #MIME객체화
    msg = MIMEMultipart("alternative")
    part2 = MIMEText(content)
    msg.attach(part2)
    msg["From"] = sendemail
    msg["To"] = recvemail
    msg["subject"] =title
    #파일첨부
    part = MIMEBase("application","octet-stream")
    #파일 읽어오기
    with open("","rb") as f:
        #part에 담기
        part.set_payload(f.read())
    #파일 첨부할 수 있는 형태로 인코딩
    encoders.encode_base64(part)
    # header 정보 정의
    part.add_header("content-Disposition","attachment",filename = ".csv")

    msg.attach(part)

    #메일 서버 접속 
    s = smtplib.SMTP(smtpname,smtpport)
    #메일 서버 접근
    s.starttls()
    #메일 서버 로그인
    s.login(sendemail,password)
    #메일 발송
    s.sendmail(sendemail,recvemail,msg.as_string())
    s.close()
