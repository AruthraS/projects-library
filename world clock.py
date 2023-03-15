import pytz
from datetime import datetime
def display():
    print("MENU 1:-")
    print("1.Africa\n2.America\n3.America/Argentenia\n4.America/Indiana\n5.America/Kentucky\nAmerica/North_Dakota\n6.Antartica\n7.Arctic\n8.Asia")
    print("9.Atlantic\n10.Australia\n11.Brazil\n12.CET\n13.CST6CDT\n14.Canada\n15.Chile\n16.Cuba\n17.EET\n18.EST\n19.ESTSEDT\n20.Egypt\n21.Eire")
    print("22.Etc/GMT\n23.Europe24.GB\n25.Greenwich\n26.HST\n27.Hongkong\n28.Iceland\n29.Indian\n30.Iran\n31.Israel\n32.Jamaica\n33.Japan\n34.Kwajalein")
    print("35.Libya\n36.MET\n37.MST\n38.Mexico\n39.NZ\n40.Navajo\n41.PRC\n42.PST8PDT\n43.Poland\n44.Portugal\n45.ROC\n46.ROK\n47.Singapore\n48.Turkey\n49.UCT\n50.US\n51.UTC\n52.Universal\n53.W-SU\n54.WET\n55.Zulu")
def disp1():
    print("CHOOSE THE REGION FROM THE MENU 1")
    x=input("ENTER THE REGION :")
    return x
def disp(x):
    p=pytz.all_timezones
    print("MENU 2:-")
    for i in p:
        if i.startswith(x):
            print(i)
        elif x[0]<i[0]:
            break
    print("CHOOSE THE REGION FROM THE MENU 2")
    y=input("ENTER THE REGION :")
    return y
def operation(y):
    x=pytz.timezone(y)
    a=(str(datetime.now(x).time()))[0:9]
    return a
i=0
display()
while True:
    if i==1:
        i=int(input("NEEDED RESTART?(1:YES,2:NO):"))
    if i==2:
        break
    else:
        q=disp1()
        w=disp(q)
        e=operation(w)
        print("TIME IN ",w," is ",e)
    i=1
