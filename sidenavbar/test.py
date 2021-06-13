
from TkinterSidebar.sidebar import *
from TkinterSidebar.pages.display_pages import *


root = Tk()

#screen size
root.resizable(False, False)
root.geometry("750x510")
main_frame = Frame(root, bg="white", width=1000, height=1000)
main_frame.place(x=200, y=0)


sidebar = SideBar(root)
sidebar.add_spacer("Menu")
sidebar.add_button("Home", lambda: HomePage(main_frame), icon="home.png")
sidebar.add_button("Settings", lambda: SettingsPage(main_frame), icon="settings.png")
sidebar.add_button("Help", lambda: HelpPage(main_frame), icon="help.png")
sidebar.add_button("About", lambda: AboutPage(main_frame), icon="about.png")


sidebar.finish()


root.mainloop()