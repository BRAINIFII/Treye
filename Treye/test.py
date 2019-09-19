import time
import Tmodules.treye as treye
import os
import bitly_api

API_USER = os.environ['BITLY_API_USER']
API_KEY = os.environ['BITLY_KEY']
bitly = bitly_api.Connection(API_USER, API_KEY)
url = 'https://www.amazon.in/DJI-Ronin-S-Superior-Handheld-stabilizer/dp/B07H1DTR7F?pf_rd_p=d956de62-3849-4fa4-a5f3-eea045432d33&pd_rd_wg=rYUHT&pf_rd_r=TS0KC55G8KCDEGWZ2BHY&ref_=pd_gw_cr_simh&pd_rd_w=c6f3f&pd_rd_r=0cea55db-d6b2-4783-a251-8207520b97aa'
#treye.crawler(url,API_USER,API_KEY)
price = treye.productprice
print(price)

# previous_price = 4000
# current_price = 5000
# while True:
#     print(current_price)
#     current_price = current_price - 100
#     time.sleep(0.5)
#     if current_price < previous_price:
#         print("Price dropped")
#         break
