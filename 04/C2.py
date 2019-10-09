#program for finding the min
lst = [9,41,12,3,74,15]
def my_min():
    Smallest = None
    for the_num in lst:
        if Smallest is None:
            Smallest = the_num
        elif Smallest > the_num:
            Smallest = the_num
    return Smallest
print (my_min())

#program for finding the max
def my_max():
    Largest = None
    for the_num in lst:
        if Largest is None:
            Largest = the_num
        elif Largest < the_num:
            Largest = the_num
    return Largest
print (my_max())

#program for finding the mediam
lst = [9,41,12,3,74,15]
def my_median():
    lst.sort()
    r = int(len(lst) / 2)
    if (int(len(lst) / 2)) * 2 == len(lst):
        median = 0.5 * (lst[r] + lst[(r+1)])
    elif int(len(lst) / 2) * 2 != len(lst):
        median = lst[r]
    return median
print (my_median())

#program for finding the range
lst = [9,41,12,3,74,15]
def my_range():
    lst.sort()
    r = len(lst)
    my_max = lst[(r-1)]
    my_min = lst[0]
    range = my_max - my_min
    return range
print (my_range())