from firebase import firebase
import RTfirebaseData

#由輸入資料的NO取得KeyID
def CheckKey(no, datas):
    key_id = ""
    if(datas != None):
        for key in datas:
            if(no == datas[key]["no"]):
                key_id = key
                break
    return key_id

#查詢
def RTDGet():
    return fb.get(table, None)
    '''
    for key,value in result.items():
        print("id={}\tno={}\tname={}".format(key,value["no"],value["name"]))
    '''
#儲data至firebase
def RTDPost():
    for data in datas:
        fb.post(table, data)
        print("{} 儲存完畢".format(data))

#從firebase中移除指定NO那層所有資料
def RTDDelete():
    datas = RTDGet()
    no = input("請輸入要刪除的章節NO\n")
    key_id = CheckKey(int(no), datas)
    if(key_id != ''):
        fb.delete(table + "/" + key_id, None)
        print("移除完畢")
    else:
        print("並無此章節")

#修改firebase
def RTDPut():
    datas = RTDGet()
    no = input("請輸入要修改的章節NO\n")
    name = input("請輸入姓名\n")
    key_id = CheckKey(int(no), datas)
    data = {"no":int(no), "name":name}
    if(key_id != ''):
        fb.put(table, data=data, name=key_id) #table為路徑，data為要修改的資料，name是KEY
        print("修改完畢")
    else:
        print("並無此章節")
    

    
###主程式 初始化區塊 ###
datas = [{"no":1, "name":"Voy"},
            {"no":2, "name":"fafalina"},
            {"no":3, "name":"Po-Wen"}]

url = RTfirebaseData.url
table = RTfirebaseData.table
fb = firebase.FirebaseApplication(url, None)

