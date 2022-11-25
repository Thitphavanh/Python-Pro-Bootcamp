# weight = 80
# height = 1.73

# bmi = weight/(height*height)
# print(bmi)

# ********************

# weight_as_int = int(weight)
# height_as_float = float(height)

# bmi = weight_as_int / (height_as_float * height_as_float)
# bmi_as_int = int(bmi)


height = input("enter your height in m: ")
weight = input("enter your weight in m: ")

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)
