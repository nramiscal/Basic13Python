# Print 1-255
# Print all the integers from 1 to 255.

def print1to255():
    for i in range(1,256):
        print i

print1to255()

# Print Ints and Sum 0-255
# Print integers from 0 to 255, and the sum so far.

def printIntsAndSum0to255():
    sum = 0;
    for i in range(0,256):
        sum += i
        print i
    print "Sum is {}".format(sum)

printIntsAndSum0to255()

# Print Max of Array
# Print the largest element in a given array, by iterating through it and comparing values.

def printMaxOfArray(arr):
    max = arr[0]
    for element in arr:
        if element > max:
            max = element
    print "Max is", max

printMaxOfArray([1,3,5,7,8,3,345,765,9,23])

# Print Odds 1-255
# Print all odd integers from 1 to 255.

def printOdds1to255():
    for i in range(1,256,2):
        print i

printOdds1to255()

# Print Array Values
# Print all values in a given array by iterating through it.

def printArrayValues(arr):
    for elem in arr:
        print elem

printArrayValues([1,3,5,7,8,3,345,765,9,23])

# Print Average of Array

def printAverageOfArray(arr):
    sum = 0.0
    for elem in arr:
        sum += elem
    print sum/len(arr)

printAverageOfArray([0,1,2,3,4,5,6,7,8,9])

# Greater than Y
# Count and print the number of array values less than a given Y.

def numGreaterThanY(arr, y):
    count = 0
    for elem in arr:
        if elem > y:
            count += 1
    print "Count is", count

numGreaterThanY([0,1,2,3,4,5,6,7,8,9],6)

# Print Max, Min, Average Array Values
# Given an array, print max, min and average values.

def printMaxMinAverageArrayVals(arr):
    max = arr[0]
    min = arr[0]
    sum = 0.0

    for elem in arr:
        if elem < min:
            min = elem
        if elem > max:
            max = elem
        sum += elem

    print "Max is", max
    print "Min is", min
    print "Avg is", sum/len(arr)

printMaxMinAverageArrayVals([0,1,2,3,4,5,6,7,8,9])

# Square Array Values
# Given an array, square each value in the array.

def squareArrVals(arr):
    for i in range(0,len(arr)):
        arr[i] = arr[i]*arr[i]
    print arr

squareArrVals([1,2,3,4,5])

# Zero Out Array Negative Values
# Set negative array values to zero.

def zeroOutArrayNegativeVals(arr):
    for i in range(0,len(arr)):
        if arr[i] < 0:
            arr[i] = 0
    print arr

zeroOutArrayNegativeVals([-1,-5,2,4,-6,8,9])

# Shift Array Values Left
# Shift array values: drop the first and leave '0' at end.

def shiftArrValsLeft(arr):
    for i in range(0,len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = 0
    print arr

shiftArrValsLeft([-1,-5,2,4,-6,8,9])

# Swap String for Array Negative Values
# Replace any negative array values with 'Dojo' .

def swapStringForArrayNegativeVals(arr):
    for i in range(0,len(arr)):
        if arr[i] < 0:
            arr[i] = "Dojo"
    print arr

swapStringForArrayNegativeVals([-1,-5,2,4,-6,8,9])
