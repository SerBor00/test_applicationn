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
        main_bl = BoxLayout(size_hint=(1, None), height=900)
        bl2 = BoxLayout(size_hint=(1, None), height=700, padding= (100 , 1 , 1 , 1), spacing= 20 )        
        bl = BoxLayout(size_hint=(1, None), height=200 , padding= (100 , 1 , 1 , 1))
                
        high_text = Label(text= "РЕГИСТРАЦИЯ" , color = "#02034e", size_hint_y=None, height= 32 , font_size =32, size_hint=(None, None) , size = (300 , 32))
        bl2.add_widget(high_text)
        
        bl2.add_widget(Label(text="имя и фамилия" , color = "#02034e", size_hint_y=None, height= 32 , font_size =26, size_hint=(None, None) , size = (300 , 32)))        
        self.namer = TextInput(hint_text= "Вася Пупкин", multiline=False, size_hint_y=None, height= 32, size_hint=(None, None) , size = (300 , 32), padding= (1 , 1 , 1 , 1 ), font_size =25)
        bl2.add_widget(self.namer)
        
        bl2.add_widget(Label(text= "дата рождения" , color = "#02034e", size_hint_y=None, height= 32 , font_size =26, size_hint=(None, None) , size = (300 , 32)))
        self.date = TextInput(hint_text= "дд.мм.гггг", multiline=False, size_hint_y=None, height= 32, size_hint=(None, None) , size = (300 , 32), padding= (92 , 1 , 1 , 1), font_size =25)
        bl2.add_widget(self.date)
        
        bl2.add_widget(Label(text= "пол" , color = "#02034e", size_hint_y=None, height= 32 , font_size =26, size_hint=(None, None) , size = (300 , 32)))
        self.gender = TextInput(hint_text= "муж / жен", multiline=False, size_hint_y=None, height= 32, size_hint=(None, None) , size = (300 , 32), padding= (88 , 1 , 1 , 1), font_size =25)
        bl2.add_widget(self.gender)
        
        checkpoint = Button(text= "сохранить" , size_hint=(None, None) , size = (300 , 60))
        checkpoint.bind(on_release=self.checkpoint_info)
        bl.add_widget(checkpoint)
        
        fst_page = Button(text="назад" , size_hint=(None, None) , size = (300 , 60))
        fst_page.bind(on_release=self.switch_fst_page)
        bl.add_widget(fst_page)
        
        main_bl.add_widget(bl2)
        main_bl.add_widget(bl)
        
        self.add_widget(main_bl)
    
    def switch_fst_page(self, *args):
        self.manager.current = "Главная"
        
    def checkpoint_info(self, *args):
        name = self.namer.text.title()
        date = self.date.text
        gender = self.gender.text.title()
        
        
        conn = sqlite3.connect(path_db())
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO players (first_and_second_name, date_of_born, gender) VALUES (?, ?, ?)", (name, date, gender))

        conn.commit()
        conn.close()
        