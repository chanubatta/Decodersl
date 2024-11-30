import marshal,codecs,binascii,zlib,bz2,pyfiglet,os,time,dis,lzma,gzip,base64
from sys import stdout
import subprocess as sp
import sys,random, base64, getpass, re
from py_compile import compile as _compile
#from cfonts import render, say
import webbrowser
webbrowser.open('https://t.me/KLM_J')
from rich.panel import Panel as nel
from rich import print as cetak
import pyfiglet,requests,subprocess
d = '\x1b[90;1m'
m = '\x1b[91;1m'
h = '\x1b[92;1m'
k = '\x1b[93;1m'
b = '\x1b[94;1m'
j = '\x1b[95;1m'
a = '\x1b[96;1m'
p = '\x1b[97;1m'
A = "\033[1;91m"#الاحمر
B = "\033[1;90m"#الرصاصي
C = "\033[1;97m"#الابيض
E = "\033[1;92m"#الاخضر
H = "\033[1;93m"#الاصفر
K = "\033[1;94m"#البنفسجي
L = "\033[1;95m"#وردي
M = "\033[1;96m"#السمائي
R = '\x1b[1;31m' #احمر 
G = '\x1b[1;32m' #اخضر
B = '\x1b[0;94m' #بنفسجي
Y = '\x1b[1;33m' #اصفر
E = '\033[91m' #احمر
###############
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a16 = '\x1b[38;5;48m'  # أخضر فاتح
M = '\033[2;36m' #سماوي
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a40 = '\x1b[38;5;117m'  # أزرق سماوي
def clr():
	os.system("clear")
def slow(T):
    for r in T + '\n':
        sys.stdout.write(r)
        sys.stdout.flush()
        time.sleep(0.03)
def running(s):
	try:
		for c in s + '\n':
        	    sys.stdout.write(c)
	            sys.stdout.flush()
	            time.sleep(0.001)
	except (KeyboardInterrupt,EOFError):
		print('Exit!')
os.system('clear')
import pyfiglet
import requests
import re
from rich.panel import Panel as Ch
from rich import print as code
a =	'/033[31m'
s =	'/033[32m'
d =    '/033[33m'
g =	'/033[34m'
def PY_97():
	print(a16+'⏕'*28)
	print(a20+' ➲ 1. ɒєcσɒє мαяsнαℓ     ')
	print(a20+' ➲ 2. ɒєcσɒє мαяsнαℓ 3.7    ')
	print(a20+' ➲ 3. ɒєcσɒє вαsє32    ')
	print(a20+' ➲ 4. ɒєcσɒє вαsє64    ')
	print(a20+' ➲ 5. ɒєcσɒє вαsє16    ')
	print(a20+' ➲ 6. ɒєcσɒє вαsє85    ')
	print(a20+' ➲ 7. ɒєcσɒє ℓαмвɒα.мαяsнαℓ.вαsє64.zℓiв    ')
	print(a20+' ➲ 8. ɒєcσɒє ℓαмвɒα    ')
	print(a20+' ➲ 9. ɒєcσɒє ємσji    ')
	print(a20+' ➲ 10. ɒєcσɒє нєx    ')
	print(a20+' ➲ 11. ɒєcσɒє ρyc    ')
	print(a20+' ➲ 12. ɒєcσɒє ℓzмα.zℓiв    ')
	print(a20+' ➲ 13. ɒєcσɒє вiиαscℓℓ    ')
	print(a20+' ➲ 14. ɒєcσɒє zℓiв,вαsє    ')
	print(a20+' ➲ 15. ɒєcσɒє ɢziв    ')
	print(a20+' ➲ 16. ɒєcσɒє cσɒєcs    ')
	print(a20+' ➲ 17. ɒєcσɒє sмρℓє ρyc    ')
	print(a20+' ➲ 18. ɒєcσɒє sмρℓє ρyc2    ')
	print(a20+' ➲ 19. ɒєcσɒє ℓzмα    ')
	print(a20+' ➲ 20. cyτнσи    ')
	print(a20+' ➲ 0. єxєτ    ')
	print(a16+'⏔'*28)
#@U_G_GU
def ahm():
    b = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File marshal : ")
    am = ('\x1b[38;5;51m','\x1b[38;5;63m ','\x1b[38;5;73m2','\x1b[38;5;83m8','\x1b[38;5;93m0','\x1b[38;5;103m0')
    for i in range(50):
        time.sleep(.1)
        sys.stdout.write('\rDecode marshal ...>>> ')
        sys.stdout.flush()
        print('')
    a = open(b).read()
    m = False
    k = ""
    n = 0
    for x in a:
        if x == "'" and a[n-1] == "b":
            m = True
            continue
        if x == "'" and not a[n-1] == "\\":
            break
        if m:
            k = k + a[n+1]
        n += 1
    k += "'"
    k = "b'" + k

    a = f"exec(marshal.loads({k}))"
    exec(a)
 

def unmarszlib():
        try:
            files = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File marshal 3.7: ")
        except:
            exit("")
        if len(files) == 0:
              exit("")
        try:
            bk = open(files,"r").read()
        except IOError:
            print("file tidak ada")
            exit()
        bk = bk.replace("import","import uncompyle6,")
        bk = bk.replace("exec(","uncompyle6.main.decompile(3.7,")
        bk = bk.replace(")))",")),open(\"hasil.py\",\"w\"))")
        exec(bk)
def exit():
        print('الله وياك مع السلامه ')
        sys.exit()
def ex():
        print('الله وياك مع السلامه ')
        sys.exit()
def men():
            
            file=input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("PY_97.py","w").write(data2)            
            os.system("python PY_97.py > PY_97.py")
            PY_97=str(open("PY_97.py","r").read())
            data3=f"""#Decode By  @ZZKGZ\nimport marshal\nexec(marshal.loads({PY_97}))"""
            open("PY_97.py","w").write(data3)
            print("marshal-magic PY_97.py -m normal -o PY_97.py")
            print('')
            print('\n') 
            print('[•] Decode Done √')
            #PY_97()
########################(decode lambda+ emoji)
#PY_97
def lamb():
      print("------------------------------------------")
      file_nme = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File Lambda : ")
      print("------------------------------------------")
      try:
        with open(file_nme, 'r') as file:
              Hussein = file.read()
              NB_JG = Hussein.replace("exec", "print")
        with open(file_nme, 'w') as file:
              file.write(NB_JG)
  
              print("The first step  completed successfully ✅")
              os.system("clear")
              subprocess.run(['python3', f'{file_nme}'])
      #        open("PY_97.py","w").write()
      except FileNotFoundError:
            print("The file was not found. Please select from the list below 👇🏻")
            os.system("ls")
      except Exception as e:
            print(f"Erorr : {e}")


#PY_97
def emoji():
     # print("------------------------------------------")
      file_name = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File emoji: ")
      #print("------------------------------------------")
      try:
        with open(file_name, 'r') as file:
              Hussein = file.read()
              NB_JG = Hussein.replace("exec", "print")
        with open(file_name, 'w') as file:
              file.write(NB_JG)
              
              print("The first step  completed successfully ✅")
              os.system("clear")
              subprocess.run(['python3', f'{file_name}'])
      except FileNotFoundError:
            print("The file was not found. Please select from the list below 👇🏻")
            os.system("ls")
      except Exception as e:
            print(f"Erorr : {e}")
#############(decode base )########################
#PY_97
def decode_base64_file():
    decode_base64 = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File base64:  ")
    #decode_base64_file(decode_base64)
    with open(decode_base64, 'rb') as file:
        encoded_data = file.read()
        decoded_data = base64.b64decode(encoded_data)
        
    with open("Decode_base64.py", 'wb') as file:
          file.write(decoded_data)
          print(" من قبل برو   تم فك تشفير الملف وحفظ النص المفكوك في ملف Decode_base64.")
          #PY_97()
#PY_97
def decode_base16_file():
    decode_base16 = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File base16:  ")
    #decode_base64_file(decode_base64)
    with open(decode_base16, 'rb') as file:
        encoded_data = file.read()
        decoded_data = base64.b16decode(encoded_data)
        
    with open("Decode_base16.py", 'wb') as file:
          file.write(decoded_data)
          print("تم فك تشفير الملف وحفظ النص المفكوك في ملف Decode_base16.py.")
        #  PY_97()
#PY_97        
def decode_base32_file():
    decode_base32 = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File base32:  ")
    #decode_base64_file(decode_base64)
    with open(decode_base32, 'rb') as file:
        encoded_data = file.read()
        decoded_data = base64.b32decode(encoded_data)
        
    with open("Decode_base32.py", 'wb') as file:
          file.write(decoded_data)
          print("تم فك تشفير الملف وحفظ النص المفكوك في ملف Decode_base32.py.") 
         # PY_97()
#PY_97      
def decode_base85_file():
    decode_base85 = input("\x1b[1;31m[\x1b[1;31mPY_97\x1b[1;31m] \033[1;97m> - Enter File base85:  ")
    #decode_base64_file(decode_base64)
    with open(decode_base85, 'rb') as file:
        encoded_data = file.read()
        decoded_data = base64.b85decode(encoded_data)
        
    with open("Decode_base85.py", 'wb') as file:
          file.write(decoded_data)
          print("تم فك تشفير الملف وحفظ النص المفكوك في ملف Decode_base85.py.") 
          #PY_97()
#PY_97             
def decode_hex():
    filename = input("Enter the name of the encoded file: ")
    with open(filename, "rb") as f:
              encoded_data = f.read().hex()
              decoded_data = bytes.fromhex(encoded_data)
              decoded_filename = f"{filename}_decoded.py"
    with open(decoded_filename, "wb") as f:
              f.write(decoded_data)
              print(f"File {filename} decoded successfully and saved as {decoded_filename}")
           #   PY_97()
#PY_97
def lzm_zlb():
#	 #()
	clr()
	while True:
			file = input(a9+'input your file : ')
			filer = input(a12+'output your file : ')
			com = f'marshal-magic {file} -o {filer} '
			os.system(com)
			slow(G+'  by @U_G_GU    *_*')
	else:
			PY_97()
#@PY_97
def zlb():
#	 #()
	clr()
	while True:
			file = input(a9+'input your file : ')
			filer = input(a12+'output your file : ')
			com = f'marshal-magic {file} -o {filer} '
			os.system(com)
			slow(G+'  by @U_G_GU  *_*')
	else:
			PY_97()
#PY_97
def lzm():
#	 #()
	clr()
	while True:
			file = input(a9+'input your file : ')
			filer = input(a12+'output your file : ')
			com = f'marshal-magic {file} -o {filer} '
			os.system(com)
			slow(G+'  by @U_G_GU  *_*')
	else:
	      PY_97()
#PY_97
def cods():
#	 #()
	clr()
	while True:
			file = input(a9+'input your file : ')
			filer = input(a12+'output your file : ')
			com = f'marshal-magic {file} -o {filer} '
			os.system(com)
			slow(G+'  by @U_G_GU   *_*')
	else:
			
			PY_97()
#PY_97
def binasci():
#	 #()
	clr()
	while True:
			file = input(a9+'input your file : ')
			filer = input(a12+'output your file : ')
			com = f'marshal-magic {file} -o {filer} '
			os.system(com)
			slow(G+'  by @U_G_GU  *_*')
	else:
			PY_97()
#PY_97
def gzp_base():
#
	clr()
	while True:
			file = input(a9+'input your file : ')
			filer = input(a12+'output your file : ')
			com = f'marshal-magic {file} -o {filer} '
			os.system(com)
			slow(G+'  by @U_G_GU  *_*')
	else:
			PY_97()
#PY_97			
def zlib_base():
#	 #()
	clr()
	while True:
			file = input(a9+'input your file : ')
			filer = input(a12+'output your file : ')
			com = f'marshal-magic {file} -o {filer} '
			os.system(com)
			slow(G+'  by @U_G_GU   *_*')
	else:
			PY_97()
#PY_97
def smple_pyc():
#		 #()
		clr()
		while True:
			Ty = input(a9+'input your file : ')
			Tr = input(a12+'output your file : ')
			com = f'pycdc {Ty} > {Tr}'
			os.system(com)
			slow(G+'  by @U_G_GU  *_*')
		else:
			PY_97()
#PY_97	
def smple_pyc2():
#		 #()
		clr()
		while True:
			Ty = input('input your file : ')
			Tr = input('output your file : ')
			com = f'uncompyle6 {Ty} > {Tr}'
			os.system('uncompyle6 {Ty} > {Tr}')
			slow('  by @U_G_GU  *_*')
		else:
			PY_97()
#PY_97
def gzp():
#	 #()
	clr()
	while True:
			file = input(a9+'input your file : ')
			filer = input(a12+'output your file : ')
			com = f'marshal-magic {file} -o {filer} '
			os.system(com)
			slow(G+'  by @U_G_GU  *_*')
	else:
			PY_97()
#PY_97
def cython():
	webbrowser.open('https://t.me/PY_97')
	lzm()
print(f'''{a5}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀
　　⡠⠚⠁　⣀⡠⠒⠚⡄⠑　⠈⠳⡄⠀⠀⠀
　⢀⡞⠁⠠⠦　　　⠸⠠⠀　⢀⠤⠜⣆⠀⠀
⢀⡎　　⠡⡀　⠐⠂　⠈　　⣁⠀⣀⣸⡆⠀
⢸⠀⡤⡀　⡧　　　⠠⠤　⠨　　　⢧⠀
⠀⢧　⠈⢀⠆⣤⣤⣶⣶⣦⣤⠁⢀⠔⣢⣴⣶⢨⠇
　⠘⡆⡄　 ⣿⣿⣿🔥⣿⣿⡆　⣼⣿🔥⣿⡏⠀
　　⢻⠀⠇　⠙⢿⣿⣿⡿⢿⠁ ⠻⠿⠿⢿⡅⠀
⠀⠀⢈⡷⢼⠈⢈⣀⠠　⠐⠊⢀⣾⡟⣦⠤⠼⠁⠀
　　⠘⣆⠅⣽⠉⠘⡆⠆　⢀⠛⠓⡁⢻⠀⠀⠀⠀
　　　⢺⠐⠙⢦⢀⡧⣈⣘⣈⣀⣢⣣⣾⠀⠀⠀⠀
　　　⠈⠳⢌⠈⠛⢷⣓⡜⢤⠧⡗⣿⡇⠀⠀⠀⠀
　　　　　⠳⣄⠀⠀⠉⠍⠉⡀⡞⠀⠀⠀⠀⠀
　　　　　　⠉⠑⠲⠤⠴⠚⠁⠀⠀⠀⠀⠀⠀⠀
''')
PY_97()				
se = int(input(" > cнσσsє : "))
if se == 1:
	ahm()
elif se == 2:
	unmarszlib()
elif se == 3:
      decode_base64_file()
elif se == 4:
	decode_base32_file()
elif se == 5:
	decode_base16_file()
elif se == 6:
	decode_base85_file()
elif se == 7:
	men()
elif se == 8:
	lamb()
elif se == 9:
	emoji()
elif se == 10:
       decode_hex()
elif se == 11:
      ex()
elif se == 12:
      lzm_zlb()
elif se == 13:
	binasci()
elif se == 14:
	zlib_base()
elif se == 15:
	gzp()
elif se == 16:
	cods()
elif se == 17:
	smple_pyc()
elif se == 18:
	smple_pyc2()
elif se == 19:
       lzm()
elif se == 20:
       cython()
elif se == 0:
	exit()
#PY_97()		
if __name__ == "__main__":
	U_G_GU()