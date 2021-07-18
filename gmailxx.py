import csv
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import traceback

#Umfrage ändern 
#Ort ändern


df = pd.read_csv(r'C:\Users\larsv\OneDrive\Dokumente\Python Scripts\Muenchen\xx.txt') #Variabel
i = 0
for x in df['name']:
    try:
        mail_content = 'Guten Tag '+ df['name'][i] + ',<br> <br> im Rahmen einer Studie ' \
                        'der Technischen Universität München beschäftigen wir uns mit dem Thema "Startup Kooperationen im Handwerk".' \
                        ' Derzeit gibt es wenig Forschung über die Zusammenarbeit von Handwerksbetrieben und Startups, weshalb wir ein Meinungs- und ' \
                        'Erfahrungsbild mit Hilfe einer Umfrage einholen wollen. Sie müssen für die Beantwortung der Umfrage aber noch keinen Kontakt zu Startups gehabt haben.<br> <br> ' \
                        'Derzeit werten wir Rückmeldung von Handwerksbetrieben aus ganz Deutschland aus und für eine finale Betrachtung fehlen uns noch' \
                        '' \
                        ' ausreichend Rückmeldungen aus dem Einzugsgebiet München/Oberbayern. Deshalb würde die Rückmeldung von Ihnen ' + df['name'][i] + ' ' \
                        'uns entscheidend weiterhelfen. <br> <br> <a href="https://tumchristinanedyalkoff.limesurvey.net/18?lang=de"> ' \
                        'Hier klicken, um zur Umfrage zu gelangen</a><br> <br> Die Umfrage dauert ca. 5 Minuten und ist anonym. Die Antworten können ihrem Betrieb nicht zugeordnet werden. <br> ' \
                        'Diese Studie wird vom Controlling Lehrstuhl der TU München betreut und bei Fragen zur Umfrage können sie gerne eine E-Mail an: lars.von-fromberg@tum.de schreiben. ' \
                        '<br><br> Vielen Dank für Ihre Teilnahme!<br>  <br>' \
                        '<table width="365" cellspacing="0" cellpadding="0" border="0"> <tr> <td style="vertical-align: middle; text-align:left;color:#000000;font-size:12px;font-family:helvetica, arial;; text-align:left"> <span><span style="margin-right:5px;color:#000000;font-size:15px;font-family:helvetica, arial">Lars von Fromberg</span> <span style="margin-right:5px;color:#000000;font-size:12px;font-family:helvetica, arial">Student Management &#x26; Technology M.Sc.</span><br><span style="margin-right:5px;color:#000000;font-size:12px;font-family:helvetica, arial">TUM School of Management</span></span> <br><br> <table cellspacing="0" cellpadding="0" border="0" style="margin:0 5px 5px 0;display:inline;"><tr><td style="padding-right:5px"><img width="40" height="40" src="https://s1g.s3.amazonaws.com/22729bc9dcaa8b2cd54e556ae46c6b79.png" alt="email" style="border:none;"></td><td><span style="font:12px helvetica, arial;">Email:&nbsp;<a href="mailto:lars.von-fromberg@tum.de" style="color:#3388cc;text-decoration:none;">lars.von-fromberg@tum.de</a></span></td></tr></table> <br> <br> <table cellpadding="0" cellpadding="0" border="0"><tr></tr></table> </td> </tr> </table> '''



        #The mail addresses and password
        sender_address = 'lars.von-fromberg@tum.de'
        sender_pass = ''# Hier TUM-Login daten bzw. Gmail application code
        receiver_address = df['mail'][i]

        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Umfrage Startup Kooperation ' + df['name'][i] + ''   #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'html'))

        #Create SMTP session for sending the mail
        session = smtplib.SMTP('postout.lrz.de', 587)
        #postout.lrz.de (TUM-SMTP)
        #smtp.gmail.com (GMAIL-SMTP)

        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print(df['mail'][i] + " " + df['name'][i] )
        i = i + 1
    except Exception as e:
        print(e) # Manchmal gibt es beim Senden ein Fehler. Schickt das System kurz in Ruhe, damit es nicht abstürzt.
        time.sleep(120)
        i = i + 1
