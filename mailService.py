import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time

def sendMail(receive):
    
    fromaddr = "chinmay2003cp@gmail.com"
    toaddr = receive
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Fine generated for not wearing mask"
    body = "This mail is being sent to you because of the discription of the rule of not wearing mask in public places"
    msg.attach(MIMEText(body, 'plain'))
    filename = "invoice.pdf"
    attachment = open("invoice.pdf", "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(fromaddr, "xfvklwrbdubwtomo")
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()
    except smtplib.SMTPException:
        print("Error in sending email")
    print("Email sent")

if __name__ == "__main__":
    sendMail("receive")




# xfvklwrbdubwtomo