from kivy.app import App
from kivy.uix.widget import Widget
import os

os.environ['KIVY_GL_BACKEND'] = 'gl'

class CheckTest(Widget):
    pass

class CheckApp(App):
    def build(self):
        return CheckTest()

if __name__ == "__main__":
    CheckApp().run()
