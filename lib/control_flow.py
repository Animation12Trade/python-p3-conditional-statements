#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username.lower() == 'admin' and password == '12345':
        return "Access granted"
    else:
        return "Access denied"

print(admin_login("admin", "12345"))  
print(admin_login("ADMIN", "12345"))  
print(admin_login("user", "12345"))   
print(admin_login("admin", "123"))  
    

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


print(hows_the_weather(33))  
print(hows_the_weather(55)) 
print(hows_the_weather(99))  
print(hows_the_weather(75))  
    
     

def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


print(fizzbuzz(0))   
print(fizzbuzz(15))  
print(fizzbuzz(45))  
print(fizzbuzz(3))   
print(fizzbuzz(33))  
print(fizzbuzz(42))  
print(fizzbuzz(5))   
print(fizzbuzz(10))  
print(fizzbuzz(50))  
print(fizzbuzz(2))   
print(fizzbuzz(13))  
print(fizzbuzz(59))  


def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None


print(calculator("+", 1, 2))   
print(calculator("+", 5, 7))   
print(calculator("+", 9, 90))  
print(calculator("-", 1, 2))   
print(calculator("-", 7, 5))   
print(calculator("-", 9, 9))   
print(calculator("*", 1, 2))   
print(calculator("*", 5, 7))   
print(calculator("*", 9, 10))  
print(calculator("/", 1, 1))   
print(calculator("/", 14, 7))  
print(calculator("/", 90, 9))  
print(calculator("?", 90, 9))
    
