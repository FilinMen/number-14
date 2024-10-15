import math 

input_data =open("input.txt","r")
data =input_data.read()
data = data.split()
a = int(data[0])
b = int(data[1])
g = math.gcd(a,b) # для нод
k = math.lcm(a,b) # для нок
output_data = open("output.txt","w")
output_data.write(k)
input_data.close()
output_data.close()

