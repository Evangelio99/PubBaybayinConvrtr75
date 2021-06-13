from ..pages.page import *

"""
defualt widget color:

#201F1E - grey
"""

#text color
def_bg = "white"
def_fg = "black"

class HomePage(Page):
    def __init__(self, parent):
        print("Showing home page")


        # init page/ delete old page
        Page.__init__(self, parent)

        t = Label(self, text="This is home page", bg=def_bg, fg=def_fg)
        t.place(x=100, y=100)

class SettingsPage(Page):
    def __init__(self, parent):
        print("Showing settings page")


        # init page/ delete old page
        Page.__init__(self, parent)

        t = Label(self, text="This is settings page", bg=def_bg, fg=def_fg)
        t.place(x=100, y=100)

class HelpPage(Page):
    def __init__(self, parent):
        print("Showing help page")

        # init page/ delete old page
        Page.__init__(self, parent)

        t = Label(self, text="This is Help Page", bg=def_bg, fg=def_fg)
        t.place(x=100, y=100)

class AboutPage(Page):
    def __init__(self, parent):
        print("Showing about page")

        #init page/ delete oldpage
        Page.__init__(self,parent)

        t = Label(self, text="This is about page", bg=def_bg, fg=def_fg)
        t.place(x=100,y=100)
