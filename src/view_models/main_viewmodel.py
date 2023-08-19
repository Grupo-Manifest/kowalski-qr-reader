from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file("views/main_view.kv")
class MainView(Screen):
    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)
