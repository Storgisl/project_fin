from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

def __init__(self, **kwargs):
    # make sure we aren't overriding any important functionality
    super(RootWidget, self).__init__(**kwargs)
