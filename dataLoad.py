import firebase_admin 
from firebase_admin import credentials, firestore

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

db=firestore.client()


def item_buy(user,item):
  db.collection("User").document(user).update({"item":firestore.ArrayUnion([item])})

def item_apply(user,item):
  db.collection("User").document(user).update({"item_apply":item})


def item_apply_get(user):
  field=db.collection("User").document(user).get().to_dict()
  return field["item_apply"]



