#MODULOS PARA O FUNCIONAMENTO DO PROGRAMA.
import pyautogui
import datetime
import time
import sys
import glob
import os

##############################################

# MODULOS PARA O ENVIO DO EMAIL AUTOMATICO.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# VARIAVEL GLOBAL
screenshotName = "screenshot"
#LOCAL ONDE SERA ARMAZENADO TODAS AS IMG(SCREENSHOT)
path = "C:/Users/fernando/PycharmProjects/Captura/prints/"

x_start_point = 0
y_start_point = 0
#AREA ESTABELECIDA PARA O TAMANHO DA IMG.
x_area = 1653
y_area = 780

#CONTAGEM ME SEGUNDOS
contador = 10

#INICIANDO O LOOP DO SCRIPT.
while True:
    now = datetime.datetime.now()
    now_two_params = str(now).split(" ")
    date = str(now_two_params[0])
    raw_time = str(now_two_params[1]).split(".")
    time_raw = str(raw_time[0])
    time_clean = time_raw.replace(':', '')

    try:
        print("Tirando uma Captura de Tela...")
        screenshot = pyautogui.screenshot(path + screenshotName + date + "_" + time_clean +".png", region=(x_start_point, y_start_point, x_area, y_area))
    except Exception as e:
        print(e)

    print("Captura de Tela OK! ")
    files_path = os.path.join(path, '*')
    files = sorted(glob.iglob(files_path), key=os.path.getatime, reverse=True)

    last_screenshot = files[0]
    print("Ultima Captura de Tela: \n" + str(last_screenshot))

# #######################################################################33

    #E-MAIL DO REMETENTE.
    email_user = 'wellingthon957@gmail.com'
    email_password = '963852741f'

    #E-MAIL DO DESTINATÁRIOS
    list_destinatal = 'glaucimeiresilva34830@gmail.com, wellingthon741@gmail.com'

    #DEFINIÇÃO DO TITLO DO ASSUNTO.
    titlo = 'Relatorio de produção hora a hora'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = list_destinatal
    msg['Subject'] = titlo

    #DEFINIÇÃO DO CORPO DO E-MAIL
    body = "Esta e uma mensagem automatica, encaminha aos senhores"

    msg.attach(MIMEText(body, 'plain'))

    filename = last_screenshot
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)

    msg.attach(part)
    text = msg.as_string()
    #server = smtplib.SMTP('smtp.outlook.com', 587)
    #server = smtplib.SMTP('smtp.hotmail.com', 587)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user, email_password)

# CONFIRMAÇÃO DE ENVIO DOS E-MAILS PARA OS DESTINATÁRIOS.
    try:
        print("\nEnviando E-mail para: " + str(list_destinatal))
        server.sendmail(email_user, list_destinatal.split(','), text)
    except Exception as e:
        print(e)
    print("E-mail enviado com sucesso!")

    print("\nAguando: " + str(contador) + " segundo para a Prox Captura de Imagens\n")
    server.quit()
    time.sleep(int(contador))
    #FINAL DO LOOP


