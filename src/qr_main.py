from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

from view_models.main_viewmodel import MainView

class QrMain(MDApp):
    def build(self):
        screen_manager = MDScreenManager()
        screen_manager.add_widget(MainView())

        return screen_manager


if __name__ == "__main__":
    QrMain().run()