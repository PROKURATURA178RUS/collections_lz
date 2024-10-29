input_data = open('input.txt','r') # Создадим файл со входными данными
data = input_data.read ()
data = data.split()
n = int(data[0])
fib1 = 1
fib2 = 1 
pr_list = []
for i in range(-1 , n+1 ):     
    
    pr_list.append(fib2) 
    

output = open('output.txt', 'w') 
output.write(str(pr_list))
output.write(str())



input_data.close() 
output.close()   