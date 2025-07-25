import os
menu = """
 __    __     ______     __   __     __  __    
/\ "-./  \   /\  ___\   /\ "-.\ \   /\ \/\ \   
\ \ \-./\ \  \ \  __\   \ \ \-.  \  \ \ \_\ \  
 \ \_\ \ \_\  \ \_____\  \ \_\\"\_\  \ \_____\ 
  \/_/  \/_/   \/_____/   \/_/ \/_/   \/_____/ 
                                               
"""
print(menu)
fold = """
[1]-load_api
[2]-exit

"""
print(fold)
select = int(input("=>"))
if select == 1:
	os.system("clear")
	os.system("python load.py")
else:
	os.system("quit()")
