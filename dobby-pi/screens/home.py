from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

class HomeScreen(Screen):
    quick_weave_btn = ObjectProperty(None)
    new_peg_plan_btn = ObjectProperty(None)

    def quick_weave_on_press(self, args):
        pass
