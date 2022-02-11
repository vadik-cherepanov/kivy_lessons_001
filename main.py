from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.colorpicker import ColorPicker


class MainApp(App):

    def build(self):
        box = BoxLayout(orientation='vertical')
        clr_picker = ColorPicker()
        box.add_widget(clr_picker)
        return box


if __name__ == '__main__':
    app = MainApp()
    MainApp().run()
