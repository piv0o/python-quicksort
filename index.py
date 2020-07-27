#========================================#
# Imported Libaries
#========================================#
from random import random
from time import time
from math import floor
import sys

#========================================#
# Randomize Array
#========================================#

def createRandomArray(n):
    arr = [];
    for i in range(n):
        arr.append(round(random()*100));
    return arr;

#========================================#
# Quick Sort Algorithm
#========================================#
def quickSort(arr, * args ):
    #----------------------------------
    # init low and high if not avaiable
    #----------------------------------
    if(len(args) > 0):
        low = args[0];
    else:
        low = 0; 

    if(len(args) > 1):
        high = args[1];
    else:
        high = len(arr) - 1;

    if(len(arr) > 1):
        #----------------------------------
        # partitions the array
        #----------------------------------
        index = partition(arr,low,high);
        #----------------------------------
        # recurve branch the next elements in the array
        #----------------------------------
        if(low < index - 1):
            quickSort(arr, low, index - 1);

        if(index < high):
            quickSort(arr, index, high);
    
    return arr;


def partition(arr, low, high):
    pivot = arr[floor((low + high) / 2)];
    i = low;
    j = high;

    while(i <= j):
        while (arr[i] < pivot):
            i+=1;

        while (arr[j] > pivot):
            j-=1;

        if(i <= j):
            arr = swap(arr, i, j);
            i+=1;
            j-=1;

    return i; 


def swap(arr, index1, index2):
    if(index1 != index2):
        #pop the array elements 
        firstElement = arr.pop(index1);
        secondElement = arr.pop(index2-1);
        #re-insert the array elements 
        arr.insert(index1, secondElement);
        arr.insert(index2, firstElement);
    return arr; 


#========================================#
# Initialization
#========================================#
def initilize(n):
    randomArray = createRandomArray(n);
    print("\n["+str(n)+"] Randomized Array\n");
    start = time()*1000;
    SortedArray = quickSort(randomArray);
    delta = time()*1000 - start; 
    print(SortedArray);
    print("sorted "+str(n)+ " elements in "+str(delta)+"ms");

initilize(int(sys.argv[1]));