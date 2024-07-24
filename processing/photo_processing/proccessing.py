from kivy.uix.filechooser import FileChooserListView
from kivy.uix.boxlayout import BoxLayout

def open_file_chooser(instance):
    content = BoxLayout(orientation='vertical')
    filechooser = FileChooserListView(filters=['*.png', '*.jpg', '*.jpeg', '*.gif', '*.bmp'])
    select_btn = Button(text="Select", size_hint_y=None, height=50)

    def select_photo(instance):
            selected = filechooser.selection
            if selected:
                img.source = selected[0]
                popup.dismiss()

    popup = Popup(title="Select a Photo", content=content, size_hint=(0.9, 0.9))
        popup.open()
