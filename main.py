def createHeap(data, length, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < length and data[index] < data[left]:
            largest = left
        if right < length and data[largest] < data[right]:
            largest = right
        if largest != index:
            data[index], data[largest] = data[largest], data[index]
            createHeap(data, length, largest)
            
def heapSort(data):
        length = len(data)
        for index in range(length, -1, -1):
            createHeap(data, length, index)
        for index in range(length - 1, 0, -1):            
            data[index], data[0] = data[0], data[index]
            createHeap(data, index, 0)
        print(data)
        

random_list_of_nums = [35, 12, 43, 8, 51]  
heapSort(random_list_of_nums)  
print(random_list_of_nums)