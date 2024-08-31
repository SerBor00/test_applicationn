from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

class match_plus(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bl = BoxLayout()
        
        players2 = Button(text="2 игрока", size_hint=(None, None) , size = (270 , 60))
        players2.bind(on_release=self.switch_2_players)
        bl.add_widget(players2)
        
        players3 = Button(text="3 игрока", size_hint=(None, None) , size = (270 , 60))
        players3.bind(on_release=self.switch_3_players)
        bl.add_widget(players3)
        
        players4 = Button(text="4 игрока", size_hint=(None, None) , size = (270 , 60))
        players4.bind(on_release=self.switch_4_players)
        bl.add_widget(players4)
        
        players5 = Button(text="5 игрока", size_hint=(None, None) , size = (270 , 60))
        players5.bind(on_release=self.switch_5_players)
        bl.add_widget(players5)
        
        fst_page = Button(text="Назад", size_hint=(None, None) , size = (270 , 60))
        fst_page.bind(on_release=self.switch_fst_page)
        bl.add_widget(fst_page)
        
        self.add_widget(bl)
 
    def switch_2_players(self, *args):
        self.manager.current = "2 Игрока"
        
    def switch_3_players(self, *args):
        self.manager.current = "3 Игрока"
        
    def switch_4_players(self, *args):
        self.manager.current = "4 Игрока"
        
    def switch_5_players(self, *args):
        self.manager.current = "5 Игрока"
       
    def switch_fst_page(self, *args):
        self.manager.current = "Главная"
        
    
