import email
import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyCTG8WWk89CaPfUPwjNPObOce13gDC-Uro",
  'authDomain': "shootinggame-adf10.firebaseapp.com",
  'projectId': "shootinggame-adf10",
  'storageBucket': "shootinggame-adf10.appspot.com",
  'messagingSenderId': "205816370300",
  'appId': "1:205816370300:web:d9781abb8849788013e5f9",
  'measurementId': "G-YZ257BPC77"
}

firebase=pyrebase.initialize_app(firebaseConfig)

#db=firebase.auth()
auth=firebase.auth()
#storage=firebase.storage()

#Authentication

#Login
def Login():
  email=input("Enter you email")
  password=input("Enter you password")
  try:
    auth.sign_in_with_email_and_password(email,password)
    print("Successfully signed in!")
  except:
    print("Invalid user or password. Try again")
    
