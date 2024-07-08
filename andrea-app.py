from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.label import Label
from kivy.uix.settings import Popup, dp
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import FocusBehavior
from kivy.lang import Builder
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.storage.jsonstore import JsonStore
import json
from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker, MDTimePicker
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager,Screen


    


class MainApp(MDApp):
    ddate=StringProperty("")
    ttime=StringProperty("")
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Pink"
        return Builder.load_file('Queen.kv')

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_selected)
        date_dialog.open()

    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.on_time_selected)
        time_dialog.open()

    def on_time_selected(self, instance,time):
        self.ttime=str(time)

    def on_date_selected(self, instance,value, date_range):
        self.ddate=str(value)
class MyScreenManager(ScreenManager):
    pass


       

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class SecondScreen(Screen):
    nname = StringProperty("")
    nnage =StringProperty("")
    nnd= StringProperty("")
    def load21(self, i):
        try:
            # Read existing data
            with open('patients_info.json', 'r') as file:
                data = json.load(file)
                if not isinstance(data, list):
                    data = []
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        # Get the specific patient's data based on the index
        if data and i < len(data):
            # Remove the patient data from the list
            del data[i]

            # Write the updated data back to the file
            with open('patients_info.json', 'w') as file:
                json.dump(data, file)
        else:
            print(f"Patient with index {i} not found.")
            
    def load2(self, i):
        try:
            # Read existing data
            with open('patients_info.json', 'r') as file:
                data = json.load(file)
                if not isinstance(data, list):
                    data = []
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        # Get the specific patient's data based on the index
        if data and i < len(data):
            patient = data[i]
            lname = patient.get("Name", "")
            lage = patient.get("Age", "")
            ldiagnostic = patient.get("Diagnostic", "")
            self.nname = lname
            self.nnage = lage
            self.nnd = ldiagnostic
    def loadwi(self):
        user_data3 = {
            "Name": self.ids.nname5.text,
            "Informations-diagnostic": self.ids.diagnostic_info1.text,
            "Analyse de la seance": self.ids.session_analysis.text
        }
        if any(user_data3.values()):
            try:
                # Read existing data
                with open('work_info.json', 'r') as file:
                    data3 = json.load(file)
                    if not isinstance(data3, list):
                        data3 = []
            except (FileNotFoundError, json.JSONDecodeError):
                data3 = []

            data3.append(user_data3)

            with open('work_info.json', 'w') as file:
                json.dump(data3, file, indent=4)
        else:
            print("User data is empty. Nothing to append.")
        app = App.get_running_app()
        app.root.current = 'main'
        app.root.transition.direction = 'right'

  
    wki =StringProperty("")
    wka= StringProperty("")
    def load3(self):
        try:
            with open('work_info.json', 'r') as file:
                data = json.load(file)
                if not isinstance(data, list):
                    print("Data format is incorrect.")
                    return None
        except (FileNotFoundError, json.JSONDecodeError):
            print("File not found or JSON decode error.")
            return None

        for user_data in data:
            if user_data.get("Name") == self.nname:
                self.wkname = user_data.get("Name", "")
                self.wki = user_data.get("Informations-diagnostic", "")
                self.wka = user_data.get("Analyse de la seance", "")
            

        print("No information found for the specified name.")
        return None

class Bx2(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nname1 = ""

    def get_info(self):
        try:
            # Read existing data
            with open('patients_info.json', 'r') as file:
                data = json.load(file)
                if not isinstance(data, list):
                    data = []
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        self.ids.scroll_layout.clear_widgets()
        for i, patient in enumerate(data):
            name = patient.get("Name", "")
            age = patient.get("Age", "")
            diagnostic = patient.get("Diagnostic", "")
            date = patient.get("Date", "")
            time = patient.get("Time", "")
            inf = f"{name},{age}\n{date},{time}\n{diagnostic}"
            if inf:
                button_id = i
                new_button = Button(
                    text=inf,
                   # size_hint_y=1,
                   size_hint_x=0.8,
                   size_hint_y=1,
                   # pos_hint={'top': 0, 'right': 0.2},
                    font_size='12sp',
                    background_color=(1, 0.5, 0.5, 1)
                )
                new_button.id = str(button_id)
                new_button.bind(on_touch_up=lambda instance: self.goto(instance.id))
###
                button_id = i
                new_button2 = Button(
                    text="delete",
                   # size_hint_y=1,
                    #font_size='12sp',
                   # pos_hint={'top': 0, 'right': 0.2},
                    size_hint_x=0.2,
                    size_hint_y=1,
                    background_color=(1, 0.5, 0.5, 1)
                )
                new_button2.id = str(button_id)
                new_button2.bind(on_touch_up=lambda instance: self.delete(instance.id))
                new_layout=f"layout{i}"
                new_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=dp(50), pos_hint={'top': 1, 'right': 1}, spacing=dp(0))
                self.ids.scroll_layout.add_widget(new_layout)
                new_layout.add_widget(new_button)
                new_layout.add_widget(new_button2)
    def delete(self, button_id):
        app = App.get_running_app()
        second_screen = app.root.get_screen('workdone')
        second_screen.load21(int(button_id))

    def goto(self, button_id):
        app = App.get_running_app()
        second_screen = app.root.get_screen('workdone')
        second_screen.load2(int(button_id))
        app.root.current = 'workdone'
        app.root.transition.direction = 'left'


    
        
        

    

class Bx1(BoxLayout):
    pass



class Bx3(BoxLayout):
    sbtext=StringProperty("SAVE")
    def save_info(self):
        user_data = {
            "Name": self.ids.name_input.text,
            "Age": self.ids.age_input.text,
            "Diagnostic": self.ids.diagnostic_input.text,
            "Date": self.ids.date_picked.text,
            "Time": self.ids.time_picked.text
        }
        if any(user_data.values()):
            try:
                # Read existing data
                with open('patients_info.json', 'r') as file:
                    data = json.load(file)
                    if not isinstance(data, list):
                        data = []
            except (FileNotFoundError, json.JSONDecodeError):
                data = []

            data.append(user_data)

            with open('patients_info.json', 'w') as file:
                json.dump(data, file, indent=4)
        else:
            print("User data is empty. Nothing to append.")

        ###########
        user_data2 = {
            "Name": self.ids.name_input.text,
            "Age": self.ids.age_input.text,
            "Diagnostic": self.ids.diagnostic_input.text
        }
        if any(user_data2.values()):
            try:
                # Read existing data
                with open('opatients_info.json', 'r') as file:
                    data2 = json.load(file)
                    if not isinstance(data2, list):
                        data2 = []
            except (FileNotFoundError, json.JSONDecodeError):
                data2 = []
            data2.append(user_data2)
            with open('opatients_info.json', 'w') as file:
                json.dump(data2, file, indent=4)
        else:
            print("User data is empty. Nothing to append.")
        # Write updated data back to the file
        ############

    def saved_text(self):
        self.sbtext="SAVED"

    def save(self):
        self.save_info()
        self.saved_text()
    #pass

class wd(BoxLayout):
    pass




class Queen(App):
    pass

if __name__ == '__main__':
    MainApp().run()
    #Queen().run()
