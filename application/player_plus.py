from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from database import path_db
import sqlite3

class player_plus(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bl = BoxLayout()
                
        bl = BoxLayout(spacing= 20 , padding= 5)
                
        high_text = Label(text= "Регистрация" , color = "#02034e", size_hint_y=None, height= 32 , font_size =32)
        bl.add_widget(high_text)
        
        bl.add_widget(Label(text="Имя и Фамилия" , color = "#02034e", size_hint_y=None, height= 32 , font_size =26))        
        self.namer = TextInput(hint_text= "Вася Пупкин", multiline=False, size_hint_y=None, height= 32 )
        bl.add_widget(self.namer)
        
        bl.add_widget(Label(text= "Дата рождения" , color = "#02034e", size_hint_y=None, height= 32 , font_size =26))
        self.date = TextInput(hint_text= "дд.мм.гггг", multiline=False, size_hint_y=None, height= 32)
        bl.add_widget(self.date)
        
        bl.add_widget(Label(text= "Пол" , color = "#02034e", size_hint_y=None, height= 32 , font_size =26))
        self.gender = TextInput(hint_text= "Муж / Жен", multiline=False, size_hint_y=None, height= 32)
        bl.add_widget(self.gender)
        
        checkpoint = Button(text= "Сохранить")
        checkpoint.bind(on_release=self.checkpoint_info)
        bl.add_widget(checkpoint)
        
        fst_page = Button(text="Назад")
        fst_page.bind(on_release=self.switch_fst_page)
        bl.add_widget(fst_page)
        
        self.add_widget(bl)
    
    def switch_fst_page(self, *args):
        self.manager.current = "Главная"
        
    def checkpoint_info(self, *args):
        name = self.namer.text
        date = self.date.text
        gender = self.gender.text
        
        
        conn = sqlite3.connect(path_db())
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO players (first_and_second_name, date_of_born, gender) VALUES (?, ?, ?)", (name, date, gender))

        conn.commit()
        conn.close()
        