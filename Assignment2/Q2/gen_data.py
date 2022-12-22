import numpy as np
import json

def Rand(start, end, num):
    res = []
    for j in range(num):
        res.append(np.random.randint(start, end))
    return res
 
 
num = 1000000
start = 0
end = 100
data = Rand(start, end, num)
print("Initial Data:",data)

filename = 'data.json'
with open(filename, 'w') as file_object:
    json.dump(data, file_object)

