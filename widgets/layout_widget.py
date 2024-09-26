from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup

class RootWidget(AnchorLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

        self.add_widget(
                Button(
                    text="Click",
                    size_hint=(.5, .5),
                    on_press=self.open_filechooser,
                )
        )
    def open_filechooser(self, instance):
        # Create a FileChooserListView or FileChooserIconView
        filechooser = FileChooserListView()

        # Create a layout to hold the filechooser and buttons
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(filechooser)

        # Create a button to close the popup
        close_button = Button(text="Close", size_hint=(1, 0.1))
        close_button.bind(on_press=self.close_popup)
        layout.add_widget(close_button)

        # Create the popup
        self.popup = Popup(title='FileChooser', content=layout, size_hint=(0.9, 0.9))
        self.popup.open()

    def close_popup(self, instance):
        self.popup.dismiss()


