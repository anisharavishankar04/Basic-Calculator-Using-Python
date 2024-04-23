def add(a,b):
  answer=a+b
  print(a,"+",b,"=",answer)

def sub(a,b):
  answer=a-b
  print(a,"-",b,"=",answer)

def mul(a,b):
  answer=a*b
  print(a,"*",b,"=",answer)

def div(a,b):
  answer=a/b
  print(a,"/",b,"=",answer)



while choice!='e' or choice!='E':
  
  print("A. Addition\nB. Subtraction\nC. Multiplication\nD. Division\nE. Exit")
  choice=input("Enter your choice: ")
  
  if choice=='A' or choice=='a':
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    add(a,b)
  
  elif choice=='b' or choice=='B':
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    sub(a,b)
  
  elif choice=='c' or choice=='C':
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    mul(a,b)
  
  elif choice=='c' or choice=='C':
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    div(a,b)
  
  elif choice=='e' or choice=='E':
    print("The program has been terminated.")
    quit()


