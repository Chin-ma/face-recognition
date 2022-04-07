import smtplib
gmail_user = 'chinmay2003cp@gmail.com'
part = 'xfvklwrbdubwtomo'

sent_from = gmail_user
to = ['chinu2003cp@gmail.com']
subject = 'Test mail from python'
body = 'This is a test mail which is generated using python to check its functionality'

email_text = """\
From: %s
To: %s
Subject: %s

%s
"""%(sent_from, ",".join(to),subject,body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, part)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print("Email sent successfully")
except Exception as ex:
    print("Something went wrong", ex)