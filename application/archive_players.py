from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from database import path_db
import sqlite3

class archive_players(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        bl = BoxLayout()
        
        self.search = TextInput(hint_text= "имя фамилия",foreground_color = ('#02034e'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e") , border = (0.1 , 0.1 , 0.1 , 0.1)  ,hint_text_color = "#6188a3", font_name = 'application/shrift/TT Norms Pro Medium.otf', multiline=False, size_hint_y=None, height= 32, size_hint=(None, None) , size = (400 , 32))
        bl.add_widget(self.search)
        
        self.conn = sqlite3.connect(path_db())
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("SELECT first_and_second_name , date_of_born , gender FROM players")
        self.players = self.cursor.fetchall()
        
        
        
        for i in self.players:
            bl.add_widget(Label(text=f"Игроки: {i}" , color = "#02034e", size_hint_y=None, height= 64 , font_size =20 , size_hint=(None, None) , size = (500 , 64)))
        
        archive = Button(text="Назад", size_hint=(None, None) , size = (270 , 60))
        archive.bind(on_release=self.switch_archive)
        bl.add_widget(archive)
        
        self.add_widget(bl)
        
    def on_search (self, *args):
        search = self.search.text.title()
        self.cursor.execute("""
            SELECT first_and_second_name , date_of_born , gender FROM players WHERE first_and_second_name = ?    
        """, (search,))
        self.players = self.cursor.fetchone()
        
        
    def switch_archive(self, *args):
        self.conn.close()
        self.manager.current = "Архив"