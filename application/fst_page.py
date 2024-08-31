from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class fst_page(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bl = BoxLayout()
        match_p = Button(text="Игра+", size_hint=(None, None) , size = (270 , 60))
        player_p = Button(text="Игрок+", size_hint=(None, None) , size = (270 , 60))
        archive = Button(text="Архив", size_hint=(None, None) , size = (270 , 60))
        match_p.bind(on_release=self.switch_match_p)
        player_p.bind(on_release=self.switch_player_p)
        archive.bind(on_release=self.switch_archive)
        bl.add_widget(match_p)
        bl.add_widget(player_p)
        bl.add_widget(archive)
        self.add_widget(bl)
        
    def switch_match_p(self, *args):
        self.manager.current = "Игра+"
        
    def switch_player_p(self, *args):
        self.manager.current = "Игрок+"
        
    def switch_archive(self, *args):
        self.manager.current = "Архив"