from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from models.qr_code_model import QRCodeModel

Builder.load_file("views/main_view.kv")
class MainView(Screen):
    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.qr_code_handler = QRCodeModel()


    def on_symbols(self, instance, symbols):
        self.qr_code_handler.handle_symbols(instance, symbols)
