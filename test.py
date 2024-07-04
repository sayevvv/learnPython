
# Syntax learning python 

#unpacking
pack = ["word 1", 30, 2.76]
var, var2, var3 = pack

print(var)
print(var2)
print(var3)

#output variables
x = "Hello World "
y = "Hello Human"

print(x,y)
print(x+y)

#for numbers, + acts as an operator
x1 = float(7)
x2 = float(8)
print(x1 + x2)
print(x2 * x1)

#Variables Created outside of function can be used inside the func
def myfunc():
    hasilBagi = x1 / x2
    hasilKali = x1 * x2
    global ye # make function var to global
    ye = "i might be a global var gang"
    print("Hasil bagi dari 7 dan 8 adalah " + str(hasilBagi))
    print("Hasil kali nya " + str(hasilKali))

myfunc()

print(ye) # In order to use this var, the func needs to be called out first and this line HAVE TO BE AFTER THE FUNCTION

# x = "Hello World"	str	
# x = 20	int	
# x = 20.5	float	
# x = 1j	complex	
# x = ["apple", "banana", "cherry"]	list	
# x = ("apple", "banana", "cherry")	tuple	
# x = range(6)	range	
# x = {"name" : "John", "age" : 36}	dict	
# x = {"apple", "banana", "cherry"}	set	
# x = frozenset({"apple", "banana", "cherry"})	frozenset	
# x = True	bool	
# x = b"Hello"	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview	
# x = None	NoneType
	
# Setting the Specific Data Type

# If you want to specify the data type, you can use the following constructor functions:

# x = str("Hello World")	str	
# x = int(20)	int	
# x = float(20.5)	float	
# x = complex(1j)	complex	
# x = list(("apple", "banana", "cherry"))	list	
# x = tuple(("apple", "banana", "cherry"))	tuple	
# x = range(6)	range	
# x = dict(name="John", age=36)	dict	
# x = set(("apple", "banana", "cherry"))	set	
# x = frozenset(("apple", "banana", "cherry"))	frozenset	
# x = bool(5)	bool	
# x = bytes(5)	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview

num1 = 40e2 
print(type(num1)) # this is float, e means power of

num2 = 3j 
print(type(num2)) # complex, j is the imaginary part




