from kivy.app import App
from screens.manager import DobbyScreenManager
from screens.home import HomeScreen

class DobbyPiApp(App):
    def build(self):
        screenManager = DobbyScreenManager()
        screenManager.add_widget()
        return DobbyScreenManager()

if __name__ == '__main__':
    DobbyPiApp().run()