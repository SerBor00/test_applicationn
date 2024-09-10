from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from database import path_db
import sqlite3

class archive_matches(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        bl = BoxLayout()
        
        self.search = TextInput(hint_text = "Имя и Фамилия игрока", multiline=False, size_hint_y=None, height= 32, size_hint=(None, None) , size = (500 , 32))
        bl.add_widget(self.search)
        
        self.conn = sqlite3.connect(path_db())
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("""
            SELECT * FROM matches
        """)
        match_info = self.cursor.fetchall()
        
        if match_info:  # Проверяем, не пуст ли список match_info
            for match_data in match_info:
                perstenges = list()
                
                self.cursor.execute("""
                    SELECT 
                    p.first_and_second_name
                    FROM players p
                    JOIN match_players mp ON p.player_id = mp.player_id
                    WHERE mp.match_id = ?
                """, (match_data[0],))
                names = self.cursor.fetchall()
                
                self.cursor.execute("""
                    SELECT 
                    p.player_id
                    FROM players p
                    JOIN match_players mp ON p.player_id = mp.player_id
                    WHERE mp.match_id = ?
                """, (match_data[0],))
                
                player_id = self.cursor.fetchall()
                
                for i in range(len(player_id)):
                    
                    self.cursor.execute("""
                        SELECT 
                            mpi.* 
                        FROM 
                            match_persteges_info mpi 
                        JOIN 
                            points p ON mpi.points_id = p.points_id
                        JOIN 
                            match_stats ms ON p.points_id = ms.points_id
                        JOIN 
                            matches m ON ms.match_id = m.match_id
                        JOIN 
                            match_players mp ON m.match_id = mp.match_id
                        WHERE 
                            mp.player_id = ? AND m.match_id = ?;
                    """, (player_id[i][0], match_data[0],))
                    
                perstenges=self.cursor.fetchall()
                button = Button(text=f"Дата: {match_data[1]} Команды: {match_data[2]} Турнир: {match_data[3]}")
                button.bind(on_press=lambda instance, match_data=match_data, names=names, perstenges=perstenges: self.show_popup(match_data, names, perstenges))
                bl.add_widget(button)
                

        archive = Button(text="Назад", size_hint=(None, None) , size = (270 , 60))
        archive.bind(on_release=self.switch_archive)
        bl.add_widget(archive)
        self.add_widget(bl)
        
    def show_popup(self, match_data, names, perstenges):
            if len(names) == 2:
                name_percent=["Dro %", "Take %", "Guard %", "final %", "End 1", "End 2", "End 3", "End 4", "End 5", "End 6", "End 7", "End 8", "Ex-end 1", "Ex-end 2", "Ex-end 3"]
            else:
                name_percent=["Dro %", "Take %", "Guard %", "final %", "End 1", "End 2", "End 3", "End 4", "End 5", "End 6", "End 7", "End 8", "End 9", "End 10", "Ex-end 1", "Ex-end 2", "Ex-end 3"]
                
            for i in range(len(perstenges)):
                perstenges[i] = perstenges[i][1:]
                
            popup = Popup(title=f"Матч: {match_data[3]}")
            popup.content = BoxLayout(orientation='vertical')
            popup.content.add_widget(Label(text=f"Команды: {match_data[2]}"))
            gl = GridLayout(cols=len(names), rows=1)
            for name in names:
                gl.add_widget(Label(text = f"{name[0]}"))
            gl2 = GridLayout(cols=len(names)*2 , rows=len(name_percent))
            if len(names) == 2:
                range_h = 0
                for i in range(len(name_percent)+2):
                    if i == 12:
                        continue
                    elif i == 13:
                        range_h = 2
                        continue
                    else:
                        gl2.add_widget(Label(text=f"{name_percent[i-range_h]}"))
                        gl2.add_widget(Label(text=f"{perstenges[0][i]}"))
                        gl2.add_widget(Label(text=f"{name_percent[i-range_h]}"))
                        gl2.add_widget(Label(text=f"{perstenges[1][i]}"))
            elif len(names) == 3:
                for i in range(len(name_percent)):
                    gl2.add_widget(Label(text=f"{name_percent[i]}"))
                    gl2.add_widget(Label(text=f"{perstenges[0][i]}"))
                    gl2.add_widget(Label(text=f"{name_percent[i]}"))
                    gl2.add_widget(Label(text=f"{perstenges[1][i]}"))
                    gl2.add_widget(Label(text=f"{name_percent[i]}"))
                    gl2.add_widget(Label(text=f"{perstenges[2][i]}"))
            elif len(names) == 4:
                for i in range(len(name_percent)):
                    gl2.add_widget(Label(text=f"{name_percent[i]}"))
                    gl2.add_widget(Label(text=f"{perstenges[0][i]}"))
                    gl2.add_widget(Label(text=f"{name_percent[i]}"))
                    gl2.add_widget(Label(text=f"{perstenges[1][i]}"))
                    gl2.add_widget(Label(text=f"{name_percent[i]}"))
                    gl2.add_widget(Label(text=f"{perstenges[2][i]}"))
                    gl2.add_widget(Label(text=f"{name_percent[i]}"))
                    gl2.add_widget(Label(text=f"{perstenges[3][i]}"))
            else:
                for i in range(len(name_percent)):
                    gl2.add_widget(Label(text=f"{name_percent[i]}"))
                    gl2.add_widget(Label(text=f"{perstenges[0][i]}"))
                    gl2.add_widget(Label(text=f"{name_percent[i]}"))
                    gl2.add_widget(Label(text=f"{perstenges[1][i]}"))
                    gl2.add_widget(Label(text=f"{name_percent[i]}"))
                    gl2.add_widget(Label(text=f"{perstenges[2][i]}"))
                    gl2.add_widget(Label(text=f"{name_percent[i]}"))
                    gl2.add_widget(Label(text=f"{perstenges[3][i]}"))
                    gl2.add_widget(Label(text=f"{name_percent[i]}"))
                    gl2.add_widget(Label(text=f"{perstenges[4][i]}"))
            
            popup.content.add_widget(gl)
            popup.content.add_widget(gl2)

            popup.content.add_widget(Button(text="Закрыть", on_press=lambda instance: popup.dismiss()))
            popup.open()
        
    def switch_archive(self, *args):
        self.conn.close()
        self.manager.current = "Архив"