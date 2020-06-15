'''
冒泡排序:时间复杂度n²,空间复杂度1
'''
l = [1,423,12,1234,34,12,41,2,34,12,43,12]
for j in range(1,len(l)):
    for i in range(len(l)-j):
        if l[i] > l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]
print("冒泡排序,从小到大",l)
count = 0
l = [1,423,12,1234,34,12,41,2,34,12,43,12]
for j in range(1,len(l)):
    for i in range(len(l)-j):
        count+=1
        if l[i] < l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]
print("冒泡排序,从大到小",l)
print("列表长度:",len(l),"次数:",count)
print("-"*50)
'''
选择排序:时间复杂度n²,空间复杂度n
'''
l = [1,423,12,1234,34,12,41,2,34,12,43,12]
for i in range(len(l)-1):
    mindex = i
    for j in range(i+1,len(l)):
        count += 1
        if l[mindex] < l[j]:
            mindex = j
    l[i],l[mindex] = l[mindex],l[i]
print("插入排序,从大到小",l)
count = 0
l = [1,423,12,1234,34,12,41,2,34,12,43,12]
for i in range(len(l)-1):
    mindex = i
    for j in range(i+1,len(l)):
        count += 1
        if l[mindex] > l[j]:
            mindex = j
    l[i],l[mindex] = l[mindex],l[i]
print("插入排序,从小到大",l)
print("列表长度:",len(l),"次数:",count)
print("-"*50)
'''
插入排序:时间复杂度n²,空间复杂度1
'''
l = [31,1,423,12,1234,34,12,41,2,34,12,43,12]
for i in range(1,len(l)):
    for j in range(i,0,-1):
        if l[i] >= l[j-1]:
            l.insert(j,l[i])
            del l[i+1]
            break
    else:
        l.insert(0, l[i])
        del l[i + 1]
print("插入排序,从小到大",l)
l = [31,1,423,12,1234,34,12,41,2,34,12,43,12,42]
count = 0
for i in range(1,len(l)):
    for j in range(i,0,-1):
        count += 1
        if l[i] <= l[j-1]:
            l.insert(j,l[i])
            del l[i+1]
            break
    else:
        count += 1
        l.insert(0, l[i])
        del l[i + 1]
print("插入排序,从大到小",l)
print("列表长度:",len(l),"次数:",count)
print("-"*50)
'''
希尔排序:
'''
l = [31,1,423,12,1234,34,12,41,2,34,12,43,12,42,23]
# l = [9,7,3,5,1]
c = len(l)
gap = c//2
count = 0
count1 = 0
count2 = 0

while gap>0:
    count1 += 1
    for i in range(gap,c):
        count2 += 1
        j = i
        current = l[i]
        while j-gap>=0 and current<l[j-gap]:
            count += 1
            l[j] = l[j - gap]
            j = j - gap
        l[j] = current
    gap=gap//2

print("插入排序,从小到大",l)
print("列表长度:", len(l) ,"次数:", count,count1,count2)

'''
归并排序:时间复杂度log以2为底n的对数*n，空间复杂度为n
'''
def merge(left,right):
    result = []
    while len(left)>0 and len(right)>0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while len(left)>0:
        result.append(left.pop(0))
    while len(right)>0:
        result.append(right.pop(0))
    return result

def mergeSort(arr):
    c = len(arr)
    if c<2:
        return arr
    middle = c//2
    left = arr[0:middle]
    right = arr[middle:]
    return merge(mergeSort(left), mergeSort(right))

print(mergeSort([31,1,423,12,1234,34,12,41,2,34,12,43,12,42,23]))


# 递归 排序
def sortarr(left,right):
    result = []
    while len(left)>0 and len(right)>0:
        if left[0] > right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

def splitarr(arr):
    if len(arr)<2:
        return arr
    left = arr[0:len(arr)//2]
    right = arr[len(arr) // 2:]

    return sortarr(splitarr(left),splitarr(right))
print(splitarr([31,1,423,12,1234,34,12,41,2,34,12,43,12,42,23]))


'''
快速排序
'''

def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]

def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    for i in range(index,right):
        if arr[i] < arr[pivot]:
            swap(arr,i,index)
            index += 1
    swap(arr,pivot,index-1)
    return index - 1

def quickSort(arr, left="", right=""):
    c = len(arr)
    left = 0 if type(left) != int else left
    right = c-1 if type(right) != int else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex - 1)
        quickSort(arr, partitionIndex + 1, right)
    return arr
print(quickSort([31,1,423,12,1234,34,12,41,2,34,12,43,12,42,23]))
