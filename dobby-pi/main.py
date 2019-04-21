from kivy.app import App
from home import HomeWidget

class DobbyPiApp(App):
    def build(self):
        return HomeWidget()

if __name__ == '__main__':
    DobbyPiApp().run()