Smallest = None
for the_num in [9,41,12,3,74,15]:
    if Smallest is None:
        Smallest = the_num
    elif Smallest > the_num:
        Smallest = the_num
    print (Smallest, the_num)
print ('After', Smallest)