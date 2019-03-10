import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from conf import config
def send_report():
    msg = MIMEMultipart()
    body = MIMEText(config.body,'plain','utf-8')
    msg.attach(body)

    msg['From'] =config.smtp_user
    msg['To']=','.join(config.receive)
    msg['Subject']=config.subject

    with open(config.report_file,"rb") as f:
        att_file = f.read()

    att=MIMEText(att_file,'base64','utf-8')
    att["Content-Type"]="application/octet-stream"
    att["Content-Disposition"]="attachment;filename='report.html'"
    msg.attach(att)

    smtp = smtplib.SMTP_SSL(config.smtp_server)
    smtp.login(config.smtp_user,config.smtp_password)
    smtp.sendmail(config.smtp_user,config.receive,msg.as_string())

if __name__ == '__main__':
    send_report()
