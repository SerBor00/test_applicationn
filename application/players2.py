from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from database import path_db, inp_filter
import sqlite3

class players2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bl = BoxLayout(size_hint_y=None, height= 300) #height=300
        gl = GridLayout(cols= 2 , spacing=(15 , 5) , padding= (60 , 1 , 1 , 1))
        gl2 = GridLayout(cols=5, rows=39, spacing=(15 , 5), padding= 1, size_hint_y=None, height= 2700) #height=1200
        fl2 = FloatLayout(size_hint_y=None, height= 200) #height=200
        main_bl = BoxLayout(size_hint=(1, None), height=3330) #height=1830
        
        bl.add_widget(Label(text= "Название команды" , color = "#02034e", size_hint_y=None, height= 32 , font_size =28 ))
        self.name_team = TextInput(hint_text= "Приморкий край" , multiline=False, size_hint_y=None, height= 32)
        bl.add_widget(self.name_team)
        
        bl.add_widget(Label(text= "Название игры" , color = "#02034e", size_hint_y=None, height= 32 , font_size =24 ))
        self.name_match = TextInput(hint_text= "Первенство России среди кого и какого возраста", multiline=False, size_hint_y=None, height= 32)
        bl.add_widget(self.name_match)
        
        bl.add_widget(Label(text= "дата игры" , color = "#02034e", size_hint_y=None, height= 32 , font_size =24 ))
        self.date_match = TextInput(hint_text= "дд.мм.гггг", multiline=False, size_hint_y=None, height= 32)
        bl.add_widget(self.date_match)
        
        gl.add_widget(Label(text= "Имя и Фамилия" , color = "#02034e", size_hint_y=None, height= 32 , font_size =22 ))
        gl.add_widget(Label(text= "Имя и Фамилия" , color = "#02034e", size_hint_y=None, height= 32 , font_size =22 ))
        self.name_1 = TextInput(hint_text= "Имя и Фамилия", size_hint_y=None, height= 32)
        gl.add_widget(self.name_1)
        self.name_2 = TextInput(hint_text= "Имя и Фамилия", size_hint_y=None, height= 32)
        gl.add_widget(self.name_2)
        
        gl2.add_widget(Label(text="1" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_1)
        self.one_1_button = Button(text="-")
        self.one_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_1_button)
        self.one_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_2)
        self.one_2_button = Button(text="-")
        self.one_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_2_button)
        
        gl2.add_widget(Label(text="2" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.two_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_1)
        self.two_1_button = Button(text="-")
        self.two_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_1_button)
        self.two_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_2)
        self.two_2_button = Button(text="-")
        self.two_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_2_button)
        
        gl2.add_widget(Label(text="3" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.three_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.three_1)
        self.three_1_button = Button(text="-")
        self.three_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.three_1_button)
        self.three_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.three_2)
        self.three_2_button = Button(text="-")
        self.three_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.three_2_button)
        
        gl2.add_widget(Label(text="4" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.four_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.four_1)
        self.four_1_button = Button(text="-")
        self.four_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.four_1_button)
        self.four_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.four_2)
        self.four_2_button = Button(text="-")
        self.four_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.four_2_button)
        
        gl2.add_widget(Label(text="5" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.five_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.five_1)
        self.five_1_button = Button(text="-")
        self.five_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.five_1_button)
        self.five_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.five_2)
        self.five_2_button = Button(text="-")
        self.five_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.five_2_button)
        
        gl2.add_widget(Label(text="6" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.six_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.six_1)
        self.six_1_button = Button(text="-")
        self.six_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.six_1_button)
        self.six_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.six_2)
        self.six_2_button = Button(text="-")
        self.six_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.six_2_button)
        
        gl2.add_widget(Label(text="7" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.seven_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.seven_1)
        self.seven_1_button = Button(text="-")
        self.seven_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.seven_1_button)
        self.seven_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.seven_2)
        self.seven_2_button = Button(text="-")
        self.seven_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.seven_2_button)
        
        gl2.add_widget(Label(text="8" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.eight_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.eight_1)
        self.eight_1_button = Button(text="-")
        self.eight_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.eight_1_button)
        self.eight_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.eight_2)
        self.eight_2_button = Button(text="-")
        self.eight_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.eight_2_button)
        
        gl2.add_widget(Label(text="9" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.nine_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.nine_1)
        self.nine_1_button = Button(text="-")
        self.nine_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.nine_1_button)
        self.nine_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.nine_2)
        self.nine_2_button = Button(text="-")
        self.nine_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.nine_2_button)
        
        gl2.add_widget(Label(text="10" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_zero_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_zero_1)
        self.one_zero_1_button = Button(text="-")
        self.one_zero_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_zero_1_button)
        self.one_zero_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_zero_2)
        self.one_zero_2_button = Button(text="-")
        self.one_zero_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_zero_2_button)
        
        gl2.add_widget(Label(text="11" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_one_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_one_1)
        self.one_one_1_button = Button(text="-")
        self.one_one_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_one_1_button)
        self.one_one_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_one_2)
        self.one_one_2_button = Button(text="-")
        self.one_one_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_one_2_button)
        
        gl2.add_widget(Label(text="12" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_two_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_two_1)
        self.one_two_1_button = Button(text="-")
        self.one_two_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_two_1_button)
        self.one_two_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_two_2)
        self.one_two_2_button = Button(text="-")
        self.one_two_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_two_2_button)
        
        gl2.add_widget(Label(text="13" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_three_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_three_1)
        self.one_three_1_button = Button(text="-")
        self.one_three_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_three_1_button)
        self.one_three_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_three_2)
        self.one_three_2_button = Button(text="-")
        self.one_three_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_three_2_button)
        
        gl2.add_widget(Label(text="14" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_four_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_four_1)
        self.one_four_1_button = Button(text="-")
        self.one_four_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_four_1_button)
        self.one_four_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_four_2)
        self.one_four_2_button = Button(text="-")
        self.one_four_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_four_2_button)
        
        gl2.add_widget(Label(text="15" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_five_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_five_1)
        self.one_five_1_button = Button(text="-")
        self.one_five_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_five_1_button)
        self.one_five_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_five_2)
        self.one_five_2_button = Button(text="-")
        self.one_five_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_five_2_button)
        
        gl2.add_widget(Label(text="16" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_six_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_six_1)
        self.one_six_1_button = Button(text="-")
        self.one_six_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_six_1_button)
        self.one_six_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_six_2)
        self.one_six_2_button = Button(text="-")
        self.one_six_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_six_2_button)
        
        gl2.add_widget(Label(text="17" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_seven_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_seven_1)
        self.one_seven_1_button = Button(text="-")
        self.one_seven_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_seven_1_button)
        self.one_seven_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_seven_2)
        self.one_seven_2_button = Button(text="-")
        self.one_seven_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_seven_2_button)
        
        gl2.add_widget(Label(text="18" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_eight_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_eight_1)
        self.one_eight_1_button = Button(text="-")
        self.one_eight_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_eight_1_button)
        self.one_eight_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_eight_2)
        self.one_eight_2_button = Button(text="-")
        self.one_eight_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_eight_2_button)
        
        gl2.add_widget(Label(text="19" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_nine_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_nine_1)
        self.one_nine_1_button = Button(text="-")
        self.one_nine_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_nine_1_button)
        self.one_nine_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_nine_2)
        self.one_nine_2_button = Button(text="-")
        self.one_nine_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_nine_2_button)
        
        gl2.add_widget(Label(text="20" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.two_zero_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_zero_1)
        self.two_zero_1_button = Button(text="-")
        self.two_zero_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_zero_1_button)
        self.two_zero_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_zero_2)
        self.two_zero_2_button = Button(text="-")
        self.two_zero_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_zero_2_button)
        
        gl2.add_widget(Label(text="21" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.two_one_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_one_1)
        self.two_one_1_button = Button(text="-")
        self.two_one_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_one_1_button)
        self.two_one_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_one_2)
        self.two_one_2_button = Button(text="-")
        self.two_one_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_one_2_button)
        
        gl2.add_widget(Label(text="22" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.two_two_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_two_1)
        self.two_two_1_button = Button(text="-")
        self.two_two_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_two_1_button)
        self.two_two_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_two_2)
        self.two_two_2_button = Button(text="-")
        self.two_two_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_two_2_button)
        
        gl2.add_widget(Label(text="23" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.two_three_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_three_1)
        self.two_three_1_button = Button(text="-")
        self.two_three_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_three_1_button)
        self.two_three_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_three_2)
        self.two_three_2_button = Button(text="-")
        self.two_three_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_three_2_button)
        
        gl2.add_widget(Label(text="24" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.two_four_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_four_1)
        self.two_four_1_button = Button(text="-")
        self.two_four_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_four_1_button)
        self.two_four_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_four_2)
        self.two_four_2_button = Button(text="-")
        self.two_four_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_four_2_button)
        
        gl2.add_widget(Label(text="25" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.two_five_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_five_1)
        self.two_five_1_button = Button(text="-")
        self.two_five_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_five_1_button)
        self.two_five_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_five_2)
        self.two_five_2_button = Button(text="-")
        self.two_five_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_five_2_button)
        
        gl2.add_widget(Label(text="26" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.two_six_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_six_1)
        self.two_six_1_button = Button(text="-")
        self.two_six_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_six_1_button)
        self.two_six_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_six_2)
        self.two_six_2_button = Button(text="-")
        self.two_six_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_six_2_button)
        
        gl2.add_widget(Label(text="27" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.two_seven_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_seven_1)
        self.two_seven_1_button = Button(text="-")
        self.two_seven_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_seven_1_button)
        self.two_seven_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_seven_2)
        self.two_seven_2_button = Button(text="-")
        self.two_seven_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_seven_2_button)
        
        gl2.add_widget(Label(text="28" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.two_eight_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_eight_1)
        self.two_eight_1_button = Button(text="-")
        self.two_eight_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_eight_1_button)
        self.two_eight_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_eight_2)
        self.two_eight_2_button = Button(text="-")
        self.two_eight_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_eight_2_button)
        
        gl2.add_widget(Label(text="29" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.two_nine_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_nine_1)
        self.two_nine_1_button = Button(text="-")
        self.two_nine_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_nine_1_button)
        self.two_nine_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_nine_2)
        self.two_nine_2_button = Button(text="-")
        self.two_nine_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_nine_2_button)
        
        gl2.add_widget(Label(text="30" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.three_zero_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.three_zero_1)
        self.three_zero_1_button = Button(text="-")
        self.three_zero_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.three_zero_1_button)
        self.three_zero_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.three_zero_2)
        self.three_zero_2_button = Button(text="-")
        self.three_zero_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.three_zero_2_button)
        
        gl2.add_widget(Label(text="extra-1" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.extra_one_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_one_1)
        self.extra_one_1_button = Button(text="-")
        self.extra_one_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_one_1_button)
        self.extra_one_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_one_2)
        self.extra_one_2_button = Button(text="-")
        self.extra_one_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_one_2_button)
        
        gl2.add_widget(Label(text="extra-2" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.extra_two_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_two_1)
        self.extra_two_1_button = Button(text="-")
        self.extra_two_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_two_1_button)
        self.extra_two_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_two_2)
        self.extra_two_2_button = Button(text="-")
        self.extra_two_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_two_2_button)
        
        gl2.add_widget(Label(text="extra-3" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.extra_three_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_three_1)
        self.extra_three_1_button = Button(text="-")
        self.extra_three_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_three_1_button)
        self.extra_three_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_three_2)
        self.extra_three_2_button = Button(text="-")
        self.extra_three_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_three_2_button)
        
        gl2.add_widget(Label(text="extra-4" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.extra_four_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_four_1)
        self.extra_four_1_button = Button(text="-")
        self.extra_four_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_four_1_button)
        self.extra_four_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_four_2)
        self.extra_four_2_button = Button(text="-")
        self.extra_four_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_four_2_button)
        
        gl2.add_widget(Label(text="extra-5" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.extra_five_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_five_1)
        self.extra_five_1_button = Button(text="-")
        self.extra_five_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_five_1_button)
        self.extra_five_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_five_2)
        self.extra_five_2_button = Button(text="-")
        self.extra_five_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_five_2_button)
        
        gl2.add_widget(Label(text="extra-6" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.extra_six_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_six_1)
        self.extra_six_1_button = Button(text="-")
        self.extra_six_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_six_1_button)
        self.extra_six_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_six_2)
        self.extra_six_2_button = Button(text="-")
        self.extra_six_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_six_2_button)
        
        gl2.add_widget(Label(text="extra-7" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.extra_seven_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_seven_1)
        self.extra_seven_1_button = Button(text="-")
        self.extra_seven_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_seven_1_button)
        self.extra_seven_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_seven_2)
        self.extra_seven_2_button = Button(text="-")
        self.extra_seven_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_seven_2_button)
        
        gl2.add_widget(Label(text="extra-8" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.extra_eight_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_eight_1)
        self.extra_eight_1_button = Button(text="-")
        self.extra_eight_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_eight_1_button)
        self.extra_eight_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_eight_2)
        self.extra_eight_2_button = Button(text="-")
        self.extra_eight_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_eight_2_button)
        
        gl2.add_widget(Label(text="extra-9" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.extra_nine_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_nine_1)
        self.extra_nine_1_button = Button(text="-")
        self.extra_nine_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_nine_1_button)
        self.extra_nine_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_nine_2)
        self.extra_nine_2_button = Button(text="-")
        self.extra_nine_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_nine_2_button)
        
        self.final_percentage_1 = Label(text="", pos=(20, 40))
        self.types_throw_1 = Label(text="", pos=(20, -20))
        self.final_percentage_2 = Label(text="", pos=(120, 40))
        self.types_throw_2 = Label(text="", pos=(120, -20))
        
        fl2.add_widget(self.final_percentage_1)
        fl2.add_widget(self.types_throw_1)
        fl2.add_widget(self.final_percentage_2)
        fl2.add_widget(self.types_throw_2)
        
        end = Button(text= "Рассчёт", pos=(0, 90))
        end.bind(on_release=self.math_operation)
        fl2.add_widget(end)
        
        match_plus = Button(text= "Назад")
        match_plus.bind(on_release=self.switch_match_plus)
        fl2.add_widget(match_plus)
        
        main_bl.add_widget(bl)
        main_bl.add_widget(gl)
        main_bl.add_widget(gl2)
        main_bl.add_widget(fl2)
        
        scroll = ScrollView()
        scroll.add_widget(main_bl)
        
        self.add_widget(scroll)
    
    def switch_button_type(self, instance):
        new_type_throw = "-DTG"
        type_throw = new_type_throw.find(instance.text)
        type_throw =(type_throw +1) % len(new_type_throw)
        instance.text = new_type_throw[type_throw]
        return instance.text
    
    def switch_match_plus(self, *args):
        self.manager.current = "Игра+"

    def math_operation(self, *args):
        
        flag = True
        sum_dro = 0
        sum_take = 0
        sum_guard = 0
        
        helper = 0
        listik = [self.one_1.text, self.two_1.text, self.three_1.text, self.four_1.text, self.five_1.text, self.six_1.text, self.seven_1.text, self.eight_1.text, self.nine_1.text, self.one_zero_1.text,
                  self.one_one_1.text, self.one_two_1.text, self.one_three_1.text, self.one_four_1.text, self.one_five_1.text, self.one_six_1.text, self.one_seven_1.text, self.one_eight_1.text, self.one_nine_1.text,
                  self.two_zero_1.text, self.two_one_1.text, self.two_two_1.text, self.two_three_1.text, self.two_four_1.text, self.two_five_1.text, self.two_six_1.text, self.two_seven_1.text, self.two_eight_1.text,
                  self.two_nine_1.text, self.three_zero_1.text, self.extra_one_1.text, self.extra_two_1.text, self.extra_three_1.text, self.extra_four_1.text, self.extra_five_1.text,
                  self.extra_six_1.text, self.extra_seven_1.text, self.extra_eight_1.text, self.extra_nine_1.text]
        
        type_listik = [self.one_1_button.text, self.two_1_button.text, self.three_1_button.text, self.four_1_button.text, self.five_1_button.text, self.six_1_button.text, self.seven_1_button.text, self.eight_1_button.text, self.nine_1_button.text,
                       self.one_zero_1_button.text, self.one_one_1_button.text, self.one_two_1_button.text, self.one_three_1_button.text, self.one_four_1_button.text, self.one_five_1_button.text, self.one_six_1_button.text, self.one_seven_1_button.text,
                       self.one_eight_1_button.text, self.one_nine_1_button.text, self.two_zero_1_button.text, self.two_one_1_button.text, self.two_two_1_button.text, self.two_three_1_button.text, self.two_four_1_button.text, self.two_five_1_button.text,
                       self.two_six_1_button.text, self.two_seven_1_button.text, self.two_eight_1_button.text, self.two_nine_1_button.text, self.three_zero_1_button.text, self.extra_one_1_button.text, self.extra_two_1_button.text, self.extra_three_1_button.text,
                       self.extra_four_1_button.text, self.extra_five_1_button.text, self.extra_six_1_button.text, self.extra_seven_1_button.text, self.extra_eight_1_button.text, self.extra_nine_1_button.text]
        
        for i in range(len(listik)):
            if listik[i] == "":
                helper = i
                break
            elif len(listik[i]) > 1:
                flag = False
            else:
                listik[i] = int(listik[i])
                continue
        else:
            helper = len(listik)
            
        if len(listik) - (listik.count("") + helper) == 0 and helper != 0 and flag == True:
            
            listik = listik[:helper]
            type_listik = type_listik[:helper]
        
            for i in range(len(type_listik)):
                if type_listik[i] == "D":
                    sum_dro += listik[i]
                    continue
                if type_listik[i] == "T":
                    sum_take += listik[i]
                    continue
                if type_listik[i] == "G":
                    sum_guard += listik[i]
                    continue
        
            helper = round(sum(listik) / (helper*4) * 100, 2)
            if sum_dro != 0:
                sum_dro = round(sum_dro / (type_listik.count("D")*4) * 100,)
            if sum_take != 0:
                sum_take = round(sum_take / (type_listik.count("T")*4) * 100, 2)
            if sum_guard != 0:
                sum_guard = round(sum_guard / (type_listik.count("G")*4) * 100, 2)
        
            self.final_percentage_1.text = f"Процент: {helper}"
            self.types_throw_1.text = f"Dro: {sum_dro} \nTake: {sum_take} \nGuard: {sum_guard}"
        else:
            self.final_percentage_1.text = f"Ошибка, {helper}"
            self.types_throw_1.text = ""
        
        flag = True
        sum_dro = 0
        sum_take = 0
        sum_guard = 0
        
        helper = 0
        
        listik = [self.one_2.text, self.two_2.text, self.three_2.text, self.four_2.text, self.five_2.text, self.six_2.text, self.seven_2.text, self.eight_2.text, self.nine_2.text, self.one_zero_2.text,
                  self.one_one_2.text, self.one_two_2.text, self.one_three_2.text, self.one_four_2.text, self.one_five_2.text, self.one_six_2.text, self.one_seven_2.text, self.one_eight_2.text, self.one_nine_2.text,
                  self.two_zero_2.text, self.two_one_2.text, self.two_two_2.text, self.two_three_2.text, self.two_four_2.text, self.two_five_2.text, self.two_six_2.text, self.two_seven_2.text, self.two_eight_2.text,
                  self.two_nine_2.text, self.three_zero_2.text, self.extra_one_2.text, self.extra_two_2.text, self.extra_three_2.text, self.extra_four_2.text, self.extra_five_2.text,
                  self.extra_six_2.text, self.extra_seven_2.text, self.extra_eight_2.text, self.extra_nine_2.text]
        
        type_listik = [self.one_2_button.text, self.two_2_button.text, self.three_2_button.text, self.four_2_button.text, self.five_2_button.text, self.six_2_button.text, self.seven_2_button.text, self.eight_2_button.text, self.nine_2_button.text,
                       self.one_zero_2_button.text, self.one_one_2_button.text, self.one_two_2_button.text, self.one_three_2_button.text, self.one_four_2_button.text, self.one_five_2_button.text, self.one_six_2_button.text, self.one_seven_2_button.text,
                       self.one_eight_2_button.text, self.one_nine_2_button.text, self.two_zero_2_button.text, self.two_one_2_button.text, self.two_two_2_button.text, self.two_three_2_button.text, self.two_four_2_button.text, self.two_five_2_button.text,
                       self.two_six_2_button.text, self.two_seven_2_button.text, self.two_eight_2_button.text, self.two_nine_2_button.text, self.three_zero_2_button.text, self.extra_one_2_button.text, self.extra_two_2_button.text, self.extra_three_2_button.text,
                       self.extra_four_2_button.text, self.extra_five_2_button.text, self.extra_six_2_button.text, self.extra_seven_2_button.text, self.extra_eight_2_button.text, self.extra_nine_2_button.text]
        
        for i in range(len(listik)):
            if listik[i] == "":
                helper = i
                break
            elif len(listik[i]) > 1:
                flag = False
            else:
                listik[i] = int(listik[i])
                continue
        else:
            helper = len(listik)
            
        if len(listik) - (listik.count("") + helper) == 0 and helper != 0 and flag == True:
            
            listik = listik[:helper]
            type_listik = type_listik[:helper]
        
            for i in range(len(type_listik)):
                if type_listik[i] == "D":
                    sum_dro += listik[i]
                    continue
                if type_listik[i] == "T":
                    sum_take += listik[i]
                    continue
                if type_listik[i] == "G":
                    sum_guard += listik[i]
                    continue
        
            helper = round(sum(listik) / (helper*4) * 100, 2)
            if sum_dro != 0:
                sum_dro = round(sum_dro / (type_listik.count("D")*4) * 100,)
            if sum_take != 0:
                sum_take = round(sum_take / (type_listik.count("T")*4) * 100, 2)
            if sum_guard != 0:
                sum_guard = round(sum_guard / (type_listik.count("G")*4) * 100, 2)
        
            self.final_percentage_2.text = f"Процент: {helper}"
            self.types_throw_2.text = f"Dro: {sum_dro} \nTake: {sum_take} \nGuard: {sum_guard}"
        else:
            self.final_percentage_2.text = f"Ошибка, {helper}"
            self.types_throw_2.text = ""