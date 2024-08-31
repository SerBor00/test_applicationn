from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from database import path_db
import sqlite3

class archive_matches(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        bl = BoxLayout()
        
        self.search = TextInput(hint_text = "Имя и Фамилия игрока")
        bl.add_widget(self.search)
        
        self.conn = sqlite3.connect(path_db())
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("SELECT * FROM match_persteges_info")
        self.match_players = self.cursor.fetchall()
        
        for i in self.match_players:
            bl.add_widget(Label(text= f"Проценты: {i}"))
            
        
        archive = Button(text="Назад", size_hint=(None, None) , size = (270 , 60))
        archive.bind(on_release=self.switch_archive)
        bl.add_widget(archive)
        self.add_widget(bl)
        
    def on_search(self, *args):
        search = self.search.text
        
        
    def switch_archive(self, *args):
        self.conn.close()
        self.manager.current = "Архив"