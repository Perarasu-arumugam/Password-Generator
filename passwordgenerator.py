import random
print ( """******************ARASU 1st PROJECT**********************
___________________________________________________________""")
password = int(input("ENTER THE LENGTH OF THE PASSWORD TO GENERATE = "))

c = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM,.@"

output = "".join(random.sample(c,password))
print(output)
