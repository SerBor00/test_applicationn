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
        gl = GridLayout(cols= 3 , spacing=(1 , 1) , padding= (1 , 1 , 1 , 1))
        gl2 = GridLayout(cols=7, spacing=(0 , 5), rows=39, padding= (1 , 1 , 1 , 1 ), size_hint_y=None, height= 1550) #height=1200
        fl2 = BoxLayout(size_hint_y=None, height= 150, padding= (1 , 1 , 1 , 1 )) #height=200
        grid_bl =  BoxLayout(size_hint=(1, None), height=1600, padding= (1 , 1 , 1 , 800 ))
        main_bl = BoxLayout(size_hint=(1, None), height=2950) #height=1830
        grid_per = GridLayout(cols = 2 , height=100, padding= (1 , 1 , 1 , 1 ), spacing=(70 , 10))

        bl.add_widget(Label(text= "дата игры" , color = "#02034e", size_hint_y=None, height= 32 , font_size =24 , size_hint=(None, None) , size = (125 , 32)))
        self.date_match = TextInput(hint_text= "дд.мм.гггг", multiline=False, size_hint_y=None, height= 32, size_hint=(None, None) , size = (150 , 32))
        bl.add_widget(self.date_match)

        bl.add_widget(Label(text= "название команды" , color = "#02034e", size_hint_y=None, height= 32 , font_size =24 , size_hint=(None, None) , size = (230 , 32) ))
        self.name_team = TextInput(hint_text= "Приморкий край" , multiline=False, size_hint_y=None, height= 32, size_hint=(None, None) , size = (250 , 32))
        bl.add_widget(self.name_team) 

        bl.add_widget(Label(text= "название игры" , color = "#02034e", size_hint_y=None, height= 32 , font_size =24 , size_hint=(None, None) , size = (185 , 32)))
        self.name_match = TextInput(hint_text= "Первенство России среди кого и какого возраста", multiline=False, size_hint_y=None, height= 32, size_hint=(None, None) , size = (500 , 32))
        bl.add_widget(self.name_match)
        
        gl.add_widget(Label(text= "№" , color = "#02034e", size_hint_y=None, height= 32 , font_size =20, size_hint=(None, None) , size = (68 , 32) ))
        gl.add_widget(Label(text= "Имя Фамилия" , color = "#02034e", size_hint_y=None, height= 32 , font_size =22, size_hint=(None, None) , size = (162 , 32) ))
        gl.add_widget(Label(text= "Имя Фамилия" , color = "#02034e", size_hint_y=None, height= 32 , font_size =22, size_hint=(None, None) , size = (162 , 32) ))
        gl.add_widget(Label(text= "броска" , color = "#02034e", size_hint_y=None, height= 32 , font_size =20, size_hint=(None, None) , size = (68 , 48) ))
        self.name_1 = TextInput(hint_text= "Имя Фамилия", size_hint_y=None, height= 32, size_hint=(None, None) , size = (162 , 48))
        gl.add_widget(self.name_1)
        self.name_2 = TextInput(hint_text= "Имя Фамилия", size_hint_y=None, height= 32, size_hint=(None, None) , size = (162 , 48))
        gl.add_widget(self.name_2)
        
        gl2.add_widget(Label(text="1" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50) )
        gl2.add_widget(self.one_1)
        self.one_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50) )
        self.one_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_1_button)
        gl2.add_widget(Label(text= "end - 1" , color = "#02034e", size_hint=(None, None) , size = (75 , 50), font_size =18))
        self.one_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_2)
        self.one_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_2_button)
        gl2.add_widget(Label(text= "end - 1" , color = "#02034e", size_hint=(None, None) , size = (75 , 50) , font_size =18 ))
        
        gl2.add_widget(Label(text="2" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.two_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_1)
        self.two_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_1_button)
        self.end_first_1_1 = Label(text = "." ,  color = "#02034e", size_hint=(None, None) , size = (75 , 50) , font_size =18)
        gl2.add_widget(self.end_first_1_1)
        self.two_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_2)
        self.two_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_2_button)
        self.end_second_1_1 = Label(text = "." ,  color = "#02034e", size_hint=(None, None) , size = (75 , 50) , font_size =18)
        gl2.add_widget(self.end_second_1_1)
        
        gl2.add_widget(Label(text="3" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.three_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.three_1)
        self.three_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.three_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.three_1_button)
        self.end_first_1_2 = Label(text = "." ,  color = "#02034e", size_hint=(None, None) , size = (75 , 50) , font_size =18)
        gl2.add_widget(self.end_first_1_2)
        self.three_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.three_2)
        self.three_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.three_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.three_2_button)
        self.end_second_1_2 = Label(text = "." ,  color = "#02034e", size_hint=(None, None) , size = (75 , 50) , font_size =18)
        gl2.add_widget(self.end_second_1_2)
       
        
        gl2.add_widget(Label(text="4" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.four_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.four_1)
        self.four_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.four_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.four_1_button)
        gl2.add_widget(Label(text= "end - 2" , color = "#02034e", size_hint=(None, None) , size = (75 , 50) , font_size =18))
        self.four_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.four_2)
        self.four_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.four_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.four_2_button)
        gl2.add_widget(Label(text= "end - 2" , color = "#02034e", size_hint=(None, None) , size = (75 , 50) , font_size =18))
        
        gl2.add_widget(Label(text="5" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.five_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.five_1)
        self.five_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.five_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.five_1_button)
        self.end_first_2_1 = Label(text = "." ,  color = "#02034e", size_hint=(None, None) , size = (75 , 50) , font_size =18)
        gl2.add_widget(self.end_first_2_1)
        self.five_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.five_2)
        self.five_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.five_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.five_2_button)
        self.end_second_2_1 = Label(text = "." ,  color = "#02034e", size_hint=(None, None) , size = (75 , 50) , font_size =18)
        gl2.add_widget(self.end_second_2_1)
        
        gl2.add_widget(Label(text="6" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.six_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.six_1)
        self.six_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.six_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.six_1_button)
        self.end_first_2_2 = Label(text = "." ,  color = "#02034e", size_hint=(None, None) , size = (75 , 50) , font_size =18)
        gl2.add_widget(self.end_first_2_2)
        self.six_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.six_2)
        self.six_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.six_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.six_2_button)
        self.end_second_2_2 = Label(text = "." ,  color = "#02034e", size_hint=(None, None) , size = (75 , 50) , font_size =18)
        gl2.add_widget(self.end_second_2_2)
        
        gl2.add_widget(Label(text="7" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.seven_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.seven_1)
        self.seven_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.seven_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.seven_1_button)
        gl2.add_widget(Label(text= "end - 3" , color = "#02034e", size_hint=(None, None) , size = (75 , 50) , font_size =18))
        self.seven_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.seven_2)
        self.seven_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.seven_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.seven_2_button)
        gl2.add_widget(Label(text= "end - 3" , color = "#02034e", size_hint=(None, None) , size = (75 , 50) , font_size =18))
        
        gl2.add_widget(Label(text="8" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.eight_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.eight_1)
        self.eight_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.eight_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.eight_1_button)
        self.end_first_3_1 = Label(text = "." ,  color = "#02034e", size_hint=(None, None) , size = (75 , 50) , font_size =18)
        gl2.add_widget(self.end_first_3_1)
        self.eight_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.eight_2)
        self.eight_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.eight_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.eight_2_button)
        self.end_second_4 = Label(text = "." ,  color = "#02034e", size_hint=(None, None) , size = (75 , 50) , font_size =18)
        gl2.add_widget(self.end_second_4)
        
        gl2.add_widget(Label(text="9" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.nine_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.nine_1)
        self.nine_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.nine_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.nine_1_button)
        self.end_first_3_2 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_3_2)
        self.nine_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.nine_2)
        self.nine_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.nine_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.nine_2_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        
        gl2.add_widget(Label(text="10" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_zero_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_zero_1)
        self.one_zero_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_zero_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_zero_1_button)
        gl2.add_widget(Label(text= "end - 4" , color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50)))
        self.one_zero_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_zero_2)
        self.one_zero_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_zero_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_zero_2_button)
        gl2.add_widget(Label(text= "end - 4" , color = "#02034e", size_hint=(None, None) , size = (75 , 50) , font_size =18))
        
        gl2.add_widget(Label(text="11" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_one_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_one_1)
        self.one_one_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_one_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_one_1_button)
        self.end_first_4_1 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_4_1)
        self.one_one_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_one_2)
        self.one_one_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_one_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_one_2_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        
        gl2.add_widget(Label(text="12" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_two_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_two_1)
        self.one_two_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_two_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_two_1_button)
        self.end_first_4_2 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_4_2)
        self.one_two_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_two_2)
        self.one_two_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_two_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_two_2_button)
        self.end_second_6 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_6)
        
        gl2.add_widget(Label(text="13" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_three_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_three_1)
        self.one_three_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_three_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_three_1_button)
        gl2.add_widget(Label(text= "end - 5" , color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50)))
        self.one_three_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_three_2)
        self.one_three_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_three_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_three_2_button)
        gl2.add_widget(Label(text= "end - 5" , color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50)))
        
        gl2.add_widget(Label(text="14" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_four_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_four_1)
        self.one_four_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_four_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_four_1_button)
        self.end_first_5_1 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_5_1)
        self.one_four_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_four_2)
        self.one_four_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_four_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_four_2_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        
        gl2.add_widget(Label(text="15" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_five_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_five_1)
        self.one_five_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_five_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_five_1_button)
        self.end_first_5_2 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_5_2)
        self.one_five_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_five_2)
        self.one_five_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_five_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_five_2_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        
        gl2.add_widget(Label(text="16" , color = "#02034e", size_hint=(None, None) , size = (68, 50) , font_size =18 ))
        self.one_six_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_six_1)
        self.one_six_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_six_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_six_1_button)
        gl2.add_widget(Label(text= "end - 6" , color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50)))
        self.one_six_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_six_2)
        self.one_six_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_six_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_six_2_button)
        gl2.add_widget(Label(text= "end - 6" , color = "#02034e", size_hint=(None, None) , size = (75 , 50) , font_size =18))
        
        gl2.add_widget(Label(text="17" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_seven_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_seven_1)
        self.one_seven_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_seven_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_seven_1_button)
        self.end_first_6_1 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_6_1)
        self.one_seven_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_seven_2)
        self.one_seven_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_seven_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_seven_2_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        
        gl2.add_widget(Label(text="18" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_eight_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_eight_1)
        self.one_eight_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_eight_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_eight_1_button)
        self.end_first_6_2 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_6_2)
        self.one_eight_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_eight_2)
        self.one_eight_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_eight_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_eight_2_button)
        self.end_second_9 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_9)
        
        gl2.add_widget(Label(text="19" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_nine_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_nine_1)
        self.one_nine_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_nine_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_nine_1_button)
        gl2.add_widget(Label(text= "end - 7" , color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50)))
        self.one_nine_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.one_nine_2)
        self.one_nine_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.one_nine_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_nine_2_button)
        gl2.add_widget(Label(text= "end - 7" , color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50)))
        
        gl2.add_widget(Label(text="20" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.two_zero_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_zero_1)
        self.two_zero_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_zero_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_zero_1_button)
        self.end_first_7_1 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_7_1)
        self.two_zero_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_zero_2)
        self.two_zero_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_zero_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_zero_2_button)
        self.end_second_10 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_10)
        
        gl2.add_widget(Label(text="21" , color = "#02034e", size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.two_one_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_one_1)
        self.two_one_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_one_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_one_1_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        self.two_one_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_one_2)
        self.two_one_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_one_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_one_2_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        
        gl2.add_widget(Label(text="22" , color = "#02034e", size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.two_two_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_two_1)
        self.two_two_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_two_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_two_1_button)
        gl2.add_widget(Label(text= "end - 8" , color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50)))
        self.two_two_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_two_2)
        self.two_two_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_two_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_two_2_button)
        gl2.add_widget(Label(text= "end - 8" , color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50)))
        
        gl2.add_widget(Label(text="23" , color = "#02034e", size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.two_three_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_three_1)
        self.two_three_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_three_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_three_1_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        self.two_three_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_three_2)
        self.two_three_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_three_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_three_2_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        
        gl2.add_widget(Label(text="24" , color = "#02034e", size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.two_four_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_four_1)
        self.two_four_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_four_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_four_1_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        self.two_four_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_four_2)
        self.two_four_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_four_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_four_2_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        
        gl2.add_widget(Label(text="25" , color = "#02034e", size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.two_five_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_five_1)
        self.two_five_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_five_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_five_1_button)
        gl2.add_widget(Label(text= "end - 9" , color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50)))
        self.two_five_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_five_2)
        self.two_five_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_five_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_five_2_button)
        gl2.add_widget(Label(text= "end - 9" , color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50)))
        
        gl2.add_widget(Label(text="26" , color = "#02034e", size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.two_six_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_six_1)
        self.two_six_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_six_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_six_1_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        self.two_six_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_six_2)
        self.two_six_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_six_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_six_2_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        
        gl2.add_widget(Label(text="27" , color = "#02034e", size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.two_seven_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_seven_1)
        self.two_seven_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_seven_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_seven_1_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        self.two_seven_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_seven_2)
        self.two_seven_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_seven_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_seven_2_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        
        gl2.add_widget(Label(text="28" , color = "#02034e", size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.two_eight_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_eight_1)
        self.two_eight_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_eight_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_eight_1_button)
        gl2.add_widget(Label(text= "end - 10" , color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50)))
        self.two_eight_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_eight_2)
        self.two_eight_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_eight_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_eight_2_button)
        gl2.add_widget(Label(text= "end - 10" , color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50)))
        
        gl2.add_widget(Label(text="29" , color = "#02034e", size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.two_nine_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_nine_1)
        self.two_nine_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_nine_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_nine_1_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        self.two_nine_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.two_nine_2)
        self.two_nine_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.two_nine_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_nine_2_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        
        gl2.add_widget(Label(text="30" , color = "#02034e", size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.three_zero_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.three_zero_1)
        self.three_zero_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.three_zero_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.three_zero_1_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        self.three_zero_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.three_zero_2)
        self.three_zero_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.three_zero_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.three_zero_2_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        
        gl2.add_widget(Label(text="extra-1" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.extra_one_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.extra_one_1)
        self.extra_one_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.extra_one_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_one_1_button)
        gl2.add_widget(Label(text= "ex.end 1" , color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50)))
        self.extra_one_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.extra_one_2)
        self.extra_one_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.extra_one_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_one_2_button)
        gl2.add_widget(Label(text= "ex.end 1" , color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50)))
        
        gl2.add_widget(Label(text="extra-2" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.extra_two_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.extra_two_1)
        self.extra_two_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.extra_two_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_two_1_button)
        self.end_first_ex_1_1 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_ex_1_1)
        self.extra_two_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.extra_two_2)
        self.extra_two_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.extra_two_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_two_2_button)
        self.end_second_ex_1 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_ex_1)
        
        gl2.add_widget(Label(text="extra-3" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.extra_three_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.extra_three_1)
        self.extra_three_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.extra_three_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_three_1_button)
        self.end_first_ex_1_2 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_ex_1_2)
        self.extra_three_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.extra_three_2)
        self.extra_three_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.extra_three_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_three_2_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        
        gl2.add_widget(Label(text="extra-4" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.extra_four_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.extra_four_1)
        self.extra_four_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.extra_four_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_four_1_button)
        gl2.add_widget(Label(text= "ex.end 2" , color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50)))
        self.extra_four_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.extra_four_2)
        self.extra_four_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.extra_four_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_four_2_button)
        gl2.add_widget(Label(text= "ex.end 2" , color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50)))
        
        gl2.add_widget(Label(text="extra-5" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.extra_five_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.extra_five_1)
        self.extra_five_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.extra_five_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_five_1_button)
        self.end_first_ex_2_1 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_ex_2_1)
        self.extra_five_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.extra_five_2)
        self.extra_five_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.extra_five_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_five_2_button)
        self.end_second_7 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7)
        
        gl2.add_widget(Label(text="extra-6" , color = "#02034e", size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.extra_six_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.extra_six_1)
        self.extra_six_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.extra_six_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_six_1_button)
        self.end_first_ex_2_2 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_ex_2_2)
        self.extra_six_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.extra_six_2)
        self.extra_six_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.extra_six_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_six_2_button)
        self.end_second_ex_3 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_ex_3)
        
        gl2.add_widget(Label(text="extra-7" , color = "#02034e", size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.extra_seven_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.extra_seven_1)
        self.extra_seven_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.extra_seven_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_seven_1_button)
        gl2.add_widget(Label(text= "ex.end 3" , color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50)))
        self.extra_seven_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.extra_seven_2)
        self.extra_seven_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.extra_seven_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_seven_2_button)
        gl2.add_widget(Label(text= "ex.end 3" , color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50)))
        
        gl2.add_widget(Label(text="extra-8" , color = "#02034e", size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.extra_eight_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.extra_eight_1)
        self.extra_eight_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.extra_eight_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_eight_1_button)
        self.end_first_ex_3_1 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_ex_3_1)
        self.extra_eight_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.extra_eight_2)
        self.extra_eight_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.extra_eight_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_eight_2_button)
        self.end_second_ex_3_1 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_ex_3_1)
        
        gl2.add_widget(Label(text="extra-9" , color = "#02034e", size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.extra_nine_1 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.extra_nine_1)
        self.extra_nine_1_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.extra_nine_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_nine_1_button)
        self.end_first_ex_3_2 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_ex_3_2)
        self.extra_nine_2 = TextInput(hint_text= "от 0 до 4", input_filter=inp_filter, size_hint=(None, None) , size = (45 , 50))
        gl2.add_widget(self.extra_nine_2)
        self.extra_nine_2_button = Button(text="-", size_hint=(None, None) , size = (44 , 50))
        self.extra_nine_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_nine_2_button)
        self.end_second_ex_3_2 = Label(text = "." ,  color = "#02034e", font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_ex_3_2)
        
        self.final_percentage_1 = Label(text="" , color = "#02034e", size_hint_y=None, height= 32 , font_size =20, size_hint=(None, None) , size = (68 , 32) , padding = (210 , 1200 , 1 , 1) )
        self.final_percentage_2 = Label(text="" , color = "#02034e", size_hint_y=None, height= 32 , font_size =20, size_hint=(None, None) , size = (68 , 32) , padding = (260 , 1200 , 1 , 1) )
        self.types_throw_1 = Label(text="" , color = "#02034e", size_hint_y=None, height= 80 , font_size =20, size_hint=(None, None) , size = (68 , 32) , padding = (165 , 1300 , 1 , 1) )
        self.types_throw_2 = Label(text="" , color = "#02034e", size_hint_y=None, height= 64 , font_size =20, size_hint=(None, None) , size = (68 , 32) , padding = (205 , 1300 , 1 , 1) )
        
        grid_per.add_widget(self.final_percentage_1)
        grid_per.add_widget(self.final_percentage_2)
        grid_per.add_widget(self.types_throw_1)
        grid_per.add_widget(self.types_throw_2)
        

        end = Button(text= "Рассчёт", pos=(0, 75))
        end.bind(on_release=self.math_operation)
        fl2.add_widget(end)

        save = Button(text= "Сохранить", pos=(0, 70))
        save.bind(on_release=self.save_match)
        fl2.add_widget(save)

        match_plus = Button(text= "Назад")
        match_plus.bind(on_release=self.switch_match_plus)
        fl2.add_widget(match_plus)
        
        
        grid_bl.add_widget(gl2)

        main_bl.add_widget(bl)
        main_bl.add_widget(gl)
        main_bl.add_widget(grid_bl)
        grid_bl.add_widget(grid_per)
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
            
    def save_match(self, instance, *args):
        pass
            
    def switch_match_plus(self, *args):
        self.manager.current = "Игра+"