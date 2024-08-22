from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from database import path_db
import sqlite3

class archive_players(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        bl = BoxLayout()
        
        conn = sqlite3.connect(path_db())
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM players")
        players = cursor.fetchall()
        
        conn.close()
        
        bl.add_widget(Label(text=f"Игроки: {players}"))
        
        archive = Button(text="Назад")
        archive.bind(on_release=self.switch_archive)
        bl.add_widget(archive)
        
        self.add_widget(bl)
        
        
    def switch_archive(self, *args):
        self.manager.current = "Архив"