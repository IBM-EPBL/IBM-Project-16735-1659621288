import smtplib
import os
s = smtplib.SMTP('smtp.gmail.com', 587)
def sendmail(TEXT,email,SUBJECT):
    #print("sorry we cant process your candidature")
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.login("getjob492@gmail.com", "mdvuyhdtynoxugck")
        message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        s.sendmail("getjob492@gmail.com", email, message)
    except Exception as e:
        print("Mail sending failed!",+e)
    finally:
        s.quit()