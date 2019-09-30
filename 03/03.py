#below is the code for program p01
def p01():
    func1 = 'Hello, world'
    return func1

#below is the code for program p02
def p02_1():
    name = input ('Please enter your name')
    func2 = 'Hello,' + name
    return func2

#below is the code for program p03
def p02_2():
    C = float(input('Enter the temperature in Celsius'))
    func3 = C * 1.8 + 32
    return func3

while 1>0:
    def choose():
        print ('Please choose among the programs:p01,p021,p022')
        print ('p01 can greet you as\'Hello, world!\' ')
        print ('p02_1 can greet you as \'Hello, your name\' ')
        print ('p02_2 can convert your Celsius input into Farenheit')
        opt = input ('Please choose your desired function')
        if opt == 'p01':
            print (p01())
        elif opt == 'p02_1':
            print (p02_1())
        elif opt == 'p02_2':
            print (p02_2())
        else:
            print ('Invalid input')


    choose()