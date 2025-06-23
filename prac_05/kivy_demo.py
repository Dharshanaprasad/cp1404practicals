from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    def build(self):
        self.title = "Kivy Demo"
        return Builder.load_file('kivy_layout.kv')

BoxLayoutDemo().run()
