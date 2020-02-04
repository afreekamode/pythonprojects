##1
'''PI = 3.14159265358979 # global constant -- only place the value of PI is set
def circleArea(radius):
    return PI*radius*radius # use value of global constant PI'''
##2
'''def circleCircumference(radius):
    return 2*PI*radius # use value of global constant PI
print('circle area with radius 5:', circleArea(5))
print('circumference with radius 5:', circleCircumference(5))'''
##3friends = ['ade', 'wale', 'lola', 'ada']
'''for friend in friends:
    print('merry Xmas:', friend)
print('and happy new year!')'''
##4.0Checking largest num  
'''largest_so_far = -1
print('smallest', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15, 34]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('largest num is', largest_so_far,)'''
##4.1Checking smallest num  
'''smallest_so_far = None
for value in [9, 41, 12, 3, 74, 15, 34]:
comment use for false, noine, true as its stronger thn ==
    if smallest_so_far is None:
        smallest_so_far = value
    elif value < smallest_so_far:
        smallest_so_far = value
    print(smallest_so_far, value)
print('smallest num is', smallest_so_far,)'''
##5Count & summing num
'''sum_count = 0
for thing in [9, 41, 66, 76, 4, 55, 8, 9, 33, 201, 43,]:
    sum_count =sum_count  + thing
    print(sum_count, thing)
print('Total sum of count is', sum_count)'''
##6Counting total appearance
'''count = 0
for thing in [9, 41, 66, 76, 4, 55, 8, 9, 33, 201, 43,]:
    count =count  + 1
    print(count, thing)
print('Total count is', count)'''
##7Total average counts
'''count = 0
sum = 0
print('count', 'sum', 'value')
for value in [9, 41, 66, 76, 4, 55, 8, 9, 33, 201, 43,]:
    count = count  + 1
    sum = sum + value
    print(count, sum, value)
print('Total average counts is', sum / count)'''
####9Pointing out a particular digit from group of nums
'''value = 0
count = 0
for value in [9, 41, 66, 76, 4, 9, 55, 8, 9, 33, 201, 43,]:
    if value == 9:
        count = count  + 1
        print ('large values', value, count)''' 
#### 10.0calculate inpute by users        
'''num = 0
total = 0.0
print('enter value to calculate averae count\n ')
while True:
     sval = input('->')
     if sval == '=':
         break
     try:
         fval = float(sval)
     except:
         print('invalid input')
         # use continue to retunrn if there is a mistake
         continue
    # print(fval)
     num = num + 1
     total = total + fval
    # print('all done')
print('total,:',total, 'count:',num,' and average:',total/num)'''
##11
'''my_list = [1, 2, 4, 5, 3,]
my_list.append(8)
for i in my_list:
    if i == None:
       print(i - 5)
    else:
        print(i)'''
##12
'''set = {3,4,5,7,8,9,'red'}
set1 = {'green', 4,7,9,'red','yellow','blue'}
print('union=', set|set1)
print('inter=', set&set1)
print('dif=', set-set1)
print('dif=', set1-set)'''

##13
















