import re 
def Valid(password):
  while(True):   
    if (len(password)<8): 
            flag = -1
            break
    elif(len(password)>12):
            flag=-1
            break
    elif not re.search("[a-z]", password): 
        flag = -1
        break
    elif not re.search("[A-Z]", password): 
        flag = -1
        break
    elif not re.search("[0-9]", password): 
        flag = -1
        break
    elif not re.search("[#@$]", password): 
        flag = -1
        break
    else: 
        flag = 0
    return flag
def main():
    password = input("your password")
    flag = Valid(password)
    if flag==0:
        print("Valid Password") 
    elif not flag ==-1: 
        print("Not a Valid Password")
        main()
main()
