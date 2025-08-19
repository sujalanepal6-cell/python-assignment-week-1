# simple calculator

a=int(float(input("Enter first number:")))
b=int(float(input("Enter second number:")))

print("sum:", a + b)
print("Difference:",a - b)
print("Multiplication:",a*b)

if b !=0:
      print("Division:",a / b)
      print("Modulus:",a % b)
      print("Integer Dvision =",a // b)

      
else:
      print("Division,Moduluse,Integer Division not possible (div by zero)")
      print("power =",a ** b)