# Simple form
name = input("Enter your Name:")
age = int(input("Enter your age:"))
height = float(input("Enter your Height:"))
country = input("Enter your country:")

name = name.upper()
height = f"{height:.2f}"
country = country.upper()
nickname = (name[:2] + name[-2:]).upper()

print("Hello",name)
print("You are", age, "your old.")
print("Your height is",height,"feet.")
print("You are from", country + ".")
print("Your nickname is",nickname)