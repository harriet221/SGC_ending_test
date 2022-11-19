import firebase_admin 
from firebase_admin import credentials, firestore

from register import db
from Defs import *

def item_buy(user,item):
  coin_buy(user,item)
  db.collection("User").document(user).update({"item":firestore.ArrayUnion([item])})

def item_buyList_get(user):
  itemList=db.collection("User").document(user).get().to_dict()
  return itemList["item"]

def item_apply(user,item):
  db.collection("User").document(user).update({"item_apply":item})


def item_apply_get(user):
  field=db.collection("User").document(user).get().to_dict()
  return field["item_apply"]

def coin_set(user,new_coin):
  db.collection("User").document(user).update({"coin":firestore.Increment(new_coin)})

def coin_get(user):
  field=db.collection("User").document(user).get().to_dict()
  return field["coin"]

def coin_buy(user,item):
  if item=="bullets":
    db.collection("User").document(user).update({"coin":firestore.Increment(Item.coin_10k)})
  elif item=="missile":
    db.collection("User").document(user).update({"coin":firestore.Increment(Item.coin_50k)})
  elif item=="missile2":
    db.collection("User").document(user).update({"coin":firestore.Increment(Item.coin_50k)})
  elif item=="bomb":
    db.collection("User").document(user).update({"coin":firestore.Increment(Item.coin_100k)})

def coin_give(user,coin):
  coin=int(coin)
  db.collection("User").document(user).update({"coin":firestore.Increment(coin)})

def rank_set(user,new_coin): #랭킹 DB 저장
  field=db.collection("User").document(user).get().to_dict()
  current_rank=field["rank"]
  if new_coin>current_rank:
    db.collection("User").document(user).update({"rank":new_coin})

def rank_get(user):
  field=db.collection("User").document(user).get().to_dict()
  return field["rank"]

def rank(user,score): # 높은 점수를 랭킹에 저장
    current_rank = rank_get(user)
    if current_rank < score:
        rank_set(user,score)
