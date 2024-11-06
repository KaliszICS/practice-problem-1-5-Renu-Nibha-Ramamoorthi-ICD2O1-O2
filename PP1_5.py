
def q1():
  #Write Assignment code here
  num = input("Input an integer: ") 
  num = int(num) 
  num += 3 
  print(num) 
def q2():
  #Write Assignment code here
  num = input("Input a number: ") 
  num = float(num + "4") 
  num += 2 
  print(num) 
def q3():
  #Write Assignment code here
  radius = input("Input a radius: ") 
  radius = float(radius) 
  area = 3.14 * radius * radius 
  print("The area of the circles is:", area) 
def q4():
  #Write Assignment code here
  num = input("Input a number: ") 
  num = float(num) 
  num * = 12 
  num = math.floor(num)
  print(num) 
def q5():
  #Write Assignment code here
  num = input("Input an integer: ")
  num = int(num)
  num += 5 
  print("Your number + 5 is {}".format(num)) 
              
#Comment this code out when running tests
#Do not comment this out when running your program normally

q1()
q2()
q3()
q4()
q5()
