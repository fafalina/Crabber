import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("C:\\Users\\HighSpeed\\Desktop\\Crabber-Firesbase\\serviceAccountKey.json")
firebase_admin.initialize_app(cred)

print(23)