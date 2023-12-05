# fonction 1
def countMoy(array):
    return sum(array)/len(array)
# fonction 2
def countOccurence(array):
    return array.count(12)
# fonction 3
def greater10(array):
    count = 0
    for i in range(len(array)):
        if (array[i] >= 10):
            count += 1
    return count
# fonction 4
def contains3(array):
    if 3 in array:
        return True
    return False

    

arr = [5, 12, 8, 3, 12, 7, 20, 10]

# exo 1
print("\nLa moyenne est: ", countMoy(arr))
# exo 2
print("\nLe nombre d'occurences de 12 est: ", countOccurence(arr))
# exo 3
print("\nLe nombre d'elements >= 10 est: ", greater10(arr))
# exo 4
if contains3(arr):
    print("\n3 est present")
else:
    print("\n3 nest pas present")

