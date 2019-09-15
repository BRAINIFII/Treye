import requests
from bs4 import BeautifulSoup
import sys
import Tmodules.treye as treye



headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
global URL
#URL = ["https://amzn.to/321zkTQ",
#"https://amzn.to/321A8YS"
#,"https://amzn.to/2U6oRnE"
#]

def test():
        #treye.crawler("link",API_USER,API_KEY)
        treye.crawler("https://www.amazon.in/Canon-1500D-Digital-Camera-S18-55/dp/B07BS4TJ43/ref=br_msw_pdt-3?_encoding=UTF8&smid=A14CZOWI0VEHLG&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=TFYA7CMNFXK0250QS2XR&pf_rd_t=36701&pf_rd_p=99ee64af-e6ec-417e-a806-700ff584a89b&pf_rd_i=desktop","o_5otfp6st4u","R_e33e927940d9462b8db74fc436ef7ed9")
        treye.notify()
        treye.crawler("https://www.amazon.in/gp/product/B015C7SC5U?pf_rd_p=63f66ec5-8654-4c00-843f-8b32d0b1d487&pf_rd_r=TFYA7CMNFXK0250QS2XR","o_5otfp6st4u","R_e33e927940d9462b8db74fc436ef7ed9")
        treye.notify()
test()