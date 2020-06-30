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
import sqlite3








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
    id: register
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
    last_email_text_input: email
    last_password_text_input: password
    lbl:my_label
    Label:
        text:"Enter Credentials"
        pos:0,200
        
    Label:
        id: my_label
        color: [1, 0, 0, 1] 
    Label:
        markup:True
        text:"[ref=first ref]Forgot Password?[/ref]"
        pos:200,50
        on_ref_press: root.forgot()
    Label:
        text:"Enter Registered Email"
        pos:-230,150
        font_size:20
        TextInput:
            multiline:False
            pos:280,435
            size:300,30
            font_size:15
            id:email
            auto_dismiss: False

    Label:
        text:"Enter password"
        pos:-200,95
        font_size:20
        TextInput:
            multiline:False
            pos:280,380
            size:300,30
            font_size:15
            id:password
            auto_dismiss: False
            password: True
    Button:
        text: 'LOGIN'
        size_hint: (.3,.1)
        pos:(280,180)
        width: 200
        on_press: root.credentials()      
            
            
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
    id:account
    first_name_text_input:name
    last_name_text_input:name
    create_password_text_input:password
    confirm_password_text_input:pswd
    confirmed_email_text_input:conf_email
    lbl:my_label
    Label: 
        id: my_label
        color: [1, 0, 0, 1]
        pos:245,55
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
        text:"Enter E-mail"
        pos:-180,54
        font_size:20
        TextInput:
            multiline:False
            pos:280,340
            size:300,28
            font_size:15
            id:conf_email
            auto_dismiss: False
            
    Label:
        text:"Create Password"
        pos:-200,13
        font_size:20
        TextInput:
            multiline:False
            pos:280,300
            size:300,25
            font_size:10
            id:password
            auto_dismiss: False
            password: True
            
    Label:
        text:"Confirm Password"
        pos:-210,-27
        font_size:20
        TextInput:
            multiline:False
            pos:280,260
            size:300,25
            font_size:10
            id:pswd 
            auto_dismiss: False
            password:True
    Button:         
        text: 'FINISH CREATING ACCOUNT'
        size_hint: (.3,.1)
        pos:(280,180)
        width: 200
        on_press: root.finish()
            
            
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

<reset>:
    last_email_text_input: email
    last_password_text_input:password
    last_new_text_input:passwrd
    lbl: my_label
    Label:
        id: my_label
        color: [1, 0, 0, 1] 
    
    Label:
        text:"Reset your password"
        pos:0,200
    Label:
        text:"Enter Registered Email"
        pos:-230,150
        font_size:20
        TextInput:
            multiline:False
            pos:280,435
            size:300,30
            font_size:15
            id:email
            auto_dismiss: False
            
    Label:
        text:"Enter old password"
        pos:-220,95
        font_size:20
        TextInput:
            multiline:False
            pos:280,380
            size:300,30
            font_size:15
            id:password
            auto_dismiss: False
            
    
    Label:
        text:"Enter new password"
        pos:-220,55
        font_size:20
        TextInput:
            multiline:False
            pos:280,338
            size:300,30
            font_size:15
            id:passwrd
            auto_dismiss: False
        
    Button:         
        text: 'UPDATE PASSWORD AND CONTINUE'
        size_hint: (.4,.1)
        pos:(270,180)
        width: 200
        on_press: root.passwrd_update()
        
     
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
        global mail
        mail=self.last_email_text_input.text
        self.generate_pass = ''.join([random.choice( string.ascii_uppercase +string.ascii_lowercase + string.digits)  for n in range(10)])
        
        if '@' in mail:
            fromaddr = "babipaul135@gmail.com"
            toaddr = mail
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
    
    def forgot(self):
        Clock.schedule_once(self.changeScreen,1)
        
    def changeScreen(self,*args):
        self.parent.current='reset'
    
    def entry(self,*args):
        self.parent.current='intro'
    
    def credentials(self):
        self.email=self.last_email_text_input.text
        self.password=self.last_password_text_input.text
        start=sqlite3.connect("user_details.db")
        cursor=start.execute("SELECT EMAIL_ID,PASSWORD FROM USERS")
        for row in cursor:
            print("email id-",row[0])
            print("password-",row[1])
            
        if self.email==row[0] and self.password==row[1]:
            
            Clock.schedule_once(self.entry,1)
        else:
            self.lbl.text='Enter correct credentials'
    
class account(Screen):
    pass
    
        
    
    def make(self):
        self.first_name=self.first_name_text_input.text
        self.last_name=self.last_name_text_input.text
        self.create_password=self.create_password_text_input.text
        self.confirm_password=self.confirm_password_text_input.text
        self.confirm_email=self.confirmed_email_text_input.text
        start=sqlite3.connect('user_details.db')
        start.execute("DROP TABLE USERS;")
        start.execute('''CREATE TABLE IF NOT EXISTS USERS(EMAIL_ID TEXT PRIMARY KEY,FIRST_NAME TEXT,LAST_NAME TEXT,PASSWORD TEXT)''')
        start.execute("INSERT INTO USERS (EMAIL_ID,FIRST_NAME, LAST_NAME, PASSWORD) VALUES(?, ?, ?, ?)", (self.confirm_email,self.first_name, self.last_name,self.create_password))
        start.commit()
        print('Inserted successfully')
        start.close()
        Clock.schedule_once(self.changeScreen,1)
        

    def changeScreen(self, *args):
        self.parent.current='confirmation'
    
    def finish(self):
        global mail
        self.first_name=self.first_name_text_input.text
        self.last_name=self.last_name_text_input.text
        self.create_password=self.create_password_text_input.text
        self.confirm_password=self.confirm_password_text_input.text
        self.confirmed_email_text_input.text=f"{mail}"
        self.password=self.create_password
        self.confirmed=self.confirm_password
        email=self.confirmed_email_text_input.text
        password=self.password
        confirmed=self.confirmed
        
        print(password)
        print(confirmed)
        
       
        if (self.password_check(password) and '@' in email and password==confirmed):
            
            
            self.make() 
            
                
       
                                           
        
            
        
        
        else:
            self.lbl.text='Check email and password once again'
           
           
            
        
    
    
    def password_check(self,password):
        SpecialSym =['$', '@', '#', '%'] 
        val=True
        
        if len(password)<6:
            val=False
            
        if len(password)>15:
            val=False
           
        if not any(char.isdigit() for char in password): 
            val=False
            
        if not any(char.isupper() for char in password):
            val=False
            
        if not any(char.islower() for char in password):
            val=False
            
        if not any(char in SpecialSym for char in password):
            val=False
        
        
        if val:
            return val
        
    
        
        
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
        self.parent.current = "details"
    
class intro(Screen):
    pass

class reset(Screen):
    pass
    
    def update(self):
        self.email=self.last_email_text_input.text
        self.password=self.last_password_text_input.text
        self.new=self.last_new_text_input.text
        start=sqlite3.connect('user_details.db')
        start.execute('''UPDATE USERS SET PASSWORD = ? WHERE EMAIL_ID = ?''', (self.new, self.email))
        start.commit()
        print(start.total_changes)
        cursor= start.execute("SELECT EMAIL_ID, PASSWORD from USERS")
        for row in cursor:
            print ("EMAIL-ID-", row[0])
            print ("PASSWORD-", row[1])
        start.close()
       
        
        
    def passwrd_update(self):
        self.email=self.last_email_text_input.text
        self.password=self.last_password_text_input.text
        self.new=self.last_new_text_input.text
        password=self.new
        start=sqlite3.connect('user_details.db')
        cursor_1=start.execute("SELECT EMAIL_ID, PASSWORD FROM USERS")
        for row in cursor_1:
            print ("EMAIL-ID-", row[0])
            print ("OLD-PASSWORD-", row[1])
            
        start.close()
        
        if self.password==row[1] and self.email==row[0] and self.password_check(password):
            self.update()
            Clock.schedule_once(self.changeScreen,1)
            
        else:
            self.lbl.text='Enter correct old credentials'
            
    
    def password_check(self,password):
        
        SpecialSym =['$', '@', '#', '%'] 
        val=True
        
        if len(password)<6:
            val=False
            
        if len(password)>15:
            val=False
           
        if not any(char.isdigit() for char in password): 
            val=False
            
        if not any(char.isupper() for char in password):
            val=False
            
        if not any(char.islower() for char in password):
            val=False
            
        if not any(char in SpecialSym for char in password):
            val=False
        
        
        if val:
            return val
    
        
    def changeScreen(self, *args):
        self.parent.current='login'
        
    


        

sm=ScreenManager()
sm.add_widget(start(name ="start")) 
sm.add_widget(login(name ="login")) 
sm.add_widget(register(name="register"))
sm.add_widget(details(name="details"))
sm.add_widget(account(name="account"))
sm.add_widget(confirmation(name="confirmation"))
sm.add_widget(intro(name="intro"))
sm.add_widget(reset(name="reset"))


class App(App):
    def build(self):
        return sm
        
        
App().run()
 