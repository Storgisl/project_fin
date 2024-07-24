from kivy.app import App
from kivy.uix.widget import Widget

import os

from processing.photo_processing.processing import open_file_chooser

os.environ['KIVY_GL_BACKEND'] = 'gl'

class CheckTest(Widget):
    pass

class CheckApp(App):
    def build(self):
        return CheckTest()
    self.upload_btn.bind(on_press=self.open_file_chooser)
if __name__ == "__main__":
    CheckApp().run()
