import requests
from bs4 import BeautifulSoup
import bitly_api
from user_agents import parse
import os.path
import os
from twilio.rest import Client
from win10toast import ToastNotifier
import sys
import time
import psycopg2

# status 
global status

# postgreSQL Database
def status(val):
    stat = 'Treye Status : ' + val
    print(stat)
    return stat

# Whatsapp

client = Client()
from_whatsapp_number='whatsapp:+14155238886'
to_whatsapp_number="whatsapp:" + os.environ['MY_PHONE_NUMBER']

conn = psycopg2.connect(user = "postgres",
                            password = os.environ['PG_PASSWORD'],
                            host = "127.0.0.1",
                            port = "5432",
                            database = "Treye_data")
cursor = conn.cursor()
global i
cursor.execute("select exists(select * from information_schema.tables where table_name=%s)", ('data',))
dbexist = cursor.fetchone()[0]
if dbexist == True:
    status('Data Already Exists')
    #cursor.execute("SELECT Index_No FROM data ORDER BY Index_No DESC LIMIT 1")
    cursor.execute("SELECT count(*) from data")
    dat = cursor.fetchall()
    i=dat[0][0]
    print(i,'entries found.')
elif dbexist == False:
    status("Data Not Found")
    status('Preparing for new Data')
    client = Client()
    from_whatsapp_number='whatsapp:+14155238886'
    to_whatsapp_number="whatsapp:" + os.environ['MY_PHONE_NUMBER']
    print(to_whatsapp_number)
    client.messages.create(body='_*TREYE*_\nThankyou for choosing Treye as your Amazon price tracker.\n\nLets Hope for the best.🤩\n\n💁🏻‍♂For any help contact us on www.github.com/BRAINIFII/Treye',from_=from_whatsapp_number,to = to_whatsapp_number)
    cursor.execute('''CREATE TABLE data
        (Index_No INT     NOT NULL,
        Title           VARCHAR(1000)    NOT NULL,
        Link          VARCHAR(100) NOT NULL,
        PRICE INT     NOT NULL); ''')
    cursor.execute("commit")
    status("Done with preparation")

toaster = ToastNotifier()

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

global prog_location,lenrange

lenrange = 40      #title notification range

tmout = 5          # Value in hours
prog_call = sys.argv[0]
prog_location = os.path.split(prog_call)[0]
notifytimeout = tmout * 60 * 60

def crawler(URL,API_USER,API_KEY):
    """Grab product data
    
    Arguments:
        URL {string} -- Enter your URL
        API_USER {string} -- API user-key
        API_KEY {string} -- API secret-key
    """
    global bitly,price,price_notif,product_title,product_price,i,shurl
    print("Given URL : ",URL)
    bitly = bitly_api.Connection(API_USER, API_KEY)
    response = bitly.shorten(URL)
    shurl = response["url"]
    print("Short URL ",shurl)
    page = requests.get(shurl, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice")
    #print(price)
    try :
        price = soup.find(id="priceblock_ourprice").get_text()

        if type(price) is str:
            price = price[1:]
            product_price = float(price.replace(",", ""))
            price_notif = str(product_price)
            prd_title = title.strip()
            product_title = prd_title.replace("'","")
            print("\n Character length of title ",len(product_title),"\n")
            if len(product_title) > lenrange:
                product_title = product_title[:lenrange] + "......"
            print(product_title," ----> Price = ",product_price,"\n\n")
            print('i in block 1 before increment: ',i)
            i=i+1
            print('i in block 1 after increment: ',i)
            cursor.execute("INSERT INTO data VALUES(" + str(i) + ",'" + product_title +"','" + shurl + "'," + str(product_price) + ")")
            cursor.execute("commit")
            print("INSERT INTO data VALUES(" + str(i) + ",'"+ product_title +"','" + shurl + "'," + str(product_price) +")\n\n")

        else:
            print("Product Not Found")

    except AttributeError:
        try :
            price = soup.find(id="priceblock_dealprice").get_text()
            if type(price) is str:
                price = price[1:]
                product_price = float(price.replace(",", ""))
                price_notif = str(product_price)
                prd_title = title.strip()
                product_title = prd_title.replace("'","")
                print("\n Character length of title ",len(product_title),"\n")
                if len(product_title) > lenrange:
                    product_title = product_title[:lenrange] + "......"
                print(product_title," ----> Price = ",product_price,"\n\n")
                print('i in block 2 before increment: ',i)
                i=i+1
                print('i in block 2 after increment: ',i)
                cursor.execute("INSERT INTO data VALUES(" + str(i) + ",'" + product_title +"','" + shurl + "'," + str(product_price) + ")")
                cursor.execute("commit")
                print("INSERT INTO data VALUES(" + str(i) + ",'"+ product_title +"','" + shurl + "'," + str(product_price) +")\n\n")
            else:
                print("Product Not Found")
        except AttributeError:
            try:
                price = soup.find(id="priceblock_saleprice").get_text()
                if type(price) is str:
                    price = price[1:]
                    product_price = float(price.replace(",", ""))
                    price_notif = str(product_price)
                    prd_title = title.strip()
                    product_title = prd_title.replace("'","")
                    print("\n Character length of title ",len(product_title),"\n")
                    if len(product_title) > lenrange:
                        product_title = product_title[:lenrange] + "......"
                    print(product_title," ----> Price = ",product_price,"\n\n")
                    print('i in block 3 before increment: ',i)
                    i=i+1
                    print('i in block 3 after increment: ',i)
                    cursor.execute("INSERT INTO data VALUES(" + str(i) + ",'" + product_title +"','" + shurl + "'," + str(product_price) + ")")
                    cursor.execute("commit")
                    print("INSERT INTO data VALUES(" + str(i) + ",'"+ product_title +"','" + shurl + "'," + str(product_price) +")\n\n")
                else:
                    print("Product Not Found")
            except AttributeError:
                print("Product unavailable cannot store in database")


def notify():
    toast_logo = os.path.join(prog_location,"../Python Project/icon/icon.ico")
    toaster.show_toast("Treye","Price for your searched product (" + product_title + ") is Rs. "+price_notif,icon_path=toast_logo,duration=9,threaded=True)
    text = "Treye:\nPrice for your searched product (" + product_title + ") is Rs. *"+price_notif+"* \nLink: " + shurl
    client.messages.create(body=text,from_=from_whatsapp_number,to = to_whatsapp_number)
    time.sleep(1)

def find_data():
    if dbexist == True:
        return True
    else:
        return False

def title():
    return product_title

def cleardata():
    cursor.execute("drop table data")

def productprice():
    return product_price

def testmessage():
    """Sends a Test Message on whatsapp.
    """
    text2 = "Treye:\nThis is a test message from Treye\n\nBe Happy☺\n.\n.\nBe Awesome😋"
    client.messages.create(body=text2,from_=from_whatsapp_number,to = to_whatsapp_number)

def error():
    pass

