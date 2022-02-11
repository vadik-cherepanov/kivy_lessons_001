from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from pygments.lexers import PythonLexer


class MainApp(App):

    def build(self):
        box = BoxLayout(orientation='vertical')
        codeinput = CodeInput(lexer=PythonLexer())
        box.add_widget(codeinput)
        return box

    # def on(self, *args):
    #



if __name__ == '__main__':
    app = MainApp()
    MainApp().run()
