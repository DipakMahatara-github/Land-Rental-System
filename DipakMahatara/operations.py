from write import *
from read import *
import datetime
def rentLand(kitaNo):
    data=readLandFile()
    result=""
    for i in data:
        if i["kita_no"]==kitaNo:
            if i["status"]=="Not Available":
                result="Land isn't availble. "
            else:
                name=input("enter your name: ").lower()
                while True:
                    duration=input("enter duration of loan in months: ")
                    try:
                        duration=int(duration)
                        break
                    except:
                        print("Invalid input")
                updateLandInfo(kitaNo,name,duration,datetime.date.today(),0)
                checkAndUpdateFine(name)
                generateRentInvoice(name,getUser(name),getLand(kitaNo))
                result="Land has been rented out to you"
    if result:
        print(result)
    else:
        print("Invalid Kita no.")
def returnLand(kitaNo):
    data=readLandFile()
    result=""
    for i in data:
        if i["kita_no"]==kitaNo:
            if i["status"]=="Not Available":
                name=input("Enter your name: ").lower()
                if i["customer"]==name:
                    current=checkAndUpdateFine(name)
                    updateLandInfo(kitaNo,"None","None","None",0)
                    generateReturnInvoice(name,getUser(name),current)
                    result="Land is returned"
                else:
                    result="Wrong owner details"
            else:
                result="Land was not rented."
    if result:
        print(result)
    else:
        print("Invalid Kita no.")
def checkAvailablility():
    data=readLandFile()
    print("\n-------------------------------------------------------")
    print("Available lands are: ")
    for i in data:
        if i.get("status")=="Available":
            print(f"Kita no.: {i.get("kita_no")}",end="\t")
            print(f"City: {i.get("city")}",end=("\t"))
            print(f"Direction faced: {i.get("direction")}",end=("\t"))
            print(f"Price: {i.get("price")}",end=("\t"))
            print(f"Availability Status: {i.get("status")}")
    print("\nNot Available lands are: ")
    for i in data:
        if i.get("status")=="Not Available":
            print(f"Kita no.: {i.get("kita_no")}",end=("\t"))
            print(f"City: {i.get("city")}",end=("\t"))
            print(f"Direction faced: {i.get("direction")}",end=("\t"))
            print(f"Price: {i.get("price")}",end=("\t"))
            print(f"Availability Status: {i.get("status")}")
    print("-------------------------------------------------------\n")
def checkAndUpdateFine(name):
    data=readLandFile()
    for i in range(len(data)):
        if data[i]["status"] =="Not Available":
            x=datetime.datetime.now()-datetime.datetime(int(data[i]["date"][0:4]),int(data[i]["date"][5:7]),int(data[i]["date"][8:]))
            daysPassed=x.days-int(data[i]["duration"])*30
            if daysPassed>0:
                fineamount=((daysPassed/30)+1)*int(int(data[i]["price"])*0.1)
                data[i]["fine"]=int(fineamount)
                updateFile("./landInfo.txt",data)
            return data[i]
