import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def CFSet(novel_name, chapter_id, datas):
    #新增內容
    db_ref = db.collection("novel").document(novel_name).collection("chapter").document(chapter_id)
    db_ref.set(datas)
    #TODO 新增最後更新時間



cred = credentials.Certificate("C:\\Users\\HighSpeed\\Desktop\\Crabber-Firesbase\\serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

'''
# 指定路徑 建立文件 必須給定 集合名稱 文件id
# 即使 集合一開始不存在 都可以直接使用
datas_ref = db.collection("test_collection").document("test_docment")
datas_ref.set(datas)
'''