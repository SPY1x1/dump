import os
import platform
os.system('clear')
os.system("git pull")
b = platform.architecture()[0]
if b == '64bit':
    __import__("VIP").Spy()
    
elif b == '32bit':
    print(" your phone is 32 bit \n 32 bit comming soon")
 
