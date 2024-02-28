# Question 16(a)
# Examination Number:

weight = int(input("Enter weight (in kilograms): "))
#(i)#read weight
#(ii)
height = int(input("Enter height (in centimetres): ")) # centimetres
#(iii)
bmi = round(weight / (height * height) * 10000)
print("BMI is: ", bmi)
