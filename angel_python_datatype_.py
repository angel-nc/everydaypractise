
#This is a code for printing a round number and a string message
"""
x=6.9
y=9.373
result=x+y
message="I am doing python for the first time.\n\
I guess it would be an amazing journey for me and a great incentive to boost myself"
print message
print round(result,2)



#This is a code for printing a concatenated string message
message='angel'+'QA'
message2='<'+ message*6 + '>'
print message2



# This ia code for returning many positions
message='angel'+'test'
message2= message[0:3]+message[3:6]
message3="Is is greater or equal", 3>2
print message2
print message3



#this code is taking input on run time
age= raw_input("how old are you")
weight=raw_input("how much do you weight")
height=raw_input("how much are you tall")
print "so you are %r old, %r heavy and %r tall"%(age,weight,height)



# this is a code where we can assign the argvs of command line into different variables. For example if you type angel
# angel will be assigned to variable first just after the file name of your project

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "arguments are: ", argv



# This is a code for reading a file and writing something to the file
from sys import argv
project_name, filename=argv
file_name=open(filename)

print "Here is your file %s:"%file_name
print file_name.read()
print("Open the file again:")
file_name_2=raw_input('>')
file_name_3=open(file_name_2,'w')
print "Write something to your file:"
first_line=raw_input("Enter some thing:")
second_line=raw_input("Enter something:")
print("Now I am going to write the typed things to my file ")
print file_name_3.write(first_line)
print file_name_3.write("\n")
print file_name_3.write(second_line)
print("Finally I am closing the file")
file_name_3.close()




#This ia code for reading one file and copying the content to another file
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
in_data = in_file.read()
print in_data
print "The input file is %d bytes long" % len(in_data)

print "Does the output file exist? %s" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print "Alright, all done."

out_file.close()
in_file.close()




# This is a code for starting with function
# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()



# this is a mathematical operation using function and loop

def avg(*angel):
    total=0
    for  result in angel:
       total+=result
    return total/ len(angel)




#Here starts the basic functional programs
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)



# This is the function of adding two numbers using raw input
def I_want_to_add(number_1,number_2):
    print "The result of summation is: %d"%(int(number_1)+int(number_2))

print "Enter two numbers:"
First_number=raw_input("Enter your first number:")
second_number=raw_input("Enter your second number:")
I_want_to_add(First_number,second_number)

#This is a function of multiplying two numbers
def I_want_to_multiply(number_1,number_2):
   result=int (number_1)* int (number_2)
   print "The result of multiplication is: %d"%(result)

First_number=20
Second_number=30
I_want_to_multiply(First_number,Second_number)

#This is a function of dividing numbers
def I_want_to_divide(number_1,number_2):
    print"The result is %d / %d"%(number_1,number_2)
    return number_1/number_2

result=I_want_to_divide(4,2)
print result



#This is a if else condition that prints several output based on logic
people = 30
cars = 40
buses = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."





# this is a summation  code using for loop and function
def add_adn_average(*numbers):
    sum=0
    average = 0
    for number in numbers:
        sum+=number
    return [sum, sum/len(numbers)]

result, average = add_adn_average(1,2,3,4,5)
print "The result is %d and %d"/n%(result, average)


# This is a code for summation using raw input
def add(*numbers):
    sum=0
    for number in numbers:
        sum+=int(number)
    return sum

message_1=raw_input("Enter numbers:")
number_1=raw_input("Your first number:")
number_2=raw_input("Your second number:")
number_3=raw_input("Your third number:")

result=add(number_1,number_2,number_3)
print"The result is %d"%(result)



# In this code we have declared an empty array then appended some elements in the list, then took some raw inputs added the raw inputs
# in the element, added and averaged and then printed
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i
while elements != '':
    try:
        extra_number=int(raw_input("Enter number:"))
        elements.append(extra_number)
    except:
        break

def add_and_avg(elements):
    sum=0
    average=0
    for number in elements:
        sum+=(number)
    return [sum, sum/len(elements)]
result,average=add_and_avg(elements)

print "The sum and average results are: %d %d"%(result,average)


#The string converted into items in the list
number_as_string= "1 2 3 4 5 6 7"
print"Let's do some string manipulation"

number_as_string2= number_as_string.split(' ')
List1=["10","20","30","40"]

print"The length of the list1 is: %d"%len(List1)
while len(number_as_string2)!=9:
    List2=List1.pop()
    print"Adding next item to the number_as_string now:",List2
    number_as_string2.append(List2)
    print"There are %d items now in the list: "%len(number_as_string2)
print"The list goes like this now",number_as_string2
print number_as_string2[2]
print number_as_string2[-1]
print number_as_string2.pop(-1)
print "?".join(number_as_string2[2:4])


# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state,abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])



Employeeinfo={'Angel':{'Name':'Afrig Angel','Age':'27','Occupation':'SQA Eng'},'Reshad':{'Name':'Resahad Raihan','Age':'29','Occupation':'SQA Eng'}}
for key, value in Employeeinfo.items():
    print"Show me the employee info: %s\n %s"%(key,value)

information1=Employeeinfo.get('Angel')
print "I want to show single info:",information1

information2=Employeeinfo.get('XYZ','This is not a valid attribute')
print "If not valid then print this message:",information2


professionalinfo= {'Name':'Angel',
     'Age':  '27',
     'Occupation': 'SQA',
     'yearsofexp':'3'

}

personalinfo= {'Home-residence':'uttara',
               'sector':'13',
               'road':'4',
               'house':'36'}

for key,value in professionalinfo.items():
    print "give me your professional info:",(key,value)


print "Angel who is %s years old who lives in %s" %(professionalinfo['Age'], personalinfo['Home-residence']
)

"""

import my_tax_calculator_program

print my_tax_calculator_program.allowable_expense
print my_tax_calculator_program.calculate_tax_on_taxable_amount(400000)


