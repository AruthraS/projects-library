import winsound #to set alarm sound
from datetime import datetime,time #to work with time
t=input("ENTER TIME IN HH:MM(24 hrs) FORMAT-")
print("ALARM SET.........")
while True:
    n=datetime.now().time()
    k=(str(n))[0:5]
    if k==t:
        break
winsound.Beep(500,60000) #frequency:500, time:60000 milliseconds(1 minute)
