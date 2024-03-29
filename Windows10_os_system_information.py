import os

if os.path.isdir('C:/test') == False:
    os.mkdir('C:/test')

print("Sytem information from systeminfo cmd")
os.system('echo "Sytem information from systeminfo cmd" > C:/test/test.txt')
os.system('systeminfo >> C:/test/test.txt')

print("\nHere are all your IP addresses + mac addresses")
os.system('echo "Here are all your IP addresses + mac addresses >> C:/test/test.txt')
os.system('ipconfig /a >> C:/test/test.txt')

print("\nCan you reach Google?")
os.system('echo "Can you reach Google?" >> C:/test/test.txt')
os.system('Ping 8.8.8.8 >> C:/test/test.txt')

print("\nHere is the all the open network connections you have and the port #s.")
os.system('echo "Here is the all the open network connections you have and the port #s:" >> C:/test/test.txt')
os.system('netstat -n >> C:/test/test.txt')

print("\nHere is your routing information")
os.system('echo "Here is your routing information" >> C:/test/test.txt')
os.system('netstat -r >> C:/test/test.txt')

print("\nHere is Hard drive information including your serial numbers")
os.system('echo "Here is Hard drive information including your serial numbers" >> C:/test/test.txt')
os.system('wmic diskdrive get Name, Manufacturer, Model, InterfaceType, MediaType, SerialNumber. >> C:/test/test.txt')

print("\nHere is CPU information")
os.system('echo "Here is CPU information" >> C:/test/test.txt')
os.system('wmic cpu list full >> C:/test/test.txt')

print("\nHere is your GPU information")
os.system('echo "Here is your GPU information" >> C:/test/test.txt')
os.system('wmic path win32_VideoController get name >> C:/test/test.txt')

print("\nHere is your motherboard information")
os.system('echo "Here is your motherboard information" >> C:/test/test.txt')
os.system('wmic baseboard >> C:/test/test.txt')

print("\nHere is your driver information")
os.system('echo "Here is your driver information" >> C:/test/test.txt')
os.system('driverquery -v >> C:/test/test.txt')

print("\nHere are the programs your running")
os.system('echo "Here are the programs your running" >> C:/test/test.txt')
os.system('tasklist >> C:/test/test.txt')

print("\nWhat user is logged in?")
os.system('echo "What user is logged in?" >> C:/test/test.txt')
os.system('whoami >> C:/test/test.txt')

print("\nWhat does the system's clock say?")
os.system('echo "What does the systems clock say?" >> C:/test/test.txt')
os.system('echo=%DATE% >> C:/test/test.txt')

os.system('dxdiag -x C:/test/dxdiag')

print("Everything has been outputted to C:/test/test.txt, please either give this to your IT professional or read the outputted file to fix your issue")
print("Please see test.txt + dxdiag.xml")


#This was supposed to give your office version # but it does not work in python but it works in the CMD
#os.system('powershell.exe [reg query "HKEY_CLASSES_ROOT\Word.Application\CurVer"]') #got close but having issues but any powershell command is os.system('powershell.exe [command]')

#This I might erase it halts the time it takes you have to close the popup to proceed further. It is also in the "systeminfo" cmd
#print("Pop up window will present you with your Windows system version #")
#os.system('winver')
