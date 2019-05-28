import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#將小說內容寫入資料庫
def CF_Set(novel):
    #新增內容
    try:
        # 指定路徑 建立文件 必須給定 集合名稱 文件id
        # 即使 集合一開始不存在 都可以直接使用
        db_ref = db.collection("novel").document(novel.novel_name).collection("chapter").document(novel.chapter_name)
        db_ref.set(novel.data_to_dict().get_data())
    except Exception:
        print('novel isn\'t exist')
    #TODO 新增最後更新時間

#TODO 批量寫入  再研究
def CF_Batch(novel):
    batch = db.batch

#從資料庫取得小說內容
def CF_Get(novel):
    try:
        db_ref = db.collection("novel").document(novel.novel_name).collection("chapter").document(str(novel.chapter_id))
    except Exception:
        print('novel isn\'t exist')

    return db_ref.get()

#資料庫初始化
def DB_init():
    cred = credentials.Certificate("C:\\Users\\HighSpeed\\Desktop\\Crabber-Firesbase\\serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

DB_init()
db = firestore.client()