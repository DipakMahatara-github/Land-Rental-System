def readLandFile():
    with open(f"./landInfo.txt","r") as fs:
        data=fs.readlines()
    dataArr=[]
    for line in data:
        myArr=line.strip().split(", ")
        newDict={
            "kita_no":myArr[0],
            "city":myArr[1],
            "direction":myArr[2],
            "area":myArr[3],
            "price":myArr[4],
            "status":myArr[5],
            "customer":myArr[6],
            "duration":myArr[7],
            "date":myArr[8],
            "fine":myArr[9]
        }
        dataArr.append(newDict)
    return dataArr

def getLand(kitaNo):
    data=readLandFile()
    for i in data:
        if i["kita_no"]==kitaNo:
            return i
    return None
def getUser(name):
    data=readLandFile()
    myList=[]
    for i in data:
        if i["customer"]==name:
            myList.append(i)
    return myList