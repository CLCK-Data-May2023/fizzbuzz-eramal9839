#Write a Python program that prints the numbers from 1 to 100. If the number is dividable by 3 print Fizz, 
#if the number is dividable by 5 print Buzz instead of the number. If the number is dividable by 3 and 5 print FizzBuzz 
#instead of the number.

#want to use "range" function, 

#defining the range 0-101 

for num in range (1,101): #had zero here at first and the first output was "FizzBuzz" , Changed it back to 1 

#if number is divisible by 3 and 5 
# had to use Modulo sign , the / sign only gave me one Fizz for an output  

    if num%3 == 0 and num%5 ==0: 
        print("FizzBuzz")
##if number is divisible by 3 
    elif num%3 ==0:
        print("Fizz")
#if number is divisible by 5        
    elif num%5 == 0:
        print("Buzz")    
#anything else print the number itself      
    else:
        print(num)    

    