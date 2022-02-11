from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '60')

class KgWeight(BoxLayout):
    kg_input = ObjectProperty(None)
    gramm_result = ObjectProperty(None)
    def convert_to_gramm(self):
        self.gramm_result.text = str(float(self.kg_input.text) * 1000)

class KgApp(App):
    def build(self):
        kg_weight = KgWeight()
        return kg_weight

if __name__ == '__main__':
     KgApp().run()
