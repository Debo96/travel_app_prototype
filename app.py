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
import smtplib
import random
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import threading
from threading import Thread,Event
from multiprocessing import Process
import multiprocessing
import time
import threading




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
    last_otp_text_input: OTP
    lbl:my_label
    Label:
        text:"Register"
        pos:0,200
    
    Label:
        id: my_label
        color: [1, 0, 0, 1] 
        
        
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
        on_press: root.press()   
        on_press: root.afterpress()
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
        self.generate_pass = ''.join([random.choice( string.ascii_uppercase +string.ascii_lowercase + string.digits)  for n in range(10)])
        if '@' in self.email:
            fromaddr = "babipaul135@gmail.com"
            toaddr = self.email
            msg = MIMEMultipart() 
            msg['From'] = fromaddr 
            msg['To'] = toaddr 
            msg['Subject'] = "Thanks for choosing us"
            message='Hello, this is your authentication OTP:-{}'.format(self.generate_pass)
            msg.attach(MIMEText(message))
            s = smtplib.SMTP('smtp.gmail.com', 587) 
            s.ehlo()
            s.starttls() 
            s.login(fromaddr, "babipaljoker") 
            text = msg.as_string() 
            s.sendmail(fromaddr, toaddr, text) 
            s.quit() 
            self.lbl.text='OTP sent successfully!!'
            Clock.schedule_once(self.reset_label, 11)
            
            
        else:
            self.lbl.text='Incorrect email id!!'
           
            
    def reset_label(self,*args):
        self.lbl.text=''
        

    
    def auth(self, *args):
        self.email_otp=self.generate_pass
        self.otp=self.last_otp_text_input.text
        
        if self.otp==self.email_otp:
            self.changeScreen()
            
        
            
        else:
            self.lbl.text='OTP is incorrect'
        
        
        
            
                
            
            
            
           
                
            
            
            
            
            
            
            
            
              
        
           
              
            
                
       
        
        
            
        
        
      
                
               
        
    def changeScreen(self, *args):
        
        #now switch to the screen next
        self.parent.current = "account"
    
    def invalid(self,*args):
        
            
        self.lbl.text='OTP is not valid anymore'
        self.parent.current='register'
    
    def press(self):
        timer = threading.Timer(1.0, self.auth) 
        timer.start()
        if self.lbl.text=='OTP is not valid anymore':
            timer.cancel()
        
    def afterpress(self):
        timer = threading.Timer(25.0,self.invalid)
        timer.start()
       
   
    
        

    
  
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
 