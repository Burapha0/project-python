while True:
    kg=float(input("น้ำหนัก(kg.) : "))#ให้ผู้ใช้กรอกข้อมูลเป็นเลขทศนิยม
    cm=float(input("ส่วนสูง(cm.) : "))
    m=cm/100.00#นำตัวแปร cm มาหาร 100 แล้วเก็บไว้ในตัวแปร m
    bmi=kg/(m*m)#หาค่า BMI
    print("BMI = ",bmi)#สั่งปริ้นค่า bmi
    if bmi < 18.50:
        f = open("thin.txt","r",encoding="ANSI")#สั่งให้อ่านข้อมูลใน text file ชื่อ thin แล้วเก็บไว้ในตัวแปล f
        print(f.read()) #แสดงข้อมูล ของ file text
        f.close()#สั่งให้file text ปิดการใช้งาน
    elif bmi >= 18.50 and bmi <= 22.90 :
        f = open("normal.txt","r",encoding="ANSI")
        print(f.read())
        f.close()
    elif bmi > 22.90 :
        f = open("fat.txt","r",encoding="ANSI")
        print(f.read())
        f.close()
    else :
        print("ERROR...")
    stop = input("ต้องการทำรายการต่อหรือไม่ (Y/N) : ")
    if stop.upper() == "N":
        print("จบการทำงาน")
        break
