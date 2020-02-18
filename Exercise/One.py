# Create a variable

variable0 = "xxx"

# Create a varibale with the value 1, then other with the value 2, and then other variable with the sum of both

variable1= 1
variable2 = 2
variable3 = variable1 + variable2

# Assing a variable an int, a string, a boolean, a list, a dictionary

varia = 255
varia2 = "Hola bichin"
varia2 = True
varia3 = ["loro", "perro", "gato"]
varia4 = []
varia5 = {"rata":"drogona" ,"perro": "faldero"}
varia6 = {}

# Define a list with the variables varia, varia2

thislist = [varia, varia2]

# Define a dictionary with one key (the variable varia2) and one value (the variable varia)

thisdict = {varia2:varia}

# Define a function that receive two int parameters and returns the sum of both

def my_function(input1 : int, input2 : int) -> int:
    
    return input1 + input2
  
# Define a function that prints in console the word "Hi World"

def my_other_function():
    print ("Hi World!")


# Define a function that receive one string parameter called 'name' and print in console "Hi {name}"

def my_superother_function(name : str):
    
    print("Hi "+ name) 
    
    
    
# Define a Person class that have a Name and Age, include the __init__ method with two parameters to specify the name and age. Then add to it a function that prints in console the name and the age

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

# Bonus:
# Which differences are between a variable and a value
# 1 => value
# var1 => variable
# "hola" => value
# 18 => value
# x => variable
# true => value

# Which values may a variable have?
# str => YES
# int => YES
# boolean => YES
# list => YES
# dictionary => YES
# another variable => YES
# class => YES
  # gloria = Person("Gloria", 50)
  
# Can a variable have one value (string for example) and then change that value for another type (int, boolean, class, etc)?
# YES, for example

gorra = "2"
gorra = int(gorra)

ropa = "3"
ropa = 3


# Can a variable have one string value and then change it to another string value?
# YES, for example

vino = "Toro"
vino = "Uvita"

# Can a string VALUE change it to another string value?
# If it doesn't involve a variable, then it wouldn't be possible. Values are fixed

# Can a string VALUE change it to another value of different type?