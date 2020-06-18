import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder 
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import kivy.uix.button as kb
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput





Builder.load_string(""" 
<start>:
    Label:
        text:"Hello"
        
        
                      
                
               
                
<login>:
    Label:
        text:"Welcome"
        pos:0,200
    Button:         
        text: 'LOGIN'
        size_hint: (.3,.1)
        pos:(280,350)
        width: 200
        on_press: 
            root.manager.transition.direction = 'left' 
            root.manager.transition.duration = 1 
            root.manager.current = 'details'
    Button:         
        text: 'SIGN-UP'
        size_hint: (.3,.1)
        pos:(280,250)
        width: 200
        on_press: 
            root.manager.transition.direction = 'left' 
            root.manager.transition.duration = 1 
            root.manager.current = 'register'
<register>:
    last_email_text_input: email
    Label:
        text:"Register"
        pos:0,200
    
    Label:
        text:"Email"
        pos:-180,150
        font_size:20
        TextInput:
            multiline:False
            pos:280,435
            size:300,30
            font_size:15
            id:email
            auto_dismiss: False
            
    Button:
        text:"Verify E-mail"
        size_hint:(.2,.1)
        pos:(590,420)
        width:100
        on_press:root.verify()
    Label:
        text:"OTP"
        pos:-180,95
        font_size:20
        TextInput:
            multiline:False
            pos:280,380
            size:300,30
            font_size:15
            id:OTP
            auto_dismiss: False
    Button:         
        text: 'BACK TO LOGIN PAGE'
        size_hint: (.3,.1)
        pos:(280,100)
        width: 200
        on_press: 
            root.manager.transition.direction = 'left' 
            root.manager.transition.duration = 1 
            root.manager.current = 'login'
    Button:
        text: 'MAKE ACCOUNT'
        size_hint: (.3,.1)
        pos:(280,180)
        width: 200
        on_press: 
            root.manager.transition.direction = 'left' 
            root.manager.transition.duration = 1 
            root.manager.current = 'account'
<details>:
    Label:
        text:"Enter Credentials"
        pos:0,200
    Button:         
        text: 'BACK TO LOGIN PAGE'
        size_hint: (.3,.1)
        pos:(280,100)
        width: 200
        on_press: 
            root.manager.transition.direction = 'left' 
            root.manager.transition.duration = 1 
            root.manager.current = 'login'    
    
<account>:
    Label:
        text: "Provide Details"
        pos:0,200
    Label:
        text:"First Name"
        pos:-180,150
        font_size:20
        TextInput:
            multiline:False
            pos:280,435
            size:300,30
            font_size:15
            id:name
            auto_dismiss: False
    Label:
        text:"Last Name"
        pos:-180,95
        font_size:20
        TextInput:
            multiline:False
            pos:280,380
            size:300,30
            font_size:15
            id:name
            auto_dismiss: False
    Label:
        text:"Create Password"
        pos:-200,55
        font_size:20
        TextInput:
            multiline:False
            pos:280,340
            size:300,25
            font_size:10
            id:password
            auto_dismiss: False
            
    Label:
        text:"Confirm Password"
        pos:-210,15
        font_size:20
        TextInput:
            multiline:False
            pos:280,300
            size:300,25
            font_size:10
            id:password 
            auto_dismiss: False
    Button:         
        text: 'FINISH CREATING ACCOUNT'
        size_hint: (.3,.1)
        pos:(280,180)
        width: 200
        on_press: 
            root.manager.transition.direction = 'left' 
            root.manager.transition.duration = 1 
            root.manager.current = 'confirmation'   
    Button:         
        text: 'BACK TO REGISTER PAGE'
        size_hint: (.3,.1)
        pos:(280,100)
        width: 200
        on_press: 
            root.manager.transition.direction = 'left' 
            root.manager.transition.duration = 1 
            root.manager.current = 'register' 

<confirmation>:
    Label:
        text: "Congratulations, you have been successfully registered!!"
        pos:0,200

<intro>:
    Label:
        text: "Start from here"
        pos:0,200   
""")
    

class start(Screen):
    pass
    def __init__(self,**kwargs):
        super(start, self).__init__(**kwargs)

    #this is event that is fired when the screen is displayed.
    def on_enter(self, *args):
        self.displayScreenThenLeave()

    def displayScreenThenLeave(self):
        #schedued after 3 seconds
        Clock.schedule_once(self.changeScreen, 1.7)
    def changeScreen(self, *args):
        #now switch to the screen next
        self.parent.current = "login"
    
class login(Screen):
    pass
    
    
    
class register(Screen):
    pass
    def __init__(self, **kwargs):
        super(register, self).__init__(**kwargs)
    def verify(self):
        self.email=self.last_email_text_input.text
    
        
    
  
class details(Screen):
    pass
    
class account(Screen):
    pass

class confirmation(Screen):
    pass
    def __init__(self,**kwargs):
        super(confirmation, self).__init__(**kwargs)

    #this is event that is fired when the screen is displayed.
    def on_enter(self, *args):
        self.displayScreenThenLeave()

    def displayScreenThenLeave(self):
        #schedued after 3 seconds
        Clock.schedule_once(self.changeScreen, 1.7)
    def changeScreen(self, *args):
        #now switch to the screen next
        self.parent.current = "intro"
    
class intro(Screen):
    pass
    
sm=ScreenManager()
sm.add_widget(start(name ="start")) 
sm.add_widget(login(name ="login")) 
sm.add_widget(register(name="register"))
sm.add_widget(details(name="details"))
sm.add_widget(account(name="account"))
sm.add_widget(confirmation(name="confirmation"))
sm.add_widget(intro(name="intro"))


class App(App):
    def build(self):
        return sm
        
App().run()
 