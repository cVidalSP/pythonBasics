print('imprima isso')
x = 1
if x == 1:
     print('eh 1')
else:
     print('lesho')

myint = 5
print(myint)

myfloat = 7.0
print(myfloat)
myfloat = float(myfloat)
print(myfloat)

string1 = 'Olha soh'
print(string1)
string2 = "Usando aspas duplas, se pode usar ' no meio da string"
print(string2)

a, b = 3, 4
print(a,b)

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
     print(x)

number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

helloworld = "hello" + " " + "world"
print(helloworld)

lotofhellos = "hello" * 10
print(lotofhellos)

even_number = [2,4,6,8]
odd_number = [1,3,5,7]
all_number = odd_number + even_number
print(all_number)

print([1,2,3] * 3)

name = "Carlos"
print("Hello, %s!" % name)

age = 23

print("%s is %d years old." % (name,age))

mylist = [1,2,3]
print("A list : %s" % mylist)

x = 2
print(x == 2)
print(x == 3)
print(x < 3)

if name == "Carlos" and age == 23:
     print("Your name is Carlos, and you are 23 years old.")

if name == "Jao" or "Calors":
     print("Your name is either Jao or Carlos") 

if name in ["Jao","Carlos"]:
     print("Your name is either Jao or Carlos")

x = 2 
if x  == 2:
     print("x equals two!")
else:
     print("x does not equal to two")

x = [1,2,3]
y = [1,2,3]

print(x == y)
print(x is y)

primes = [2, 3, 5, 7]
for prime in primes:
     print(prime)


for x in range(5):
     print(x)

for x in range(3,6):
     print(x)

for x in range(3,8,2):
     print(x)

count = 0
while count < 5:
     print(count)
     count += 1

def my_function():
     print("Hello from my function")

def my_function_with_args(username, greeting):
     print("Hello, %s , from my function!, I wish you %s" %(username,greeting))

def sum_two_numbers(a ,b):
     return a + b

my_function()
my_function_with_args('Pedro','Muitos dinheiros')
sum_two_numbers(66,3)

class MyClass:
     variable = "Blah"

     def function(self):
          print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "batata"

print(myobjectx.variable)
print(myobjecty.variable)

myobjectx.function()

phonebook = {}
phonebook['carlos'] = 999999999
phonebook['andreia'] = 999999998
phonebook['joao'] = 999999997
phonebook['leandro'] = 999999996

print(phonebook)

alunos = {
     "Caina": 7,
     "Pedro": 9,
     "Joao": 3
}

print(alunos)

for name,number in phonebook.items():
     print("Phone number of %s is %d" %(name, number))

del phonebook["joao"] 
phonebook.pop("andreia")
print(phonebook)








