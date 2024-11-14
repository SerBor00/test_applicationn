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
        bl = BoxLayout(size_hint_y=None, height= 200) #height=300
        gl = GridLayout(cols= 3 , rows=2 , spacing=(1 , 1) , padding= (1 , 1 , 1 , 1), size_hint_y=None, height= 80)
        gl2 = GridLayout(cols=7, spacing=(0 , 5), rows=39, padding= (1 , 1 , 1 , 1 ), size_hint_y=None, height= 1550) #height=1200
        fl2 = BoxLayout(size_hint_y=None, height= 150, padding= (1 , 1 , 1 , 1 )) #height=200
        grid_bl =  BoxLayout(size_hint=(1, None), height=1600, padding= (1 , 1 , 1 , 500 ))
        main_bl = BoxLayout(size_hint=(1, None), height=2800) #height=1830
        grid_per = GridLayout(cols = 3 , height=100, padding= (1 , 230 , 1 , 1 ), spacing=(0 , 10))
        grid_post = GridLayout(cols= 3 , rows = 3, spacing=(7 , 4) , padding= (5 , 1 , 1 , 1), size_hint_y=None, height= 130 )
        head =  BoxLayout(size_hint=(1, None), height=460, padding= (0 , 1 , 1 , 460 ), spacing= 20 )

        bl.add_widget(Label(text= "дата игры"  , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32 , font_size =24 , size_hint=(None, None) , size = (125 , 28)))
        self.date_match = TextInput(hint_text= "дд.мм.гггг",foreground_color = ('#02034e'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e") , border = (0.1 , 0.1 , 0.1 , 0.1)  ,hint_text_color = "#6188a3", font_name = 'application/shrift/TT Norms Pro Medium.otf', multiline=False, size_hint_y=None, height= 32, size_hint=(None, None) , size = (150 , 32))
        bl.add_widget(self.date_match)

        bl.add_widget(Label(text= "название команды" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32 , font_size =24 , size_hint=(None, None) , size = (230 , 28) ))
        self.name_team = TextInput(hint_text= "Приморкий край" ,foreground_color = ('#02034e'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e") , border = (0.1 , 0.1 , 0.1 , 0.1) ,hint_text_color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', multiline=False, size_hint_y=None, height= 32, size_hint=(None, None) , size = (250 , 32))
        bl.add_widget(self.name_team) 

        bl.add_widget(Label(text= "название игры"  , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32 , font_size =24 , size_hint=(None, None) , size = (185 , 28)))
        self.name_match = TextInput(hint_text= "Первенство России среди кого и какого возраста", foreground_color = ('#02034e') ,  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e") , border = (0.1 , 0.1 , 0.1 , 0.1) ,hint_text_color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', multiline=False, size_hint_y=None, height= 32, size_hint=(None, None) , size = (500 , 48))
        bl.add_widget(self.name_match)

        grid_post.add_widget(Label(text= "имя фамилия" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32 , font_size =24, size_hint=(None, None) , size = (162 , 28) ))
        grid_post.add_widget(Label(text= "имя фамилия" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32 , font_size =24, size_hint=(None, None) , size = (162 , 28) ))
        grid_post.add_widget(Label(text= "" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32 , font_size =20, size_hint=(None, None) , size = (230 , 28) ))
        self.first_post_name = TextInput(hint_text= "Имя Фамилия",foreground_color = ('#02034e') ,  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e") , border = (0.1 , 0.1 , 0.1 , 0.1) ,hint_text_color = "#6188a3"  , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32, size_hint=(None, None) , size = (162 , 48))
        grid_post.add_widget(self.first_post_name)
        self.second_post_name = TextInput(hint_text= "Имя Фамилия",foreground_color = ('#02034e') ,  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e") , border = (0.1 , 0.1 , 0.1 , 0.1) ,hint_text_color = "#6188a3"  , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32, size_hint=(None, None) , size = (162 , 48))
        grid_post.add_widget(self.second_post_name)
        grid_post.add_widget(Label(text= "" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32 , font_size =20, size_hint=(None, None) , size = (230 , 48) ))
        self.first_post = TextInput(hint_text= "199.6" ,foreground_color = ('#02034e') ,  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e") , border = (0.1 , 0.1 , 0.1 , 0.1) ,hint_text_color = "#6188a3"  , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32,  size_hint=(None, None) , size = (162 , 32))
        grid_post.add_widget(self.first_post)
        self.second_post = TextInput(hint_text= "199.6",foreground_color = ('#02034e') ,  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e") , border = (0.1 , 0.1 , 0.1 , 0.1) ,hint_text_color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32, size_hint=(None, None) , size = (162 , 32))
        grid_post.add_widget(self.second_post)
        grid_post.add_widget(Label(text= "результаты постановок" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32 , font_size =20, size_hint=(None, None) , size = (230 , 32) ))
        
        gl.add_widget(Label(text= "№" , color = "#02034e", font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32 , font_size =20, size_hint=(None, None) , size = (68 , 32) ))
        gl.add_widget(Label(text= "имя фамилия", color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32 , font_size =22, size_hint=(None, None) , size = (162 , 32) ))
        gl.add_widget(Label(text= "имя фамилия" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32 , font_size =22, size_hint=(None, None) , size = (162 , 32) ))
        gl.add_widget(Label(text= "броска" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32 , font_size =20, size_hint=(None, None) , size = (68 , 48) ))
        self.name_1 = TextInput(hint_text= "Имя Фамилия",foreground_color = ('#02034e') , hint_text_color = "#6188a3"  ,  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e") , border = (0.1 , 0.1 , 0.1 , 0.1)  , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32, size_hint=(None, None) , size = (162 , 48))
        gl.add_widget(self.name_1)
        self.name_2 = TextInput(hint_text= "Имя Фамилия",foreground_color = ('#02034e') ,  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e") , border = (0.1 , 0.1 , 0.1 , 0.1) , hint_text_color = "#6188a3"   , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32, size_hint=(None, None) , size = (162 , 48))
        gl.add_widget(self.name_2)
        
        gl2.add_widget(Label(text="1" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0 , 10 )  , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50) )
        gl2.add_widget(self.one_1)
        self.one_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50) )
        self.one_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_1_button)
        gl2.add_widget(Label(text= "end - 1" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50), font_size =18))
        self.one_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_2)
        self.one_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_2_button)
        gl2.add_widget(Label(text= "end - 1" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18 ))
        
        gl2.add_widget(Label(text="2" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.two_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.two_1)
        self.two_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.two_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_1_button)
        self.end_first_1_1 = Label(text = "",color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18)
        gl2.add_widget(self.end_first_1_1)
        self.two_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.two_2)
        self.two_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.two_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_2_button)
        self.end_second_1_1 = Label(text = "",color = "#6188a3"  , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18)
        gl2.add_widget(self.end_second_1_1)
        
        gl2.add_widget(Label(text="3" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.three_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.three_1)
        self.three_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.three_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.three_1_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        self.three_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.three_2)
        self.three_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.three_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.three_2_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
       
        
        gl2.add_widget(Label(text="4" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.four_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.four_1)
        self.four_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.four_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.four_1_button)
        gl2.add_widget(Label(text= "end - 2" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        self.four_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.four_2)
        self.four_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.four_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.four_2_button)
        gl2.add_widget(Label(text= "end - 2" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        
        gl2.add_widget(Label(text="5" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.five_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.five_1)
        self.five_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.five_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.five_1_button)
        self.end_first_2_1 = Label(text = "",color = "#6188a3"  , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18)
        gl2.add_widget(self.end_first_2_1)
        self.five_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.five_2)
        self.five_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.five_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.five_2_button)
        self.end_second_2_1 = Label(text = "",color = "#6188a3"  , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18)
        gl2.add_widget(self.end_second_2_1)
        
        gl2.add_widget(Label(text="6" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.six_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.six_1)
        self.six_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.six_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.six_1_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        self.six_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.six_2)
        self.six_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.six_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.six_2_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        
        gl2.add_widget(Label(text="7" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.seven_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.seven_1)
        self.seven_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.seven_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.seven_1_button)
        gl2.add_widget(Label(text= "end - 3" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        self.seven_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.seven_2)
        self.seven_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.seven_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.seven_2_button)
        gl2.add_widget(Label(text= "end - 3" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        
        gl2.add_widget(Label(text="8" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.eight_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.eight_1)
        self.eight_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.eight_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.eight_1_button)
        self.end_first_3_1 = Label(text = "",color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18)
        gl2.add_widget(self.end_first_3_1)
        self.eight_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.eight_2)
        self.eight_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.eight_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.eight_2_button)
        self.end_second_3_1 = Label(text = "",color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18)
        gl2.add_widget(self.end_second_3_1)
        
        gl2.add_widget(Label(text="9" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.nine_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.nine_1)
        self.nine_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.nine_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.nine_1_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        self.nine_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.nine_2)
        self.nine_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.nine_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.nine_2_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        
        gl2.add_widget(Label(text="10" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_zero_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_zero_1)
        self.one_zero_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_zero_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_zero_1_button)
        gl2.add_widget(Label(text= "end - 4" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50)))
        self.one_zero_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_zero_2)
        self.one_zero_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_zero_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_zero_2_button)
        gl2.add_widget(Label(text= "end - 4" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        
        gl2.add_widget(Label(text="11" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_one_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_one_1)
        self.one_one_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_one_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_one_1_button)
        self.end_first_4_1 = Label(text = "",color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_4_1)
        self.one_one_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_one_2)
        self.one_one_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_one_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_one_2_button)
        self.end_second_4_1 = Label(text = "",color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_4_1)
        
        gl2.add_widget(Label(text="12" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_two_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_two_1)
        self.one_two_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_two_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_two_1_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        self.one_two_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_two_2)
        self.one_two_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_two_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_two_2_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        
        gl2.add_widget(Label(text="13" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_three_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_three_1)
        self.one_three_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_three_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_three_1_button)
        gl2.add_widget(Label(text= "end - 5" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50)))
        self.one_three_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_three_2)
        self.one_three_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_three_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_three_2_button)
        gl2.add_widget(Label(text= "end - 5" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50)))
        
        gl2.add_widget(Label(text="14" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_four_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_four_1)
        self.one_four_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_four_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_four_1_button)
        self.end_first_5_1 = Label(text = "",color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_5_1)
        self.one_four_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_four_2)
        self.one_four_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_four_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_four_2_button)
        self.end_second_5_1 = Label(text = "",color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_5_1)
        
        gl2.add_widget(Label(text="15" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_five_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_five_1)
        self.one_five_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_five_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_five_1_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        self.one_five_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_five_2)
        self.one_five_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_five_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_five_2_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        
        gl2.add_widget(Label(text="16" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68, 50) , font_size =18 ))
        self.one_six_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_six_1)
        self.one_six_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_six_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_six_1_button)
        gl2.add_widget(Label(text= "end - 6" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50)))
        self.one_six_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_six_2)
        self.one_six_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_six_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_six_2_button)
        gl2.add_widget(Label(text= "end - 6" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        
        gl2.add_widget(Label(text="17" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_seven_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_seven_1)
        self.one_seven_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_seven_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_seven_1_button)
        self.end_first_6_1 = Label(text = "",color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_6_1)
        self.one_seven_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_seven_2)
        self.one_seven_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_seven_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_seven_2_button)
        self.end_second_6_1 = Label(text = "",color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_6_1)
        
        gl2.add_widget(Label(text="18" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_eight_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_eight_1)
        self.one_eight_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_eight_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_eight_1_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        self.one_eight_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_eight_2)
        self.one_eight_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_eight_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_eight_2_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        
        gl2.add_widget(Label(text="19" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.one_nine_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_nine_1)
        self.one_nine_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_nine_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_nine_1_button)
        gl2.add_widget(Label(text= "end - 7" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50)))
        self.one_nine_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.one_nine_2)
        self.one_nine_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.one_nine_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.one_nine_2_button)
        gl2.add_widget(Label(text= "end - 7" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50)))
        
        gl2.add_widget(Label(text="20" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.two_zero_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.two_zero_1)
        self.two_zero_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.two_zero_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_zero_1_button)
        self.end_first_7_1 = Label(text = "",color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_7_1)
        self.two_zero_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.two_zero_2)
        self.two_zero_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.two_zero_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_zero_2_button)
        self.end_second_7_1 = Label(text = "",color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_7_1)
        
        gl2.add_widget(Label(text="21" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.two_one_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.two_one_1)
        self.two_one_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.two_one_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_one_1_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        self.two_one_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.two_one_2)
        self.two_one_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.two_one_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_one_2_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        
        gl2.add_widget(Label(text="22" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.two_two_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.two_two_1)
        self.two_two_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.two_two_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_two_1_button)
        gl2.add_widget(Label(text= "end - 8" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50)))
        self.two_two_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.two_two_2)
        self.two_two_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.two_two_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_two_2_button)
        gl2.add_widget(Label(text= "end - 8" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50)))
        
        gl2.add_widget(Label(text="23" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.two_three_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.two_three_1)
        self.two_three_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.two_three_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_three_1_button)
        self.end_first_8_1 = Label(text = "",color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_8_1)
        self.two_three_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.two_three_2)
        self.two_three_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.two_three_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_three_2_button)
        self.end_second_8_1 = Label(text = "",color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_8_1)
        
        gl2.add_widget(Label(text="24" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.two_four_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.two_four_1)
        self.two_four_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.two_four_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_four_1_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        self.two_four_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.two_four_2)
        self.two_four_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.two_four_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.two_four_2_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        
        gl2.add_widget(Label(text="extra-1" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.extra_one_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.extra_one_1)
        self.extra_one_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.extra_one_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_one_1_button)
        gl2.add_widget(Label(text= "ex.end 1" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50)))
        self.extra_one_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.extra_one_2)
        self.extra_one_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.extra_one_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_one_2_button)
        gl2.add_widget(Label(text= "ex.end 1" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50)))
        
        gl2.add_widget(Label(text="extra-2" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.extra_two_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.extra_two_1)
        self.extra_two_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.extra_two_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_two_1_button)
        self.end_first_ex_1_1 = Label(text = "",color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_ex_1_1)
        self.extra_two_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.extra_two_2)
        self.extra_two_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.extra_two_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_two_2_button)
        self.end_second_ex_1_1 = Label(text = "",color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_ex_1_1)
        
        gl2.add_widget(Label(text="extra-3" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.extra_three_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.extra_three_1)
        self.extra_three_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.extra_three_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_three_1_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        self.extra_three_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.extra_three_2)
        self.extra_three_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.extra_three_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_three_2_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        
        gl2.add_widget(Label(text="extra-4" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.extra_four_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.extra_four_1)
        self.extra_four_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.extra_four_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_four_1_button)
        gl2.add_widget(Label(text= "ex.end 2" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50)))
        self.extra_four_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.extra_four_2)
        self.extra_four_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.extra_four_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_four_2_button)
        gl2.add_widget(Label(text= "ex.end 2" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50)))
        
        gl2.add_widget(Label(text="extra-5" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.extra_five_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.extra_five_1)
        self.extra_five_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.extra_five_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_five_1_button)
        self.end_first_ex_2_1 = Label(text = "",color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_ex_2_1)
        self.extra_five_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.extra_five_2)
        self.extra_five_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.extra_five_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_five_2_button)
        self.end_second_ex_2_1 = Label(text = "",color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_ex_2_1)
        
        gl2.add_widget(Label(text="extra-6" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (68 , 50) , font_size =18 ))
        self.extra_six_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.extra_six_1)
        self.extra_six_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.extra_six_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_six_1_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        self.extra_six_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.extra_six_2)
        self.extra_six_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.extra_six_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_six_2_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        
        gl2.add_widget(Label(text="extra-7" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.extra_seven_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.extra_seven_1)
        self.extra_seven_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.extra_seven_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_seven_1_button)
        gl2.add_widget(Label(text= "ex.end 3" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50)))
        self.extra_seven_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.extra_seven_2)
        self.extra_seven_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.extra_seven_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_seven_2_button)
        gl2.add_widget(Label(text= "ex.end 3" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50)))
        
        gl2.add_widget(Label(text="extra-8" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.extra_eight_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.extra_eight_1)
        self.extra_eight_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.extra_eight_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_eight_1_button)
        self.end_first_ex_3_1 = Label(text = "",color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_first_ex_3_1)
        self.extra_eight_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.extra_eight_2)
        self.extra_eight_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.extra_eight_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_eight_2_button)
        self.end_second_ex_3_1 = Label(text = "",color = "#6188a3" , font_name = 'application/shrift/TT Norms Pro Medium.otf', font_size =18, size_hint=(None, None) , size = (75 , 50))
        gl2.add_widget(self.end_second_ex_3_1)
        
        gl2.add_widget(Label(text="extra-9" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, 1) , size = (68 , 10) , font_size =18 ))
        self.extra_nine_1 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.extra_nine_1)
        self.extra_nine_1_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.extra_nine_1_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_nine_1_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        self.extra_nine_2 = TextInput(hint_text="0 - 4" ,foreground_color = ('#fefeff'),  padding_y = (4 , 0) , halign = ('center') , cursor_color = ("#02034e")  , hint_text_color = "#6188a3" , background_color = ("#02034e"), padding= (0, 10 ) , font_name = 'application/shrift/TT Norms Pro Medium.otf', input_filter=inp_filter, size_hint=(None, None) , size = (55 , 50))
        gl2.add_widget(self.extra_nine_2)
        self.extra_nine_2_button = Button(text="-" ,color = "#fefeff" , background_color = ("#02034e"), font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (35 , 50))
        self.extra_nine_2_button.bind(on_release=self.switch_button_type)
        gl2.add_widget(self.extra_nine_2_button)
        gl2.add_widget(Label(text = "----------" ,  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (75 , 50) , font_size =18))
        
        self.anal__1 = Label(text="",  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32 , font_size =20, size_hint=(None, None) , size = (58 , 68))
        grid_per.add_widget(self.anal__1)
        self.final_percentage_1 = Label(text="",  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32 , font_size =20, size_hint=(None, None) , size = (165 , 68) , halign = 'center' , valign = 'center')
        grid_per.add_widget(self.final_percentage_1)
        self.final_percentage_2 = Label(text="",  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32 , font_size =20, size_hint=(None, None) , size = (165 , 68) , halign = 'center' , valign = 'center')
        grid_per.add_widget(self.final_percentage_2)
        self.anal__2 = Label(text="",  color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32 , font_size =20, size_hint=(None, None) , size = (58 , 68))
        grid_per.add_widget(self.anal__2)
        self.types_throw_1 = Label(text="" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 80 , font_size =20, size_hint=(None, None) , size = (165 , 68) , halign = 'center' , valign = 'center')
        grid_per.add_widget(self.types_throw_1)
        self.types_throw_2 = Label(text="" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 64 , font_size =20, size_hint=(None, None) , size = (165 , 68) , halign = 'center' , valign = 'center')
        grid_per.add_widget(self.types_throw_2)
        
        self.save_info = Label(text="" , color = "#02034e" , font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint_y=None, height= 32 , font_size =20, size_hint=(None, None) , size = (68 , 32) , padding = (210 , 540 , 1 , 1) )
        fl2.add_widget(self.save_info)

        end = Button(text= "Рассчёт", font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (270 , 60))
        end.bind(on_release=self.math_operation)
        fl2.add_widget(end)

        save = Button(text= "Сохранить", font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (270 , 60))
        save.bind(on_release=self.save_match)
        fl2.add_widget(save)

        match_plus = Button(text= "Назад", font_name = 'application/shrift/TT Norms Pro Medium.otf', size_hint=(None, None) , size = (270 , 60))
        match_plus.bind(on_release=self.switch_match_plus)
        fl2.add_widget(match_plus)
        
        
        main_bl.add_widget(head)
        head.add_widget(bl)
        head.add_widget(grid_post)
        head.add_widget(gl)

        main_bl.add_widget(grid_bl)
        grid_bl.add_widget(gl2)
        grid_bl.add_widget(grid_per)
        main_bl.add_widget(fl2)
        
        scroll = ScrollView()
        scroll.add_widget(main_bl)
        
        self.add_widget(scroll)
        
        self.flag_page=True
    
    def switch_button_type(self, instance):
        new_type_throw = "-DTG"
        type_throw = new_type_throw.find(instance.text)
        type_throw =(type_throw +1) % len(new_type_throw)
        instance.text = new_type_throw[type_throw]
        return instance.text

    def math_operation(self, *args):
        
        self.flag_page=False
                
        self.check_info = [[], []]
        self.check_numbers = [[], []]
        self.check_persentages_numbers = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
        
        self.name_list = [self.name_1, self.name_2]
        
        self.conn = sqlite3.connect(path_db())
        cursor = self.conn.cursor()
        
        flag = True
        end_count = list()
        sum_dro = 0
        sum_take = 0
        sum_guard = 0
        count_dro = 0
        count_take = 0
        count_guard = 0
        
        helper = 0
        
        self.persentages_stat = [[], []]
        
        self.listik = [[self.one_1.text, self.two_1.text, self.three_1.text, self.four_1.text, self.five_1.text, self.six_1.text, self.seven_1.text, self.eight_1.text, self.nine_1.text, self.one_zero_1.text,
                  self.one_one_1.text, self.one_two_1.text, self.one_three_1.text, self.one_four_1.text, self.one_five_1.text, self.one_six_1.text, self.one_seven_1.text, self.one_eight_1.text, self.one_nine_1.text,
                  self.two_zero_1.text, self.two_one_1.text, self.two_two_1.text, self.two_three_1.text, self.two_four_1.text, self.extra_one_1.text, self.extra_two_1.text, self.extra_three_1.text, self.extra_four_1.text, self.extra_five_1.text, self.extra_six_1.text, self.extra_seven_1.text, self.extra_eight_1.text, self.extra_nine_1.text],
                       [self.one_2.text, self.two_2.text, self.three_2.text, self.four_2.text, self.five_2.text, self.six_2.text, self.seven_2.text, self.eight_2.text, self.nine_2.text, self.one_zero_2.text,
                  self.one_one_2.text, self.one_two_2.text, self.one_three_2.text, self.one_four_2.text, self.one_five_2.text, self.one_six_2.text, self.one_seven_2.text, self.one_eight_2.text, self.one_nine_2.text,
                  self.two_zero_2.text, self.two_one_2.text, self.two_two_2.text, self.two_three_2.text, self.two_four_2.text, self.extra_one_2.text, self.extra_two_2.text, self.extra_three_2.text, self.extra_four_2.text, self.extra_five_2.text, self.extra_six_2.text, self.extra_seven_2.text, self.extra_eight_2.text, self.extra_nine_2.text]]
        
        self.type_listik = [[self.one_1_button.text, self.two_1_button.text, self.three_1_button.text, self.four_1_button.text, self.five_1_button.text, self.six_1_button.text, self.seven_1_button.text, self.eight_1_button.text, self.nine_1_button.text,
                       self.one_zero_1_button.text, self.one_one_1_button.text, self.one_two_1_button.text, self.one_three_1_button.text, self.one_four_1_button.text, self.one_five_1_button.text, self.one_six_1_button.text, self.one_seven_1_button.text,
                       self.one_eight_1_button.text, self.one_nine_1_button.text, self.two_zero_1_button.text, self.two_one_1_button.text, self.two_two_1_button.text, self.two_three_1_button.text, self.two_four_1_button.text, self.extra_one_1_button.text, self.extra_two_1_button.text, self.extra_three_1_button.text, self.extra_four_1_button.text, self.extra_five_1_button.text, self.extra_six_1_button.text, self.extra_seven_1_button.text, self.extra_eight_1_button.text, self.extra_nine_1_button.text], 
                            [self.one_2_button.text, self.two_2_button.text, self.three_2_button.text, self.four_2_button.text, self.five_2_button.text, self.six_2_button.text, self.seven_2_button.text, self.eight_2_button.text, self.nine_2_button.text,
                       self.one_zero_2_button.text, self.one_one_2_button.text, self.one_two_2_button.text, self.one_three_2_button.text, self.one_four_2_button.text, self.one_five_2_button.text, self.one_six_2_button.text, self.one_seven_2_button.text,
                       self.one_eight_2_button.text, self.one_nine_2_button.text, self.two_zero_2_button.text, self.two_one_2_button.text, self.two_two_2_button.text, self.two_three_2_button.text, self.two_four_2_button.text, self.extra_one_2_button.text, self.extra_two_2_button.text, self.extra_three_2_button.text, self.extra_four_2_button.text, self.extra_five_2_button.text, self.extra_six_2_button.text, self.extra_seven_2_button.text, self.extra_eight_2_button.text, self.extra_nine_2_button.text]]
        
        self.end_list = [[self.end_first_1_1, self.end_first_2_1, self.end_first_3_1, self.end_first_4_1, self.end_first_5_1, self.end_first_6_1, self.end_first_7_1, self.end_first_8_1, self.end_first_ex_1_1, self.end_first_ex_2_1, self.end_first_ex_3_1],
                        [self.end_second_1_1, self.end_second_2_1, self.end_second_3_1, self.end_second_4_1, self.end_second_5_1, self.end_second_6_1, self.end_second_7_1, self.end_second_8_1, self.end_second_ex_1_1, self.end_second_ex_2_1, self.end_second_ex_3_1]]
        
        self.final_percentage_list = [self.final_percentage_1, self.final_percentage_2]
        self.types_throw_list = [self.types_throw_1, self.types_throw_2]
        
        for i in range(len(self.listik)):
            
            name = self.name_list[i].text.title()
            cursor.execute("""
                SELECT 1 FROM players WHERE first_and_second_name = ?
            """, (name,))
            
            result = cursor.fetchone()
            if result:
                for j in range(len(self.listik[i])):
                    if self.listik[i][j] == "":
                        self.check_info[i].append(j)
                        continue
                    elif len(self.listik[i][j]) > 1:
                        flag = False
                        break
                    else:
                        self.listik[i][j] = int(self.listik[i][j])
                        self.check_numbers[i].append(self.listik[i][j])
                else:
                    helper = 1
                    
                if helper != 0 and flag == True and len(self.check_info[i]) != len(self.listik[i]):
                    helper = 0
                    for k in range(len(self.listik[i])):
                        if k not in self.check_info[i]:
                            helper += self.listik[i][k]
                            end_count.append(self.listik[i][k])
                            if self.type_listik[i][k] == "D":
                                sum_dro += self.listik[i][k]
                                count_dro += 1
                            else:
                                if self.type_listik[i][k] == "T":
                                    sum_take += self.listik[i][k]
                                    count_take += 1
                                else:
                                    if self.type_listik[i][k] == "G":
                                        sum_guard += self.listik[i][k]
                                        count_guard += 1
                            if k % 3 == 2:
                                end_count = round(sum(end_count) * 100 / (len(end_count)*4), 2)
                                self.persentages_stat[i].append(end_count)
                                self.check_persentages_numbers[i].append(k//3+5)
                                self.end_list[i][k//3].text = f"{end_count}"
                                end_count = list()
                        else:
                            if len(end_count) == 0:
                                continue
                            if k % 3 == 2:
                                end_count = round(sum(end_count) * 100 / (len(end_count)*4), 2)
                                self.persentages_stat[i].append(end_count)
                                self.check_persentages_numbers[i].append(k//3+5)
                                self.end_list[i][k//3].text = f"{end_count}"
                                end_count = list()
                                
                    
                    helper = round(helper*100 / ((len(self.listik[i]) - len(self.check_info[i]))* 4))
                    if sum_dro != 0:
                        sum_dro = round(sum_dro / (count_dro*4) * 100, 2)
                        self.persentages_stat[i].append(sum_dro)
                    else:
                        self.persentages_stat[i].append(-1.0)
                    if sum_take != 0:
                        sum_take = round(sum_take / (count_take*4) * 100, 2)
                        self.persentages_stat[i].append(sum_take)
                    else:
                        self.persentages_stat[i].append(-1.0)
                    if sum_guard != 0:
                        sum_guard = round(sum_guard / (count_guard*4) * 100, 2)
                        self.persentages_stat[i].append(sum_guard)
                    else:
                        self.persentages_stat[i].append(-1.0)
                        
                    self.persentages_stat[i].append(helper)
                    self.persentages_stat[i] = self.persentages_stat[i][-4:] + self.persentages_stat[i][:-4]
                    
                    self.final_percentage_list[i].text = f"Процент: {helper}"
                    self.types_throw_list[i].text = f"Dro: {sum_dro} \nTake: {sum_take} \nGuard: {sum_guard}"
                    print(self.persentages_stat)
                
                else:
                    self.final_percentage_list[i].text = f"Ошибка, {helper}"
                    self.types_throw_list[i].text = ""

                flag = True
                sum_dro = 0
                sum_take = 0
                sum_guard = 0
                count_dro = 0
                count_take = 0
                count_guard = 0
                self.check_info[i].sort(reverse=True)
                
                helper = 0
                
            else:
                self.final_percentage_list[i].text = "Ошибка игрока"
                self.types_throw_list[i].text = ""
            
    def save_match(self, instance, *args):
        if "Ошибка" in self.final_percentage_1.text or "Ошибка" in self.final_percentage_2.text or self.final_percentage_1 == "":
            self.save_info.text = "Ошибка сохранения"
        
        elif self.name_match.text == "" or self.date_match.text == "" or self.name_team.text == "":
            self.save_info.text = "Ошибка с данными матча"
        else:
            
            def create_insert_query(column_names, values):
                placeholders = ', '.join(['?'] * (len(values)+1))
                query = f"INSERT INTO points ({', '.join(column_names)}) VALUES ({placeholders})"
                return query
            
            def create_insert_query_2(column_names, values):
                placeholders = ', '.join(['?'] * (len(values)+1))
                query = f"INSERT INTO match_persteges_info ({', '.join(column_names)}) VALUES ({placeholders})"
                return query
            
            column_names = ['match_id', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty_one', 
                    'twenty_two', 'twenty_three', 'twenty_four', 'extra_one', 'extra_two', 'extra_three', 'extra_four', 'extra_five', 'extra_six', 'extra_seven', 'extra_eight', 'extra_nine']
            
            column_names_2 = ['points_id', 'dro_persent', 'take_persent', 'guard_persent', 'final_persent', 'end_1_persent', 'end_2_persent', 'end_3_persent', 'end_4_persent', 'end_5_persent', 'end_6_persent',
                              'end_7_persent', 'end_8_persent', 'ex_1_end_persent', 'ex_2_end_persent', 'ex_3_end_persent']
            
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
            
            for i in range(2):
                name = self.name_list[i].text.title()
                cursor.execute("""
                    SELECT player_id FROM players WHERE first_and_second_name = ?
                """, (name,))
                player_id = cursor.fetchone()
                
                cursor.execute("""
                    INSERT INTO match_players (match_id, player_id) VALUES (?, ?)
                """, (match_id, player_id[0]))
                
                for j in self.check_info[i]:
                    del column_names[j+1]
                    
                query = create_insert_query(column_names, self.check_numbers[i])
                cursor.execute(query, (match_id, *self.check_numbers[i]))
                
                points_id = cursor.lastrowid
                
                cursor.execute("""
                    INSERT INTO match_stats (match_id, points_id) VALUES (?, ?)
                """, (match_id, points_id))
                
                for j in range(len(self.check_persentages_numbers[i])):
                    self.check_persentages_numbers[i][j] = column_names_2[j]
                
                query = create_insert_query_2(self.check_persentages_numbers[i], self.persentages_stat[i])
                cursor.execute(query, (points_id, *self.persentages_stat[i]))
                
                self.conn.commit()
                if i == 1:
                    continue
                else:
                    column_names = ['match_id', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty_one', 
                        'twenty_two', 'twenty_three', 'twenty_four', 'extra_one', 'extra_two', 'extra_three', 'extra_four', 'extra_five', 'extra_six', 'extra_seven', 'extra_eight', 'extra_nine']
                
            
            self.conn.commit()
            self.conn.close()
            self.save_info.text = f"Успешно сохранено"
            
    def switch_match_plus(self, *args):
        
        name_list = [self.name_1, self.name_2]
        
        listik = [[self.one_1, self.two_1, self.three_1, self.four_1, self.five_1, self.six_1, self.seven_1, self.eight_1, self.nine_1, self.one_zero_1,
                  self.one_one_1, self.one_two_1, self.one_three_1, self.one_four_1, self.one_five_1, self.one_six_1, self.one_seven_1, self.one_eight_1, self.one_nine_1,
                  self.two_zero_1, self.two_one_1, self.two_two_1, self.two_three_1, self.two_four_1, self.extra_one_1, self.extra_two_1, self.extra_three_1, self.extra_four_1, self.extra_five_1, self.extra_six_1, self.extra_seven_1, self.extra_eight_1, self.extra_nine_1], 
                  [self.one_2, self.two_2, self.three_2, self.four_2, self.five_2, self.six_2, self.seven_2, self.eight_2, self.nine_2, self.one_zero_2,
                  self.one_one_2, self.one_two_2, self.one_three_2, self.one_four_2, self.one_five_2, self.one_six_2, self.one_seven_2, self.one_eight_2, self.one_nine_2,
                  self.two_zero_2, self.two_one_2, self.two_two_2, self.two_three_2, self.two_four_2, self.extra_one_2, self.extra_two_2, self.extra_three_2, self.extra_four_2, self.extra_five_2, self.extra_six_2, self.extra_seven_2, self.extra_eight_2, self.extra_nine_2]]
        
        type_listik = [[self.one_1_button, self.two_1_button, self.three_1_button, self.four_1_button, self.five_1_button, self.six_1_button, self.seven_1_button, self.eight_1_button, self.nine_1_button,
                       self.one_zero_1_button, self.one_one_1_button, self.one_two_1_button, self.one_three_1_button, self.one_four_1_button, self.one_five_1_button, self.one_six_1_button, self.one_seven_1_button,
                       self.one_eight_1_button, self.one_nine_1_button, self.two_zero_1_button, self.two_one_1_button, self.two_two_1_button, self.two_three_1_button, self.two_four_1_button, self.extra_one_1_button, self.extra_two_1_button,
                       self.extra_three_1_button, self.extra_four_1_button, self.extra_five_1_button, self.extra_six_1_button, self.extra_seven_1_button, self.extra_eight_1_button, self.extra_nine_1_button], 
                       [self.one_2_button, self.two_2_button, self.three_2_button, self.four_2_button, self.five_2_button, self.six_2_button, self.seven_2_button, self.eight_2_button, self.nine_2_button,
                       self.one_zero_2_button, self.one_one_2_button, self.one_two_2_button, self.one_three_2_button, self.one_four_2_button, self.one_five_2_button, self.one_six_2_button, self.one_seven_2_button,
                       self.one_eight_2_button, self.one_nine_2_button, self.two_zero_2_button, self.two_one_2_button, self.two_two_2_button, self.two_three_2_button, self.two_four_2_button, self.extra_one_2_button, self.extra_two_2_button,
                       self.extra_three_2_button, self.extra_four_2_button, self.extra_five_2_button, self.extra_six_2_button, self.extra_seven_2_button, self.extra_eight_2_button, self.extra_nine_2_button]]        
                
        for i in range(len(name_list)):
            name_list[i].text = ""
            for widget in listik[i] + type_listik[i]:
                widget.text = "" if widget in listik[i] else "-"
            if self.flag_page == False:
                for widget in self.end_list[i]:
                    widget.text = "."
        if self.flag_page == False:
            for i in range(len(self.types_throw_list)):
                self.types_throw_list[i].text = ""
                self.final_percentage_list[i].text = ""
        
        self.name_match.text = ""
        self.name_team.text = ""
        self.date_match.text = ""
        
        self.flag_page=True
        
        self.manager.current = "Игра+"