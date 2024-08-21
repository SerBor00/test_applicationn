from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
import sqlite3

class archive_players(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        bl = BoxLayout()
        
        
        
        archive = Button(text="Назад")
        archive.bind(on_release=self.switch_archive)
        bl.add_widget(archive)
        
        self.add_widget(bl)
        
        
    def switch_archive(self, *args):
        self.manager.current = "Архив"