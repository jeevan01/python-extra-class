#list[]
list_number = [1,3.3,23,5,4]
#print(type(list_number))
sum=0
for x in list_number:
    print("number is",x)
    sum = sum + x
    print(sum)

list_number.append(100)
list_number.sort()

# list_number.reverse()
print(list_number)

#tuple()

#sets{}
x = {3,5,2,3,4}

#dictionary {}
{
    'key' : {'value':3}
}

#dict1 = {key:value, key1:value1, key2:value2}
