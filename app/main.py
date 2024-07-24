from kivy.app import App
from kivy.uix.widget import Widget

import os

from processing.photo_processing import proccessing

os.environ['KIVY_GL_BACKEND'] = 'gl'

class CheckTest(Widget):
    pass

class CheckApp(App):
    def build(self):
        self.upload_btn.bind(on_press=proccessing.open_file_chooser)
        return CheckTest()

if __name__ == "__main__":
    CheckApp().run()
