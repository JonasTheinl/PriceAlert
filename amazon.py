import requests
from bs4 import BeautifulSoup
import smtplib, ssl


def sendMail(converted_price):
    mail_text = 'Der Raspberry PI 4 ist momentan sehr guenstig. Er kostet: ' + converted_price
    subject = 'Price Alert Raspberry PI 4'

    Mail_From = 'testsender'
    Rcpt_To = 'testreceiver'
    DATA = 'From:%s\nTo:%s\nSubject:%s\n\n%s' % (Mail_From, Rcpt_To, subject, mail_text)
    server = smtplib.SMTP(' http://smtp.gmail.com:587')
    server.starttls()
    server.login(user, pwd)
    server.sendmail(Mail_From, Rcpt_To, DATA)
    server.quit()

user = 'testuser'
pwd = 'testpassword'


URL = 'https://www.amazon.de/Raspberry-Pi-ARM-Cortex-A72-Bluetooth-Micro-HDMI/dp/B07TC2BK1X/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1XIT0PXM3N3AA&dchild=1&keywords=raspberry+pi+4&qid=1604397946&quartzVehicle=812-409&replacementKeywords=raspberry+pi&sprefix=rasp%2Caps%2C252&sr=8-3'

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

price = soup.find(id='priceblock_ourprice').get_text()
converted_price = price[0:5]
converted_price_float = float(converted_price.replace(',', '.'))

if converted_price_float < 55:
    sendMail(converted_price)