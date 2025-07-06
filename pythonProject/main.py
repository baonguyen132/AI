from operator import length_hint
import numpy as np

def BinarySearch(list , so):
    left = 0
    right = length_hint(list) - 1

    while left+1 != right :
        middle = (left + right) // 2
        So_middle = list[middle]
        if So_middle < so: left = middle
        if So_middle > so: right = middle
        if So_middle == so: return middle

    return None

if __name__ == '__main__':
    list_name = [2, 4, 6, 7, 8, 23 , 25 , 45 , 60 , 63 , 70 , 76]
    print(BinarySearch(list_name, 50))

