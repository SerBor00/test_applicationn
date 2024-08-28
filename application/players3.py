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

class players3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bl = BoxLayout(size_hint_y=None, height= 300) #height= 300
        gl = GridLayout(cols= 3 , spacing=(15 , 5) , padding= (60 , 1 , 1 , 1))
        gl2 = GridLayout(cols=10, rows=26, spacing=(15 , 5), padding= 1, size_hint_y=None, height= 1920) #height= 950
        fl2 = FloatLayout(size_hint_y=None, height= 200) #height= 200
        main_bl = BoxLayout(size_hint=(1, None), height=2550) #height=1600
        
        bl.add_widget(Label(text= "Название команды" , color = "#02034e", size_hint_y=None, height= 32 , font_size =28 ))
        self.name_team = TextInput(hint_text= "Приморский край" , multiline=False, size_hint_y=None, height= 32)
        bl.add_widget(self.name_team)
        
        bl.add_widget(Label(text= "Название игры" , color = "#02034e", size_hint_y=None, height= 32 , font_size =24 ))
        self.name_match = TextInput(hint_text= "Первенство России среди кого и какого возраста", multiline=False, size_hint_y=None, height= 32)
        bl.add_widget(self.name_match)
        
        bl.add_widget(Label(text= "дата игры" , color = "#02034e", size_hint_y=None, height= 32 , font_size =24 ))
        self.date_match = TextInput(hint_text= "дд.мм.гггг", multiline=False, size_hint_y=None, height= 32)
        bl.add_widget(self.date_match)
        
        gl.add_widget(Label(text= "Имя и Фамилия" , color = "#02034e", size_hint_y=None, height= 32 , font_size =22 ))
        gl.add_widget(Label(text= "Имя и Фамилия" , color = "#02034e", size_hint_y=None, height= 32 , font_size =22 ))
        gl.add_widget(Label(text= "Имя и Фамилия" , color = "#02034e", size_hint_y=None, height= 32 , font_size =22 ))
        self.name_1 = TextInput(hint_text= "Имя и Фамилия", size_hint_y=None, height= 32)
        gl.add_widget(self.name_1)
        self.name_2 = TextInput(hint_text= "Имя и Фамилия", size_hint_y=None, height= 32)
        gl.add_widget(self.name_2)
        self.name_3 = TextInput(hint_text= "Имя и Фамилия", size_hint_y=None, height= 32)
        gl.add_widget(self.name_3)
        
        gl2.add_widget(Label(text="1" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_1)
        self.one_1_button = Button(text="-")
        self.one_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_1_button)
        gl2.add_widget(Label(text="end-1"))
        self.one_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_2)
        self.one_2_button = Button(text="-")
        self.one_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_2_button)
        gl2.add_widget(Label(text="end-1"))
        self.one_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_3)
        self.one_3_button = Button(text="-")
        self.one_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_3_button)
        gl2.add_widget(Label(text="end-1"))
        
        gl2.add_widget(Label(text="2" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.two_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_1)
        self.two_1_button = Button(text="-")
        self.two_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_1_button)
        self.end_one_1 = Label(text="%")
        gl2.add_widget(self.end_one_1)
        self.two_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_2)
        self.two_2_button = Button(text="-")
        self.two_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_2_button)
        self.end_one_2 = Label(text="%")
        gl2.add_widget(self.end_one_2)
        self.two_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_3)
        self.two_3_button = Button(text="-")
        self.two_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_3_button)
        self.end_one_3 = Label(text="%")
        gl2.add_widget(self.end_one_3)
        
        gl2.add_widget(Label(text="3" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.three_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.three_1)
        self.three_1_button = Button(text="-")
        self.three_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.three_1_button)
        gl2.add_widget(Label(text="end-2"))
        self.three_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.three_2)
        self.three_2_button = Button(text="-")
        self.three_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.three_2_button)
        gl2.add_widget(Label(text="end-2"))
        self.three_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.three_3)
        self.three_3_button = Button(text="-")
        self.three_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.three_3_button)
        gl2.add_widget(Label(text="end-2"))
        
        gl2.add_widget(Label(text="4" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.four_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.four_1)
        self.four_1_button = Button(text="-")
        self.four_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.four_1_button)
        self.end_two_1 = Label(text="%")
        gl2.add_widget(self.end_two_1)
        self.four_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.four_2)
        self.four_2_button = Button(text="-")
        self.four_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.four_2_button)
        self.end_two_2 = Label(text="%")
        gl2.add_widget(self.end_two_2)
        self.four_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.four_3)
        self.four_3_button = Button(text="-")
        self.four_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.four_3_button)
        self.end_two_3 = Label(text="%")
        gl2.add_widget(self.end_two_3)
        
        
        gl2.add_widget(Label(text="5" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.five_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.five_1)
        self.five_1_button = Button(text="-")
        self.five_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.five_1_button)
        gl2.add_widget(Label(text="end-3"))
        self.five_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.five_2)
        self.five_2_button = Button(text="-")
        self.five_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.five_2_button)
        gl2.add_widget(Label(text="end-3"))
        self.five_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.five_3)
        self.five_3_button = Button(text="-")
        self.five_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.five_3_button)
        gl2.add_widget(Label(text="end-3"))
        
        gl2.add_widget(Label(text="6" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.six_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.six_1)
        self.six_1_button = Button(text="-")
        self.six_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.six_1_button)
        self.end_three_1 = Label(text="%")
        gl2.add_widget(self.end_three_1)
        self.six_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.six_2)
        self.six_2_button = Button(text="-")
        self.six_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.six_2_button)
        self.end_three_2 = Label(text="%")
        gl2.add_widget(self.end_three_2)
        self.six_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.six_3)
        self.six_3_button = Button(text="-")
        self.six_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.six_3_button)
        self.end_three_3 = Label(text="%")
        gl2.add_widget(self.end_three_3)
        
        gl2.add_widget(Label(text="7" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.seven_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.seven_1)
        self.seven_1_button = Button(text="-")
        self.seven_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.seven_1_button)
        gl2.add_widget(Label(text="end-4"))
        self.seven_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.seven_2)
        self.seven_2_button = Button(text="-")
        self.seven_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.seven_2_button)
        gl2.add_widget(Label(text="end-4"))
        self.seven_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.seven_3)
        self.seven_3_button = Button(text="-")
        self.seven_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.seven_3_button)
        gl2.add_widget(Label(text="end-4"))
        
        gl2.add_widget(Label(text="8" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.eight_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.eight_1)
        self.eight_1_button = Button(text="-")
        self.eight_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.eight_1_button)
        self.end_four_1 = Label(text="%")
        gl2.add_widget(self.end_four_1)
        self.eight_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.eight_2)
        self.eight_2_button = Button(text="-")
        self.eight_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.eight_2_button)
        self.end_four_2 = Label(text="%")
        gl2.add_widget(self.end_four_2)
        self.eight_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.eight_3)
        self.eight_3_button = Button(text="-")
        self.eight_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.eight_3_button)
        self.end_four_3 = Label(text="%")
        gl2.add_widget(self.end_four_3)
        
        gl2.add_widget(Label(text="9" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.nine_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.nine_1)
        self.nine_1_button = Button(text="-")
        self.nine_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.nine_1_button)
        gl2.add_widget(Label(text="end-5"))
        self.nine_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.nine_2)
        self.nine_2_button = Button(text="-")
        self.nine_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.nine_2_button)
        gl2.add_widget(Label(text="end-5"))
        self.nine_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.nine_3)
        self.nine_3_button = Button(text="-")
        self.nine_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.nine_3_button)
        gl2.add_widget(Label(text="end-5"))
        
        gl2.add_widget(Label(text="10" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_zero_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_zero_1)
        self.one_zero_1_button = Button(text="-")
        self.one_zero_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_zero_1_button)
        self.end_five_1 = Label(text="%")
        gl2.add_widget(self.end_five_1)
        self.one_zero_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_zero_2)
        self.one_zero_2_button = Button(text="-")
        self.one_zero_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_zero_2_button)
        self.end_five_2 = Label(text="%")
        gl2.add_widget(self.end_five_2)
        self.one_zero_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_zero_3)
        self.one_zero_3_button = Button(text="-")
        self.one_zero_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_zero_3_button)
        self.end_five_3 = Label(text="%")
        gl2.add_widget(self.end_five_3)
        
        gl2.add_widget(Label(text="11" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_one_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_one_1)
        self.one_one_1_button = Button(text="-")
        self.one_one_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_one_1_button)
        gl2.add_widget(Label(text="end-6"))
        self.one_one_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_one_2)
        self.one_one_2_button = Button(text="-")
        self.one_one_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_one_2_button)
        gl2.add_widget(Label(text="end-6"))
        self.one_one_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_one_3)
        self.one_one_3_button = Button(text="-")
        self.one_one_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_one_3_button)
        gl2.add_widget(Label(text="end-6"))
        
        gl2.add_widget(Label(text="12" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_two_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_two_1)
        self.one_two_1_button = Button(text="-")
        self.one_two_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_two_1_button)
        self.end_six_1 = Label(text="%")
        gl2.add_widget(self.end_six_1)
        self.one_two_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_two_2)
        self.one_two_2_button = Button(text="-")
        self.one_two_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_two_2_button)
        self.end_six_2 = Label(text="%")
        gl2.add_widget(self.end_six_2)
        self.one_two_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_two_3)
        self.one_two_3_button = Button(text="-")
        self.one_two_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_two_3_button)
        self.end_six_3 = Label(text="%")
        gl2.add_widget(self.end_six_3)
        
        gl2.add_widget(Label(text="13" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_three_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_three_1)
        self.one_three_1_button = Button(text="-")
        self.one_three_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_three_1_button)
        gl2.add_widget(Label(text="end-7"))
        self.one_three_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_three_2)
        self.one_three_2_button = Button(text="-")
        self.one_three_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_three_2_button)
        gl2.add_widget(Label(text="end-7"))
        self.one_three_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_three_3)
        self.one_three_3_button = Button(text="-")
        self.one_three_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_three_3_button)
        gl2.add_widget(Label(text="end-7"))
        
        gl2.add_widget(Label(text="14" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_four_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_four_1)
        self.one_four_1_button = Button(text="-")
        self.one_four_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_four_1_button)
        self.end_seven_1 = Label(text="%")
        gl2.add_widget(self.end_seven_1)
        self.one_four_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_four_2)
        self.one_four_2_button = Button(text="-")
        self.one_four_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_four_2_button)
        self.end_seven_2 = Label(text="%")
        gl2.add_widget(self.end_seven_2)
        self.one_four_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_four_3)
        self.one_four_3_button = Button(text="-")
        self.one_four_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_four_3_button)
        self.end_seven_3 = Label(text="%")
        gl2.add_widget(self.end_seven_3)
        
        gl2.add_widget(Label(text="15" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_five_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_five_1)
        self.one_five_1_button = Button(text="-")
        self.one_five_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_five_1_button)
        gl2.add_widget(Label(text="end-8"))
        self.one_five_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_five_2)
        self.one_five_2_button = Button(text="-")
        self.one_five_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_five_2_button)
        gl2.add_widget(Label(text="end-8"))
        self.one_five_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_five_3)
        self.one_five_3_button = Button(text="-")
        self.one_five_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_five_3_button)
        gl2.add_widget(Label(text="end-8"))
        
        gl2.add_widget(Label(text="16" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_six_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_six_1)
        self.one_six_1_button = Button(text="-")
        self.one_six_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_six_1_button)
        self.end_eight_1 = Label(text="%")
        gl2.add_widget(self.end_eight_1)
        self.one_six_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_six_2)
        self.one_six_2_button = Button(text="-")
        self.one_six_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_six_2_button)
        self.end_eight_2 = Label(text="%")
        gl2.add_widget(self.end_eight_2)
        self.one_six_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_six_3)
        self.one_six_3_button = Button(text="-")
        self.one_six_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_six_3_button)
        self.end_eight_3 = Label(text="%")
        gl2.add_widget(self.end_eight_3)
        
        gl2.add_widget(Label(text="17" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_seven_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_seven_1)
        self.one_seven_1_button = Button(text="-")
        self.one_seven_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_seven_1_button)
        gl2.add_widget(Label(text="end-9"))
        self.one_seven_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_seven_2)
        self.one_seven_2_button = Button(text="-")
        self.one_seven_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_seven_2_button)
        gl2.add_widget(Label(text="end-9"))
        self.one_seven_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_seven_3)
        self.one_seven_3_button = Button(text="-")
        self.one_seven_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_seven_3_button)
        gl2.add_widget(Label(text="end-9"))
        
        gl2.add_widget(Label(text="18" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_eight_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_eight_1)
        self.one_eight_1_button = Button(text="-")
        self.one_eight_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_eight_1_button)
        self.end_nine_1 = Label(text="%")
        gl2.add_widget(self.end_nine_1)
        self.one_eight_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_eight_2)
        self.one_eight_2_button = Button(text="-")
        self.one_eight_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_eight_2_button)
        self.end_nine_2 = Label(text="%")
        gl2.add_widget(self.end_nine_2)
        self.one_eight_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_eight_3)
        self.one_eight_3_button = Button(text="-")
        self.one_eight_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_eight_3_button)
        self.end_nine_3 = Label(text="%")
        gl2.add_widget(self.end_nine_3)
        
        gl2.add_widget(Label(text="19" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.one_nine_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_nine_1)
        self.one_nine_1_button = Button(text="-")
        self.one_nine_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_nine_1_button)
        gl2.add_widget(Label(text="end-10"))
        self.one_nine_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_nine_2)
        self.one_nine_2_button = Button(text="-")
        self.one_nine_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_nine_2_button)
        gl2.add_widget(Label(text="end-10"))
        self.one_nine_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_nine_3)
        self.one_nine_3_button = Button(text="-")
        self.one_nine_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_nine_3_button)
        gl2.add_widget(Label(text="end-10"))
        
        gl2.add_widget(Label(text="20" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.two_zero_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_zero_1)
        self.two_zero_1_button = Button(text="-")
        self.two_zero_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_zero_1_button)
        self.end_ten_1 = Label(text="%")
        gl2.add_widget(self.end_ten_1)
        self.two_zero_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_zero_2)
        self.two_zero_2_button = Button(text="-")
        self.two_zero_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_zero_2_button)
        self.end_ten_2 = Label(text="%")
        gl2.add_widget(self.end_ten_2)
        self.two_zero_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_zero_3)
        self.two_zero_3_button = Button(text="-")
        self.two_zero_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_zero_3_button)
        self.end_ten_3 = Label(text="%")
        gl2.add_widget(self.end_ten_3)
        
        gl2.add_widget(Label(text="extra-1" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.extra_one_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_one_1)
        self.extra_one_1_button = Button(text="-")
        self.extra_one_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_one_1_button)
        gl2.add_widget(Label(text="extra_end-1"))
        self.extra_one_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_one_2)
        self.extra_one_2_button = Button(text="-")
        self.extra_one_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_one_2_button)
        gl2.add_widget(Label(text="extra_end-1"))
        self.extra_one_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_one_3)
        self.extra_one_3_button = Button(text="-")
        self.extra_one_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_one_3_button)
        gl2.add_widget(Label(text="extra_end-1"))
        
        gl2.add_widget(Label(text="extra-2" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.extra_two_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_two_1)
        self.extra_two_1_button = Button(text="-")
        self.extra_two_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_two_1_button)
        self.extra_end_one_1 = Label(text="%")
        gl2.add_widget(self.extra_end_one_1)
        self.extra_two_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_two_2)
        self.extra_two_2_button = Button(text="-")
        self.extra_two_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_two_2_button)
        self.extra_end_one_2 = Label(text="%")
        gl2.add_widget(self.extra_end_one_2)
        self.extra_two_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_two_3)
        self.extra_two_3_button = Button(text="-")
        self.extra_two_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_two_3_button)
        self.extra_end_one_3 = Label(text="%")
        gl2.add_widget(self.extra_end_one_3)
        
        gl2.add_widget(Label(text="extra-3" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.extra_three_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_three_1)
        self.extra_three_1_button = Button(text="-")
        self.extra_three_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_three_1_button)
        gl2.add_widget(Label(text="extra_end-2"))
        self.extra_three_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_three_2)
        self.extra_three_2_button = Button(text="-")
        self.extra_three_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_three_2_button)
        gl2.add_widget(Label(text="extra_end-2"))
        self.extra_three_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_three_3)
        self.extra_three_3_button = Button(text="-")
        self.extra_three_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_three_3_button)
        gl2.add_widget(Label(text="extra_end-2"))
        
        gl2.add_widget(Label(text="extra-4" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.extra_four_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_four_1)
        self.extra_four_1_button = Button(text="-")
        self.extra_four_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_four_1_button)
        self.extra_end_two_1 = Label(text="%")
        gl2.add_widget(self.extra_end_two_1)
        self.extra_four_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_four_2)
        self.extra_four_2_button = Button(text="-")
        self.extra_four_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_four_2_button)
        self.extra_end_two_2 = Label(text="%")
        gl2.add_widget(self.extra_end_two_2)
        self.extra_four_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_four_3)
        self.extra_four_3_button = Button(text="-")
        self.extra_four_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_four_3_button)
        self.extra_end_two_3 = Label(text="%")
        gl2.add_widget(self.extra_end_two_3)
        
        gl2.add_widget(Label(text="extra-5" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.extra_five_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_five_1)
        self.extra_five_1_button = Button(text="-")
        self.extra_five_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_five_1_button)
        gl2.add_widget(Label(text="extra_end-3"))
        self.extra_five_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_five_2)
        self.extra_five_2_button = Button(text="-")
        self.extra_five_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_five_2_button)
        gl2.add_widget(Label(text="extra_end-3"))
        self.extra_five_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_five_3)
        self.extra_five_3_button = Button(text="-")
        self.extra_five_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_five_3_button)
        gl2.add_widget(Label(text="extra_end-3"))
        
        gl2.add_widget(Label(text="extra-6" , color = "#02034e", size_hint=(None, 1) , size = (44 , 10) , font_size =18 ))
        self.extra_six_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_six_1)
        self.extra_six_1_button = Button(text="-")
        self.extra_six_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_six_1_button)
        self.extra_end_three_1 = Label(text="%")
        gl2.add_widget(self.extra_end_three_1)
        self.extra_six_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_six_2)
        self.extra_six_2_button = Button(text="-")
        self.extra_six_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_six_2_button)
        self.extra_end_three_2 = Label(text="%")
        gl2.add_widget(self.extra_end_three_2)
        self.extra_six_3 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_six_3)
        self.extra_six_3_button = Button(text="-")
        self.extra_six_3_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_six_3_button)
        self.extra_end_three_3 = Label(text="%")
        gl2.add_widget(self.extra_end_three_3)
        
        self.final_percentage_1 = Label(text="", pos=(-40, 80))
        self.types_throw_1 = Label(text="", pos=(-40, 20))
        self.final_percentage_2 = Label(text="", pos=(120, 80))
        self.types_throw_2 = Label(text="", pos=(120, 20))
        self.final_percentage_3 = Label(text="", pos=(280, 80))
        self.types_throw_3 = Label(text="", pos=(280, 20))
        
        self.save_info = Label(text="", pos=(120, -60))
        
        fl2.add_widget(self.final_percentage_1)
        fl2.add_widget(self.types_throw_1)
        fl2.add_widget(self.final_percentage_2)
        fl2.add_widget(self.types_throw_2)
        fl2.add_widget(self.final_percentage_3)
        fl2.add_widget(self.types_throw_3)
        
        fl2.add_widget(self.save_info)
        
        end = Button(text= "Рассчёт", pos=(0, 140))
        end.bind(on_release=self.math_operation)
        fl2.add_widget(end)
        
        save = Button(text= "Сохранить", pos=(0, 70))
        save.bind(on_release=self.save_match)
        fl2.add_widget(save)
        
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

    def math_operation(self, *args):
        
        self.name_list = [self.name_1, self.name_2, self.name_3]
        
        self.conn = sqlite3.connect(path_db())
        cursor = self.conn.cursor()
        
        flag = True
        end_count = 0
        sum_dro = 0
        sum_take = 0
        sum_guard = 0
        
        helper = 0
        
        self.persentages_stat = [[], [], []]
        
        self.listik = [[self.one_1.text, self.two_1.text, self.three_1.text, self.four_1.text, self.five_1.text, self.six_1.text, self.seven_1.text, self.eight_1.text, self.nine_1.text, self.one_zero_1.text,
                  self.one_one_1.text, self.one_two_1.text, self.one_three_1.text, self.one_four_1.text, self.one_five_1.text, self.one_six_1.text, self.one_seven_1.text, self.one_eight_1.text, self.one_nine_1.text,
                  self.two_zero_1.text, self.extra_one_1.text, self.extra_two_1.text, self.extra_three_1.text, self.extra_four_1.text, self.extra_five_1.text, self.extra_six_1.text], [self.one_2.text, self.two_2.text, self.three_2.text, self.four_2.text, self.five_2.text, self.six_2.text, self.seven_2.text, self.eight_2.text, self.nine_2.text, self.one_zero_2.text,
                  self.one_one_2.text, self.one_two_2.text, self.one_three_2.text, self.one_four_2.text, self.one_five_2.text, self.one_six_2.text, self.one_seven_2.text, self.one_eight_2.text, self.one_nine_2.text,
                  self.two_zero_2.text, self.extra_one_2.text, self.extra_two_2.text, self.extra_three_2.text, self.extra_four_2.text, self.extra_five_2.text, self.extra_six_2.text], [self.one_3.text, self.two_3.text, self.three_3.text, self.four_3.text, self.five_3.text, self.six_3.text, self.seven_3.text, self.eight_3.text, self.nine_3.text, self.one_zero_3.text,
                  self.one_one_3.text, self.one_two_3.text, self.one_three_3.text, self.one_four_3.text, self.one_five_3.text, self.one_six_3.text, self.one_seven_3.text, self.one_eight_3.text, self.one_nine_3.text,
                  self.two_zero_3.text, self.extra_one_3.text, self.extra_two_3.text, self.extra_three_3.text, self.extra_four_3.text, self.extra_five_3.text, self.extra_six_3.text]]
        
        type_listik = [[self.one_1_button.text, self.two_1_button.text, self.three_1_button.text, self.four_1_button.text, self.five_1_button.text, self.six_1_button.text, self.seven_1_button.text, self.eight_1_button.text, self.nine_1_button.text,
                       self.one_zero_1_button.text, self.one_one_1_button.text, self.one_two_1_button.text, self.one_three_1_button.text, self.one_four_1_button.text, self.one_five_1_button.text, self.one_six_1_button.text, self.one_seven_1_button.text,
                       self.one_eight_1_button.text, self.one_nine_1_button.text, self.two_zero_1_button.text, self.extra_one_1_button.text, self.extra_two_1_button.text, self.extra_three_1_button.text,
                       self.extra_four_1_button.text, self.extra_five_1_button.text, self.extra_six_1_button.text], [self.one_2_button.text, self.two_2_button.text, self.three_2_button.text, self.four_2_button.text, self.five_2_button.text, self.six_2_button.text, self.seven_2_button.text, self.eight_2_button.text, self.nine_2_button.text,
                       self.one_zero_2_button.text, self.one_one_2_button.text, self.one_two_2_button.text, self.one_three_2_button.text, self.one_four_2_button.text, self.one_five_2_button.text, self.one_six_2_button.text, self.one_seven_2_button.text,
                       self.one_eight_2_button.text, self.one_nine_2_button.text, self.two_zero_2_button.text, self.extra_one_2_button.text, self.extra_two_2_button.text, self.extra_three_2_button.text,
                       self.extra_four_2_button.text, self.extra_five_2_button.text, self.extra_six_2_button.text], [self.one_3_button.text, self.two_3_button.text, self.three_3_button.text, self.four_3_button.text, self.five_3_button.text, self.six_3_button.text, self.seven_3_button.text, self.eight_3_button.text, self.nine_3_button.text,
                       self.one_zero_3_button.text, self.one_one_3_button.text, self.one_two_3_button.text, self.one_three_3_button.text, self.one_four_3_button.text, self.one_five_3_button.text, self.one_six_3_button.text, self.one_seven_3_button.text,
                       self.one_eight_3_button.text, self.one_nine_3_button.text, self.two_zero_3_button.text, self.extra_one_3_button.text, self.extra_two_3_button.text, self.extra_three_3_button.text,
                       self.extra_four_3_button.text, self.extra_five_3_button.text, self.extra_six_3_button.text]]
        
        end_list = [[self.end_one_1, self.end_two_1, self.end_three_1, self.end_four_1, self.end_five_1, self.end_six_1, self.end_seven_1, self.end_eight_1, self.end_nine_1, self.end_ten_1, 
                    self.extra_end_one_1, self.extra_end_two_1, self.extra_end_three_1], [self.end_one_2, self.end_two_2, self.end_three_2, self.end_four_2, self.end_five_2, self.end_six_2, self.end_seven_2, self.end_eight_2, self.end_nine_2, self.end_ten_2, 
                    self.extra_end_one_2, self.extra_end_two_2, self.extra_end_three_2], [self.end_one_3, self.end_two_3, self.end_three_3, self.end_four_3, self.end_five_3, self.end_six_3, self.end_seven_3, self.end_eight_3, self.end_nine_3, self.end_ten_3, 
                    self.extra_end_one_3, self.extra_end_two_3, self.extra_end_three_3]]
        
        final_percentage_list = [self.final_percentage_1, self.final_percentage_2, self.final_percentage_3]
        
        types_throw_list = [self.types_throw_1, self.types_throw_2, self.types_throw_3]
        
        for i in range(len(self.listik)):
            name = self.name_list[i].text.lower()
            cursor.execute("""
                SELECT 1 FROM players WHERE first_and_second_name = ?
            """, (name,))
            
            result = cursor.fetchone()
            
            if result:
                for j in range(len(self.listik[i])):
                    if self.listik[i][j] == "":
                        helper = j
                        break
                    elif len(self.listik[i][j]) > 1:
                        flag = False
                        break
                    else:
                        self.listik[i][j] = int(self.listik[i][j])
                        continue
                else:
                    helper = len(self.listik[i])
                
                if len(self.listik[i]) - (self.listik[i].count("") + helper) == 0 and helper != 0 and flag == True:
                
                    if helper != len(self.listik[i]):
                        end_list[i] = end_list[i][:helper//2]
                    else:
                        end_list[i] = end_list[i][:helper-1//2]
                    self.listik[i] = self.listik[i][:helper]
                    type_listik[i] = type_listik[i][:helper]
            
                    for k in range(len(type_listik[i])):
                        end_count += self.listik[i][k]
                        if k % 2 == 1:
                            end_count = round(end_count / 8 * 100, 2)
                            self.persentages_stat[i].append(end_count)
                            end_list[i][(k-1)//2].text = f"{end_count}"
                            end_count = 0
                    
                        if type_listik[i][k] == "D":
                            sum_dro += self.listik[i][k]
                            continue
                        if type_listik[i][k] == "T":
                            sum_take += self.listik[i][k]
                            continue
                        if type_listik[i][k] == "G":
                            sum_guard += self.listik[i][k]
                            continue
            
                    helper = round(sum(self.listik[i]) / (helper*4) * 100, 2)
                    if sum_dro != 0:
                        sum_dro = round(sum_dro / (type_listik[i].count("D")*4) * 100,)
                        self.persentages_stat[i].append(sum_dro)
                    else:
                        self.persentages_stat[i].append(0.0)
                    if sum_take != 0:
                        sum_take = round(sum_take / (type_listik[i].count("T")*4) * 100, 2)
                        self.persentages_stat[i].append(sum_take)
                    else:
                        self.persentages_stat[i].append(0.0)
                    if sum_guard != 0:
                        sum_guard = round(sum_guard / (type_listik[i].count("G")*4) * 100, 2)
                        self.persentages_stat[i].append(sum_guard)
                    else:
                        self.persentages_stat[i].append(0.0)
            
                    final_percentage_list[i].text = f"Процент: {helper}"
                    types_throw_list[i].text = f"Dro: {sum_dro} \nTake: {sum_take} \nGuard: {sum_guard}"
                else:
                    final_percentage_list[i].text = f"Ошибка, {helper}"
                    types_throw_list[i].text = ""
                
                flag = True
                sum_dro = 0
                sum_take = 0
                sum_guard = 0
            
                helper = 0
            else:
                final_percentage_list[i].text = "Ошибка игрока"
                types_throw_list[i].text = ""
                
    def save_match(self, *args):
        if "Ошибка" in self.final_percentage_1.text or "Ошибка" in self.final_percentage_2.text or "Ошибка" in self.final_percentage_3.text or self.final_percentage_1 == "":
            self.save_info.text = "Ошибка сохранения"
        else:
            
            name_match = self.name_match.text
            date_game = self.date_match.text
            name_team = self.name_team.text
            
            cursor = self.conn.cursor()
            
            cursor.execute("""
                INSERT INTO matches (name_of_game, date_of_game, name_of_team) VALUES (?, ?, ?)
            """, (name_match, date_game, name_team))
            
            cursor.execute("""
                SELECT LAST_INSERT_ROWID()       
            """)
            
            match_id = cursor.lastrowid
            
            for i in range(3):
                name = self.name_list[i].text
                cursor.execute("""
                    SELECT player_id FROM players WHERE first_and_second_name = ?
                """, (name,))
                player_id = cursor.fetchone()
                
                cursor.execute("""
                    INSERT INTO match_players (match_id, player_id) VALUES (?, ?) 
                """, (match_id, player_id))                
            
            
            self.conn.commit()
            self.conn.close()
            self.save_info.text = f"Успешно сохранено \n {self.listik[0]} \n {self.listik[1]} \n {self.listik[2]}"
                
    def switch_match_plus(self, *args):
        self.manager.current = "Игра+"