#Function 1 - Countdown 

def countdown (num):
    result = []
    for i in range( num, -1, -1 ):
        result.append(i)
    print(result)

countdown(5)



#Function 2 - Print and Return 

def print_and_return(array):
    print(array[0])
    return array[1]


print(print_and_return([1,2]))
print(print_and_return([8,7]))


#Function 3 - First Plus Length

def sumFirstPlusLength (array):
    result = array[0] + len(array)
    return result

print(sumFirstPlusLength([2,5,8,6,1]))


#Function 4 - Values Greater than Second 

def greater (array):
    greaterList = []
    if len(array)<2:
        return False
    else:
        for number in range(0,len(array),1):
            if array[1]<array[number]:
                greaterList.append(array[number])
        print(len(greaterList))
        return greaterList

print(greater([1,2,5,3]))
print(greater([3]))

#Function 5 - List length, That Value

def createArray (a,b):
    newArray = []
    for number in range(0,a,1):
        newArray.append(b)
    return newArray

print(createArray(2,3))
print(createArray(5,8))