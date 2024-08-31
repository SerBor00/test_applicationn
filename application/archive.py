from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

class archive(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bl = BoxLayout()
        
        archive_players = Button(text= "Игроки", size_hint=(None, None) , size = (270 , 60))
        archive_players.bind(on_press= self.switch_archive_players)
        bl.add_widget(archive_players)
        
        archive_matches = Button(text= "Матчи", size_hint=(None, None) , size = (270 , 60))
        archive_matches.bind(on_press= self.switch_archive_matches)
        bl.add_widget(archive_matches)
        
        fst_page = Button(text="Назад", size_hint=(None, None) , size = (270 , 60))
        fst_page.bind(on_release=self.switch_fst_page)
        bl.add_widget(fst_page)
        
        self.add_widget(bl)
    
    def switch_fst_page(self, *args):
        self.manager.current = "Главная"
        
    def switch_archive_players(self, *args):
        self.manager.current = "Архив игроков"
        
    def switch_archive_matches(self, *args):
        self.manager.current = "Архив матчей"