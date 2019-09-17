from infi.systray import SysTrayIcon
import GUI
def say_hello(systray):
    GUI.vp_start_gui()

menu_options = (("Open GUI", None, say_hello),)
systray = SysTrayIcon("icon/icon.ico", "Treye", menu_options)
#systray.shutdown()
systray.start()

