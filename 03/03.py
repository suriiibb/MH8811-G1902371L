def choose():
    print ('Please choose among the programs:p01,p02,p03')
    print ('p01 can greet you as\'Hello, world!\' ')
    print ('p02 can greet you as \'Hello, your name\' ')
    print ('p03 can convert your Celsius input into Farenheit')
    opt = input ('Please choose your desired function')

#below is the code for program p01
def p01():
    func1 = 'Hello, world'
    return

#below is the code for program p02
def p02():
    name = input ('Please enter your name')
    func2 = 'Hello' + name
    return

#below is the code for program p03
def p03():
    C = float(input('Enter the temperature in Celsius'))
    func3 = C * 1.8 + 32
    return

if opt = 'p01':
    print (func1)
elif opt = 'p02':
    print (func2)
elif opt = 'p03':
    print (func3)
else:
    print ('Invalid input')

choose()
