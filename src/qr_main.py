from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class QrMain(MDApp):
    def build(self):
        return MDLabel(text="Hello, world!")


if __name__ == "__main__":
    QrMain().run()