from kivy.app import App

import os

from processing import *

os.environ['KIVY_GL_BACKEND'] = 'gl'

class CheckApp(App):
    def build(self):
        self.upload_btn.bind(on_press=open_file_chooser)
        return CheckTest()

if __name__ == "__main__":
    CheckApp().run()
