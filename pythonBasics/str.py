str = "RahulShettyAcademy.com"
str1 = " Consulting firm"
str3 = "RahulShetty"

print(str[1])  # a
print(str[0:5])  # if you want substring in python
print(str + str1)  # concatenation
print(str3 in str)  # true or false(substring check)

Var = str.split(".")
print(Var)
print(Var[1])

str4 = " great "
print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())
