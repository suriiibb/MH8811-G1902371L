#get file lines
def getFileLines(fname) :
    fhandle = open(fname)
    lines = []
    for line in fhandle :
        line = line.rstrip()
        if line : 
            lines.append(line)
    return lines



lst = list(getFileLines('MH8811-04-Data.csv'))
for i in range(len(lst)):
    lst[i]=int(lst[i])


#program for finding the min
def my_min(lst):
    Smallest = None
    for the_num in lst:
        if Smallest is None:
            Smallest = the_num
        elif Smallest > the_num:
            Smallest = the_num
    return Smallest


#program for finding the max
def my_max(lst):
    Largest = None
    for the_num in lst:
        if Largest is None:
            Largest = the_num
        elif Largest < the_num:
            Largest = the_num
    return Largest


#program for finding the mediam
def my_median(lst):
    lst.sort()
    r = int(len(lst) / 2)
    if (int(len(lst) / 2)) * 2 == len(lst):
        median = 0.5 * (lst[r] + lst[(r+1)])
    elif int(len(lst) / 2) * 2 != len(lst):
        median = lst[r]
    return median

#program for finding the range
def my_range(lst):
    lst.sort()
    r = len(lst)
    my_max = lst[(r-1)]
    my_min = lst[0]
    range = my_max - my_min
    return range

#program for finding the average
def my_average(lst):
    r = len(lst)
    sum = 0
    for the_num in lst:
        sum = sum + the_num
    my_average = sum / r
    return my_average

#program for finding the sample variance
def my_samplevariance(lst):
    sum = 0
    m = 0
    r = len(lst)
    for the_num in lst:
        sum = sum + the_num
        avg = sum / r
    for the_num in lst:
        m = m + (the_num - avg) ** 2
        samplevariance = m / (r - 1)
    return samplevariance



print('The minimum of the list is ', my_min(lst))
print('The maximum of the list is ', my_max(lst))
print('The average of the list is ',my_average(lst))
print('The median of the list is ',my_median(lst))
print('The range of the list is ',my_range(lst))
print('The samplevariance of the list is ',my_samplevariance(lst))