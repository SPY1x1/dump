import os
import platform
os.system('clear')
os.system("git pull")
b = platform.architecture()[0]
if b == '64bit':
    __import__("DUMP").Spy()
    
elif b == '32bit':
    __import__("DUMP32").Spy()
    
 
