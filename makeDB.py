import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from numpy import unicode_
import requests
import json

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
url = ""

headers = {
    
}

response = requests.request("GET", url, headers=headers)
for i in response.json():
    print(i["name"])
    name = i['id']
    print(i["bodyPart"])
    db.collection("Exercises").document(name).set(
        {
            u"bodyPart": i["bodyPart"],
            u"equipment": i["equipment"],
            u"gifUrl": i["gifUrl"],
            u"id": i["id"],
            u"name": i["name"],
            u"target": i["target"],
        }
    )
