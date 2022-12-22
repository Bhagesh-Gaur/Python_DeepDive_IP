from mpi4py import MPI
import json
import math


def insertionSort(arr):
    n = len(arr)
    if (n <= 1):
        return
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key


with open('data.json','r') as file_object:  
    data = json.load(file_object)

root = 0

comm = MPI.COMM_WORLD # Communicator for intraprocessor communication
max_processors = comm.size # Retriving Processor Counts
new_list = []
bin_size = math.floor(int((max(data)-min(data))/comm.size))

for rank in range(max_processors):  # Alloting the numbers to the bins
    new_list.append([x for x in data if (x >= bin_size*rank+rank) and x<=(bin_size+bin_size*rank+rank)])

v = comm.scatter(new_list,root) # Distributing/Scattering lists amongst the processors
print("The Rank of",v, "is", comm.rank)

# v = sorted(v) # Insertion sort on the list for the current processor 
insertionSort(v)

g = comm.gather(v,root) # Assembling the sorted lists
if comm.rank==0:
    sorted_list = []
    for i in range(len(g)):
        print("Rank:",i," ",g[i])
        sorted_list.extend(g[i])
    print("Sorted Data:",sorted_list)