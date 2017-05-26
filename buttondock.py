# File name: buttondock.py
#this is a button dock for actions to be automated via a gui button list.
###############################
#by jake goodwin
###############################
import kivy
kivy.require('1.10.0') #only accept new kivy version.

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

#change the size of the window.
Window.size = (150, 400)

class ButtonDock(BoxLayout):
    pass

class ButtonDockApp(App):
    def build(self):
        return ButtonDock()

if __name__=="__main__":
    ButtonDockApp().run()
