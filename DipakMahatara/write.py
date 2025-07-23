import datetime
from read import *
def updateFile(filename,content):
    with open(f"./{filename}","w") as fs:
        for i in content:
            value=[]
            for val in list(i.values()):
                value.append(str(val))
            fs.write(", ".join(value)+"\n")
def generateRentInvoice(name,data,land):
    with open(f"./{name}'s_rent_invoice_of_land_{land["kita_no"]}.txt","w") as fs:
        fs.write("TechnoPropertyNepal Pvt. ltd.")
        fs.write("\nKathmandu, Nepal")
        fs.write("\ntechnopropertynepal@gmail.com\n\n")
        fs.write("Rental Invoice\n\n")
        fs.write(f"Invoice date: {datetime.date.today()}")
        fs.write("\nTo,\n")
        fs.write(f"Mr/Mrs {name.capitalize()}\n\n")
        fs.write("Info of rented land: \n")
        fs.write(f"\tLand Kita no.: {land["kita_no"]}\n")
        fs.write(f"\tLocation: {land["city"]}\n")
        fs.write(f"\tDirection: {land["direction"]}\n")
        fs.write(f"\tArea: {land["area"]}\n")
        fs.write(f"\tPrice: {land["price"]}\n")
        fs.write(f"\tDuration: {land["duration"]}\n")
        fs.write(f"\tTotal Price: {int(land["price"])*int(land["duration"])}\n\n")
        fs.write("Description of user's rented lands:\n")
        totalamount=0
        for i in range(len(data)):
            fs.write(f"{i+1}. Land's Kita no.: {data[i]["kita_no"]}\n")
            fs.write(f"\tLocation: {data[i]["city"]}\n")
            fs.write(f"\tDirection of land: {data[i]["direction"]}\n")
            fs.write(f"\tLand's area in ana: {data[i]["area"]}\n")
            fs.write(f"\tDuration of loan in days: {data[i]["duration"]}\n")
            fs.write(f"\tPrice of land: Rs{data[i]["price"]}\n")

            fs.write(f"\tTotal Price: {int(land["price"])*int(land["duration"])}\n")

            fs.write(f"\tFine charged: Rs{data[i]["fine"]}\n\n")
            totalamount+=int(data[i]["price"])*int(data[i]["duration"])+int(data[i]["fine"])
        fs.write(f"Total Amount due: Rs{totalamount}")
def generateReturnInvoice(name,data,land):
    with open(f"./{name}'s_return_invoice_of_land_{land["kita_no"]}.txt","w") as fs:
        fs.write("TechnoPropertyNepal Pvt. ltd.")
        fs.write("\nKathmandu, Nepal")
        fs.write("\ntechnopropertynepal@gmail.com\n\n")
        fs.write("Rental Return Invoice\n\n")
        fs.write(f"Invoice date: {datetime.date.today()}")
        fs.write("\nTo,\n")
        fs.write(f"Mr/Mrs {name.capitalize()}\n\n")
        fs.write("Info of returned land: \n")
        fs.write(f"\tLand Kita no.: {land["kita_no"]}\n")
        fs.write(f"\tLocation: {land["city"]}\n")
        fs.write(f"\tDirection: {land["direction"]}\n")
        fs.write(f"\tArea: {land["area"]}\n")
        fs.write(f"\tPrice: {land["price"]}\n")
        print(land)
        fs.write(f"\tTotal Price of land: Rs{int(land["price"])*int(land["duration"])}\n")
        fs.write(f"\tfine charged: {land["fine"]}\n")
        fs.write(f"\tTotal Amount Paid: {int(land["price"])*int(data[i]["duration"])+int(land["fine"])}\n\n")
        fs.write("Description of user's rented lands:\n")
        totalamount=0
        if not data:
            fs.write("\tNo remaining loan\n")
        for i in range(len(data)):
            fs.write(f"{i+1}. Land's Kita no.: {data[i]["kita_no"]}\n")
            fs.write(f"\tLocation: {data[i]["city"]}\n")
            fs.write(f"\tDirection of land: {data[i]["direction"]}\n")
            fs.write(f"\tLand's area in ana: {data[i]["area"]}\n")
            fs.write(f"\tDuration of loan in days: {data[i]["duration"]}\n")
            fs.write(f"\tPrice of land: Rs{data[i]["price"]}\n")
            fs.write(f"\tTotal Price of land: Rs{int(data[i]["price"])*int(data[i]["duration"])}\n")
            fs.write(f"\tFine charged: Rs{data[i]["fine"]}\n")
            totalamount+=int(data[i]["price"])*int(data[i]["price"])+int(data[i]["fine"])

        fs.write(f"Total Amount due: Rs{totalamount}")
def updateLandInfo(kitaNo,customer,duration,date,fine):
    data=readLandFile()
    for i in range(len(data)):
        if data[i]["kita_no"]==kitaNo:
            if data[i]["status"]=="Available":
                data[i]["status"]="Not Available"
            else:
                data[i]["status"]="Available"
            data[i]["customer"]=customer
            data[i]["duration"]=duration
            data[i]["date"]=date
            data[i]["fine"]=fine
    updateFile("landInfo.txt",data)