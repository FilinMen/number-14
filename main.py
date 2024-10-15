input_data =open("input.txt","r")
data =input_data.read()
data = data.split()
a = int(data[0])
b = int(data[1])
while a != 0 and b != 0: 
        if a > b:
            a = a % b
            
        else:
            b = b % a
            g = a + b
n = (a * b) / g
n = str(n)
output_data = open("output.txt","w")
output_data.write(n)
input_data.close()
output_data.close()

