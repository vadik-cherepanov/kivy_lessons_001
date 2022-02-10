from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MainApp(App):

    def build(self):
        box = BoxLayout(orientation='vertical')
        btn = Button(text='Моя первая кнопка!', on_press=self.on)
        global label
        label = Label()
        box.add_widget(btn)
        box.add_widget(label)
        return box

    def on(self, *args):
        label.text = 'Hello, kivy!'



if __name__ == '__main__':
    app = MainApp()
    MainApp().run()
