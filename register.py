from asyncio.windows_events import NULL
import email
import firebase_admin 
from firebase_admin import credentials, firestore
import pyrebase
import pygame_menu
import pygame

cred = credentials.Certificate("./shootinggame-adf10-firebase-adminsdk-mb0cr-86331adc29.json")


firebaseConfig = {
  'apiKey': "AIzaSyCTG8WWk89CaPfUPwjNPObOce13gDC-Uro",
  'authDomain': "shootinggame-adf10.firebaseapp.com",
  'projectId': "shootinggame-adf10",
  'storageBucket': "shootinggame-adf10.appspot.com",
  'messagingSenderId': "205816370300",
  'appId': "1:205816370300:web:d9781abb8849788013e5f9",
  'measurementId': "G-YZ257BPC77",
  'databaseURL':"https://shootinggame-adf10-default-rtdb.firebaseio.com/"
}

firebase_admin.initialize_app(cred,{'databaseURL':"https://shootinggame-adf10-default-rtdb.firebaseio.com/"})

firebase=pyrebase.initialize_app(firebaseConfig)


auth=firebase.auth()
db=firestore.client()


#Login
def Login(email,password):
  global user
  user=email
  login = 0
  try:
    login=auth.sign_in_with_email_and_password(email,password)
    print("Successfully signed in!")
  except:
    print("Invalid user or password. Try again")
  return login

#register
def register(email,password,confirmPassword):
  if password==confirmPassword:
    try:
      auth.create_user_with_email_and_password(email,password)
      data={
        "email":email,
        "item_apply":"basic",
        "item":["basic"],
        "rank":0,
        "coin":0
      }
      db.collection("User").document(email).set(data)
      return 1
    except:
      print("Email already exists")
      return 0

def passwordReset(email):
  auth.send_password_reset_email(email)

#Database
#Create
#data={'age':32,'address':'LA','emplyed':False,'name':"Mark"}
#ref.update({'age':32,'address':'LA','emplyed':False,'name':"Mark"})
#db.child("name").push({"company": "google"})


#Update

#doc_ref=db.collection("User").document("1234sdasd@gmail.com")
#doc_ref.update({"number":123})
#Delete
#db.child("User").child("fjkds").child("age").remove()

#people=db.child("people").get()
#for person in people.each():
#  print(person.val())
#  print(person.key())
#  if person.val()['name']=='Mark':
#    db.child('people').child(person.key()).update({'name':'Jane'})

