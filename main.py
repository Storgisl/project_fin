from kivy.app import App

import os

from widgets import *

os.environ['KIVY_GL_BACKEND'] = 'gl'

class CheckApp(App):
    def build(self):
        self.root=RootWidget()
        return self.root

if __name__ == "__main__":
    CheckApp().run()
