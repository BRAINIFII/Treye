from infi.systray import SysTrayIcon
import GUI
import time
from win10toast import ToastNotifier
import os
import sys
import psycopg2


def say_hello(systray):
    GUI.vp_start_gui()

toaster = ToastNotifier()
prog_call = sys.argv[0]
prog_location = os.path.split(prog_call)[0]
toast_logo = os.path.join(prog_location,"../icon/icon.ico")
toaster.show_toast("Treye","Treye is minimized in tray.",icon_path=toast_logo,duration=9,threaded=True)
    

menu_options = (("Open GUI", None, say_hello),)
systray = SysTrayIcon("icon/icon.ico", "Treye", menu_options)
#systray.shutdown()
systray.start()


conn = psycopg2.connect(user = "postgres",
                            password = os.environ['PG_PASSWORD'],
                            host = "127.0.0.1",
                            port = "5432",
                            database = "Treye_data")
cursor = conn.cursor()

# concept
# previous_price = 4000
# current_price = 5000
# while True:
#     print(current_price)
#     current_price = current_price - 100
#     time.sleep(0.5)
#     if current_price < previous_price:
#         print("Price dropped")
#         break
