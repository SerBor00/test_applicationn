from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from database import path_db, inp_filter
import sqlite3


class players2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bl = BoxLayout()
        gl = GridLayout(cols= 2)
        gl2 = GridLayout(cols=3, rows=39, spacing= 0, padding= 50, size_hint_y=None, height= 1000)
        bl2 = BoxLayout()
        main_bl = BoxLayout(size_hint=(1, None), height=1800)
        
        bl.add_widget(Label(text= "Название команды"))
        self.name_team = TextInput(multiline=False)
        bl.add_widget(self.name_team)
        
        bl.add_widget(Label(text= "Название игры"))
        self.name_match = TextInput(hint_text= "Первенство России среди кого и какого возраста", multiline=False)
        bl.add_widget(self.name_match)
        
        bl.add_widget(Label(text= "дата игры"))
        self.date_match = TextInput(hint_text= "дд.мм.гггг", multiline=False)
        bl.add_widget(self.date_match)
        
        gl.add_widget(Label(text= "Имя и Фамилия"))
        gl.add_widget(Label(text= "Имя и Фамилия"))
        self.name_1 = TextInput(hint_text= "Имя и Фамилия")
        gl.add_widget(self.name_1)
        self.name_2 = TextInput(hint_text= "Имя и Фамилия")
        gl.add_widget(self.name_2)
        
        gl2.add_widget(Label(text="1"))
        self.one_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_1)
        self.one_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_2)
        
        gl2.add_widget(Label(text="2"))
        self.two_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_1)
        self.two_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_2)
        
        gl2.add_widget(Label(text="3"))
        self.three_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.three_1)
        self.three_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.three_2)
        
        gl2.add_widget(Label(text="4"))
        self.four_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.four_1)
        self.four_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.four_2)
        
        gl2.add_widget(Label(text="5"))
        self.five_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.five_1)
        self.five_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.five_2)
        
        gl2.add_widget(Label(text="6"))
        self.six_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.six_1)
        self.six_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.six_2)
        
        gl2.add_widget(Label(text="7"))
        self.seven_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.seven_1)
        self.seven_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.seven_2)
        
        gl2.add_widget(Label(text="8"))
        self.eight_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.eight_1)
        self.eight_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.eight_2)
        
        gl2.add_widget(Label(text="9"))
        self.nine_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.nine_1)
        self.nine_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.nine_2)
        
        gl2.add_widget(Label(text="10"))
        self.one_zero_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_zero_1)
        self.one_zero_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_zero_2)
        
        gl2.add_widget(Label(text="11"))
        self.one_one_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_one_1)
        self.one_one_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_one_2)
        
        gl2.add_widget(Label(text="12"))
        self.one_two_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_two_1)
        self.one_two_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_two_2)
        
        gl2.add_widget(Label(text="13"))
        self.one_three_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_three_1)
        self.one_three_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_three_2)
        
        gl2.add_widget(Label(text="14"))
        self.one_four_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_four_1)
        self.one_four_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_four_2)
        
        gl2.add_widget(Label(text="15"))
        self.one_five_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_five_1)
        self.one_five_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_five_2)
        
        gl2.add_widget(Label(text="16"))
        self.one_six_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_six_1)
        self.one_six_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_six_2)
        
        gl2.add_widget(Label(text="17"))
        self.one_seven_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_seven_1)
        self.one_seven_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_seven_2)
        
        gl2.add_widget(Label(text="18"))
        self.one_eight_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_eight_1)
        self.one_eight_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_eight_2)
        
        gl2.add_widget(Label(text="19"))
        self.one_nine_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_nine_1)
        self.one_nine_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.one_nine_2)
        
        gl2.add_widget(Label(text="20"))
        self.two_zero_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_zero_1)
        self.two_zero_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_zero_2)
        
        gl2.add_widget(Label(text="21"))
        self.two_one_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_one_1)
        self.two_one_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_one_2)
        
        gl2.add_widget(Label(text="22"))
        self.two_two_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_two_1)
        self.two_two_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_two_2)
        
        gl2.add_widget(Label(text="23"))
        self.two_three_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_three_1)
        self.two_three_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_three_2)
        
        gl2.add_widget(Label(text="24"))
        self.two_four_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_four_1)
        self.two_four_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_four_2)
        
        gl2.add_widget(Label(text="25"))
        self.two_five_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_five_1)
        self.two_five_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_five_2)
        
        gl2.add_widget(Label(text="26"))
        self.two_six_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_six_1)
        self.two_six_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_six_2)
        
        gl2.add_widget(Label(text="27"))
        self.two_seven_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_seven_1)
        self.two_seven_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_seven_2)
        
        gl2.add_widget(Label(text="28"))
        self.two_eight_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_eight_1)
        self.two_eight_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_eight_2)
        
        gl2.add_widget(Label(text="29"))
        self.two_nine_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_nine_1)
        self.two_nine_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.two_nine_2)
        
        gl2.add_widget(Label(text="30"))
        self.three_zero_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.three_zero_1)
        self.three_zero_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.three_zero_2)
        
        gl2.add_widget(Label(text="extra-1"))
        self.extra_one_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_one_1)
        self.extra_one_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_one_2)
        
        gl2.add_widget(Label(text="extra-2"))
        self.extra_two_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_two_1)
        self.extra_two_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_two_2)
        
        gl2.add_widget(Label(text="extra-3"))
        self.extra_three_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_three_1)
        self.extra_three_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_three_2)
        
        gl2.add_widget(Label(text="extra-4"))
        self.extra_four_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_four_1)
        self.extra_four_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_four_2)
        
        gl2.add_widget(Label(text="extra-5"))
        self.extra_five_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_five_1)
        self.extra_five_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_five_2)
        
        gl2.add_widget(Label(text="extra-6"))
        self.extra_six_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_six_1)
        self.extra_six_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_six_2)
        
        gl2.add_widget(Label(text="extra-7"))
        self.extra_seven_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_seven_1)
        self.extra_seven_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_seven_2)
        
        gl2.add_widget(Label(text="extra-8"))
        self.extra_eight_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_eight_1)
        self.extra_eight_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_eight_2)
        
        gl2.add_widget(Label(text="extra-9"))
        self.extra_nine_1 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_nine_1)
        self.extra_nine_2 = TextInput(hint_text= "0/1/2", input_filter=inp_filter)
        gl2.add_widget(self.extra_nine_2)
        
        end = Button(text= "Рассчёт")
        end.bind(on_release=self.math_operation)
        bl2.add_widget(end)
        
        match_plus = Button(text= "Назад")
        match_plus.bind(on_release=self.switch_match_plus)
        bl2.add_widget(match_plus)
        
        main_bl.add_widget(bl)
        main_bl.add_widget(gl)
        main_bl.add_widget(gl2)
        main_bl.add_widget(bl2)
        
        scroll = ScrollView()
        scroll.add_widget(main_bl)
        
        self.add_widget(scroll)
    
    def switch_match_plus(self, *args):
        self.manager.current = "Игра+"

    def math_operation(self, *args):
        
        data = (self.name_team.text, self.name_match.text, self.date_match.text, self.name_1.txt, self.name_2.txt)
        
        conn = sqlite3.connected(path_db())
        cursor = conn.cursor()
        
        cursor.execute("""
                       INSERT INTO comands (
                           name_of_team, name_of_game, date_of_game, first_and_second_name_1, first_and_second_name_2, 
                           one_1, two_1,
                           three_1, four_1, five_1, six_1, seven_1, eight_1, nine_1, one_zero_1, one_one_1, one_two_1, one_three_1,
                           one_four_1, one_five_1, one_six_1, one_seven_1, one_eight_1, one_nine_1, two_zero_1, two_one_1, two_two_1,
                           two_three_1, two_four_1, two_five_1, two_six_1, two_seven_1, two_eight_1, two_nine_1, three_zero_1,
                           extra_one_1, extra_two_1, extra_three_1, extra_four_1, extra_five_1, extra_six_1, extra_seven_1,
                           extra_eight_1, extra_nine_1, 
                           one_2, two_2,
                           three_2, four_2, five_2, six_2, seven_2, eight_2, nine_2, one_zero_2, one_one_2, one_two_2, one_three_2,
                           one_four_2, one_five_2, one_six_2, one_seven_2, one_eight_2, one_nine_2, two_zero_2, two_one_2, two_two_2,
                           two_three_2, two_four_2, two_five_2, two_six_2, two_seven_2, two_eight_2, two_nine_2, three_zero_2,
                           extra_one_2, extra_two_2, extra_three_2, extra_four_2, extra_five_2, extra_six_2, extra_seven_2,
                           extra_eight_2, extra_nine_2
                       ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                       ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                       """, data)