#! python3
# \t denotes a tab
print("Addition:\t", "5 + 2 =", 5 + 2)
print("Subtraction:\t", "5 - 2 =", 5 - 2)
print("Multiplication:\t", "5 * 2 =", 5 * 2)
print("Exponent:\t", "5 ** 2 =", 5 ** 2)
print("Division:\t", "5 / 2 =", 5 / 2)
print("Floor division:\t", "5 // 2 =", 5 // 2)
print("Modulo:\t\t", "5 % 2 =", 5 % 2)
print ()

print()
# When performing mathematical calculations in Python, you may make use of variables and brackets in the same way you would when performing a mathematical calculation in the real world.
a = 5
b = 2
c = (a + 5) / (b * 5)
print(c)
print ()

print()
# The following examples demonstrate the various shorthand assignment operators available in Python, as well as their equivalent (normal) mathematical operation.

a = 5
a += 2 # Equivalent to a = a + 2
print("Add and assign +=:\t\t\t", "a += 2 \t", "results in a =", a)

#print()
a = 5
a -= 2 # Equivalent to a = a – 2
print("Subtract and assign -=:\t\t", "a -= 2 \t", "results in a =", a)

#print()
a = 5
a *= 2 # Equivalent to a = a * 2
print("Multiply and assign *=:\t\t", "a *= 2 \t", "results in a =", a)

#print()
a = 5
a **= 2 # Equivalent to a = a ** 2
print("Power of and assign **=:\t", "a **= 2\t","results in a =", a)

#print()
a = 5
a /= 2 # Equivalent to a = a / 2
print("Divide and assign /=:\t\t", "a /= 2 \t","results in a =", a)

#print()
a = 5
a //= 2 # Equivalent to a = a // 2
print("Floor and assign //=:\t\t", "a //= 2\t","results in a =", a)

#print()
a = 5
a %= 2 # Equivalent to a = a % 2
print("Modulo and assign %=:\t\t", "a %= 2 \t","results in a =", a)
print ()

#print()
#The following examples demonstrate the various comparison operators available in Python. All comparison operators return a value of True or False. These operators are sometimes known as Boolean operators, since True and False are known as Boolean values.
#The equality operator == checks if 2 values are equal.
print()
print("5 == 2\t", "results in\t", 5 == 2)

#print()
# The inequality operator != checks if 2 values are not equal.
print("5 != 2\t", "results in\t", 5 != 2)

#print()
# The greater than operator > checks if the first value is greater than the second.
print("5 > 2\t", "results in\t", 5 > 2)

#print()
# The less / smaller than operator < checks if the first value is less than the second.
print("5 < 2\t", "results in\t", 5 < 2)

#print()
# The greater than or equal to operator >= checks if the first value is greater than or equal to the second.
print("5 >= 2\t", "results in\t", 5 >= 2)

#print()
# The less / smaller than or equal to operator <= checks if the first value is less than or equal to the second.
print("5 <= 2\t", "results in\t", 5 <= 2)
print ()

#print()
#For character / string values, the ASCII values of the operands are compared.  This means that “1” and “2” as strings are not compared as numeric values.
print("'2' == 'a'\t", "results in\t", '2' == 'a')
print("'2' != 'a'\t", "results in\t", '2' != 'a')
print("'2' > 'a'\t", "results in\t", '2' > 'a')
print("'2' < 'a'\t", "results in\t", '2' < 'a')
print("'2' >= 'a'\t", "results in\t", '2' >= 'a')
print("'2' <= 'a'\t", "results in\t", '2' <= 'a')
print ()

#print()
#The opposite of true is false, but false is also the equivalent of NOT true. In Python, the NOT operator is used to invert a Boolean value, i.e. NOT true is false and NOT false is true. Python uses not as its NOT operator.
a = True
b = False
print("NOT a:", "not a results in", not a)
print("NOT b:", "not b results in", not b)
print ()

#print()
# Am I hungry? Is there ice cream in the freezer? Only if both of the questions above result in an answer of yes (True) can you possibly choose to eat ice cream. If either or both of the questions results in a no answer, you won't be eating ice cream. In Python, we can string decision options together like this by using the and operator. The operation is referred to as the logical AND. When performing an AND, the result can only ever be True if both input decisions result in a True. If any of the inputs are False, the entire operation will result in False. This is demonstrated in the following code segment.
# In theory
print("True and True =", True and True)
print("True and False =", True and False)
print("False and True =", False and True)
print("False and False =", False and False)
print()

#print()
# In practice
print("(5 > 2) and (3 > 2) =", (5 > 2) and (3 > 2))
print("(5 > 2) and (3 < 2) =", (5 > 2) and (3 < 2))
print("(5 < 2) and (3 > 2) =", (5 < 2) and (3 > 2))
print("(5 < 2) and (3 < 2) =", (5 < 2) and (3 < 2))
print()

#print()
#In some complex decisions all contributing factors do not need to be True; only one of the contributing factors needs to be True. Say for example you want to buy a new game as a gift. In this example, you don't really mind which one you buy (Game 1 or Game 2), as long as one of them is available. Does the store have stock of Game 1? Does the store have stock of Game 2?
#So in this instance, your decision is not based on an AND. It will be based on the logical operator OR. In Python, or is used as the OR operator. For the or operator to result in True only one of the factors needs to result in True for the overall result to be True. The only time a decision will result in False is if both contributing decisions result in False, i.e. the store does not have stock of Game 1 or Game 2. The various True and False combinations are demonstrated in the following code segment.
# In theory
print("True or True =", True or True)
print("True or False =", True or False)
print("False or True =", False or True)
print("False or False =", False or False)
print()

#print()
# In practice
print("(5 > 2) or (3 > 2) =", (5 > 2) or (3 > 2))
print("(5 > 2) or (3 < 2) =", (5 > 2) or (3 < 2))
print("(5 < 2) or (3 > 2) =", (5 < 2) or (3 > 2))
print("(5 < 2) or (3 < 2) =", (5 < 2) or (3 < 2))
print()

#print()
#In programming, a structure that is able to evaluate a given statement and take a different course of action depending on the result, is referred to as a control structure. The most basic control structure in most programming languages is based on the if statement. The basic structure of an if statement is as follows:
#if statement to be evaluated:
#Block of code:  Action to take when the evaluation results in True
#print()
print()
#The indent in the previous example is very important. Look at the difference in output generated from the following code segment.
a = 5
b = 2

if a * b > 9:  # Note that the if statement ends in :
    print("a * b (", a * b, ") is greater than 9") # Note the indent at the beginning of the line
print()
print()

# print()
a = 5
b = 2
print("The if evaluates to true and the second line is indented:")
if a * b > 9:
    print("a * b (", a * b, ") is greater than 9")
    print("This should only print on True")

print()

print("The if evaluates to false and the second line is indented:")
if a * b < 9:
    print("a * b (", a * b, ") is greater than 9")
    print("This should only print on True")

print()

print("The if evaluates to true and the second line is not indented:")
if a * b > 9:
    print("a * b (", a * b, ") is greater than 9")
print("This should only print on True")

print()

print("The if evaluates to false and the second line is not indented")
if a * b < 9:
    print("a * b (", a * b, ") is greater than 9")
print("This should only print on True")
print()

#print()
#As you can see in the above examples, when indented in the same way as the first line of the if block of code, the second line is only displayed when the if evaluates to True. In the examples where the second line is not indented, it is not seen as part of the if statement so it is always displayed. Remember that indents are used in Python to group blocks of code.
#print()

print()
#From the examples we've seen so far, actions were taken only when the if statement evaluates to true, but what if we wanted to take an alternative course of action when the result is True? Say for instance you are driving down the highway and need to make a decision on whether to stop in order to refill your car's fuel.
fuel = 10

if fuel > 10:
    print("Keep on driving.")
else:
    print("Stop to refuel.")

#print()
#This example made use of an else statement. In most programming languages an else is used to define what action should be taken if the if statement evaluates to False. But what if we wanted to perform another test after the first one? In other words, we'd test a first condition. If that one evaluates to False we test another condition. If that then evaluates to False, we test another. We can go on like this as long as we have options for which to test. In Python, we make use of the elif structure to facilitate this functionality.
print()

#print()
fuel = 15

if fuel > 20:
    print("Drive fast.")
elif fuel > 10:
    print("Drive slow.")
else:
    print("Stop to refuel.")
print()

#print()
#We can, however, write the same code by using only if and else statements. It's up to you which syntax makes you feel most comfortable. Programming languages such as C++, C# and Java only employ the if-else structure and not the if-elif-else structure. Note the indentations in the if-else example below.
fuel = 15

if fuel > 20:
    print("Drive fast.")
else:
    if fuel > 10:
        print("Drive slow.")
    else:
        print("Stop to refuel.")
print()

#print()
#Programming and scripting languages generally support 3 kinds of operators, namely unary, binary and ternary. Unary operators are applied to a single operand, e.g. not True. Binary operators are applied to two operators, namely 5 + 2. Some languages support ternary operators, i.e. operators that are applied to three operators. An example in C++, C# and Java is the ?: operator which works as follows: condition to be tested ? Action if true : Action if false. Python does not have a ternary operator, but it supports a form of inline conditional statement based on an if-else statement. When interpreted, the first statement will trigger, except if the evaluation in the if statement evaluates to False. In this case, the statement following the else will trigger.
a = 10
b = 15

print("a is greater") if (a > b) else print("b is greater")

# or

c = 5 if (a < b) else 20
print(c)
print()

#print()
#The different data types have their purposes and are not always compatible. Even if they are compatible, applying them to one another might result in unexpected issues. What would (or should) happen if you try and add a float to a string? What happens when you divide an integer by a float? When dealing with a variable, it is helpful to be sure of what data type it actually contains. Python provides the type() function for this purpose.
print(type(3))
print(type(7.6))
print(type("Hello"))
print(type(input("Please enter a value:")))
print()

#print()
#Note from the above example that the result returned from an input() statement is always of type str (string). Although type() is handy for determining the type of a variable, it doesn't allow for the creation of a direct test to be used in a control structure, such as an if. That functionality is provided by the isinstance() function.
a = "50"

# isinstance is provided with the value to test (i.e. a) and the data type to test against
if isinstance(a,int):
    print("a is an int")
elif isinstance(a,float):
    print("a is a float")
elif isinstance(a,str):
    print("a is an str")
    print()

# print()
#Python (and other programming languages) provide the ability to convert an object of one data type to another data type. This conversion is known as casting. Python provides functions to perform casting to all basic data types (and more).  In most cases casting is accomplished by using the intended data type, e.g. int, as a method name and then passing the value to be converted as a value between brackets, e.g int(“50”).
a = 30.675
print("The value of a is", a, "and it is of type", type(a))
print("casting a to int using a = int(a)")
a = int(a)
print("The value of a is", a, "and it is of type", type(a))
print("casting a to float using a = float(a)")
a = float(a)
print("The value of a is", a, "and it is of type", type(a))
print("casting a to str using a = str(a)")
a = str(a)
print("The value of a is", a, "and it is of type", type(a))
print()
#Note how the a lost it's decimals when converting from float to int. When converting back to float the decimals do not return as the conversion process has changed the way the value is stored in memory when it was converted to int, i.e. int does not allocate space to store the decimal values. Thus, the decimal values cannot return when converting back to float since they no longer exist.
#print()