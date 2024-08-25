from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Rectangle, Color
from kivy.uix.widget import Widget
from kivy.graphics import RoundedRectangle

from fst_page import fst_page
from match_plus import match_plus
from player_plus import player_plus
from archive import archive
from players2 import players2
from players3 import players3
from players4 import players4
from players5 import players5
from archive_players import archive_players
from archive_matches import archive_matches

class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        sm = MyScreenManager()
        
        sm.add_widget(fst_page(name= "Главная"))
        sm.add_widget(match_plus(name= "Игра+"))
        sm.add_widget(player_plus(name= "Игрок+"))
        sm.add_widget(archive(name= "Архив"))
        sm.add_widget(players2(name= "2 Игрока"))
        sm.add_widget(players3(name= "3 Игрока"))
        sm.add_widget(players4(name= "4 Игрока"))
        sm.add_widget(players5(name= "5 Игрока"))
        sm.add_widget(archive_players(name= "Архив игроков"))
        sm.add_widget(archive_matches(name= "Архив матчей"))
        return sm

if __name__ == "__main__":
    MyApp().run()