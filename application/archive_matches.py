from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from database import path_db
import sqlite3

class archive_matches(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        bl = BoxLayout()
        
        self.search = TextInput(hint_text = "Имя и Фамилия игрока", multiline=False, size_hint_y=None, height= 32, size_hint=(None, None) , size = (500 , 32))
        bl.add_widget(self.search)
        
        self.conn = sqlite3.connect(path_db())
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("SELECT players.first_and_second_name , matches.name_of_game , matches.date_of_game , matches.name_of_team , match_persteges_info.dro_persent , match_persteges_info.take_persent , match_persteges_info.guard_persent , match_persteges_info.final_persent , match_persteges_info.end_1_persent , match_persteges_info.end_2_persent , match_persteges_info.end_3_persent , match_persteges_info.end_4_persent , match_persteges_info.end_6_persent , match_persteges_info.end_7_persent , match_persteges_info.end_8_persent , match_persteges_info.end_9_persent , match_persteges_info.end_10_persent , match_persteges_info.ex_1_end_persent , match_persteges_info.ex_2_end_persent , match_persteges_info.ex_3_end_persent FROM players JOIN match_players ON players.player_id = match_players.player_id JOIN matches ON match_players.match_id = matches.match_id JOIN match_stats ON matches.match_id = match_stats.match_id JOIN match_persteges_info ON match_stats.points_id = match_persteges_info.points_id;")
        self.match_players = self.cursor.fetchall()
        
        for i in self.match_players:
            bl.add_widget(Label(text= f"Очки: {i}"))
        

        archive = Button(text="Назад", size_hint=(None, None) , size = (270 , 60))
        archive.bind(on_release=self.switch_archive)
        bl.add_widget(archive)
        self.add_widget(bl)
        
    def on_search(self, *args):
        search = self.search.text
        
        
    def switch_archive(self, *args):
        self.conn.close()
        self.manager.current = "Архив"