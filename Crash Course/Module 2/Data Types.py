            #Module 2
print(type("a"))
print(type(2))
print(type(2.5))

z = 7
print("hi", z)
print("hi", str(z))
print(f"hi {str(z)}")

print()

import typing
# Define a variable of type str
z: str = "Hello, world!"
print(z)
# Define a variable of type int
x: int = 10
print(x)
# Define a variable of type float
y: float = 1.23
print(y)
# Define a variable of type list
list_of_numbers: typing.List[int] = [1, 2, 3]
print(list_of_numbers)
# Define a variable of type tuple
tuple_of_numbers: typing.Tuple[int, int, int] = (1, 2, 3)
print(tuple_of_numbers)
# Define a variable of type dict
dictionary: typing.Dict[str, int] = {"key1": 1, "key2": 2}
print(dictionary)
# Define a variable of type set
set_of_numbers: typing.Set[int] = {1, 2, 3}
print(set_of_numbers)

