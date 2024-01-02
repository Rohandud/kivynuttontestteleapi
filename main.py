from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class DemoApp(MDApp):
    def build(self):
        label = MDLabel(text="hello",halign='center')
        return label

if __name__ == "__main__":
    DemoApp().run()
