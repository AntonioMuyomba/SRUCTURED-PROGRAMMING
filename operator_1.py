# number1=int(input("enter the first number: "))
# number2=int(input("enter the second number: "))

# #Addition
# sum=number1 + number2
# print(sum)

# number1=8
# number2=5

# #Subtraction
# difference=number1 - number2
# print(difference)

# number1=8
# number2=4

# #Multiplication
# product=number1 * number2
# print(product)

# number1=8
# number2=4

# #Division
# quotient=number1 / number2
# print(quotient)

# #Modulus
# modulus=number1 % number2

# #concatenation
# print(f"the first number is {number1} and the second number is {number2}")

# first_name=input("enter your first name: ")
# last_name=input("enter your last name: ")

# name = "Antonio"
# print(name)

#    if statment
# test1 = eval(input('enter score in test-I: '))
# test2 = eval(input('enter score in test-II: '))
# test3 = eval(input('enter score in test-III: '))
# avgteprint("average score is: ", avg)
# 80
# avg = (test1 + test2 + test3 + test4 + test5) / 5
# print("average score is: ", avg)
# if avg >= 80:
#     print("you are an outstanding student.")
# if avg >= 70 and avg < 80:
#     print("you are a good student.")    
# if avg >= 60 and avg < 70:
#     print("you are an average student.")   
# if avg >= 50 and avg < 60:
#     print("you are a below average student.")
#     if avg >= 40 and avg < 50:
#      print("you are a poor student.")
# if avg < 40:
#      print("you need extra ordinary effort to improve.")               
#   if nested
# a=int(input("Enter a number: "))  
# b=int(input("Enter another number: "))
# c=int(input("Enter another number: "))

# if(a>=b):
#     if(a>=c):
#         greatest=a
#     else:
#         greatest=c
# else:
#     if(b>=c):
#         greatest=b
#     else:
#         greatest=c

# print(str(greatest)+'is the greatest.')

    #   elif statment
# if(avg>=80):
#     print("you are an outstanding student.")
# elif(avg>=70):
#     print("you are a good student.")    
# elif(avg>=60): 
#     print("you are an average student.")    
# elif(avg>=50):
#     print("you are a below average student.")
# elif(avg>=40):
#     print("you are a poor student.") 

s1,s2,s3,s4,s5=eval(input('enter your scores: '))
avg=(s1+s2+s3+s4+s5)/5  
print('average of the five scores is: ' + str(avg))  

if(avg>=80):
    print("you are an outstanding student.")
else:
    if(avg>=70):
        print("you are a good student.")
    else:
        if(avg>=60):
            print("you are an average student.")
        else:
            if(avg>=50):
                print("you are a below average student.")
            else:
                if(avg>=40):
                    print("you are a poor student.")
                else:
                    print("you need extra ordinary effort to improve.") 