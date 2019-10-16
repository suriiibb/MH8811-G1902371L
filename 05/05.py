import json
#use json to load file
def open_f(filename):
    fh = open (filename)
    data = json.load(fh)
    fh.close
    return data

#chosse a file and open and check the data type
choosefile = input ("Please choose among : H1-1.json,H1-2.json,H1-3.json,H1-4.json or H1-5.json")
data = open_f (choosefile)
data_typ = type (data)
print (data_typ)

#serialize data based on its type
def serialize(data):
    if data_typ is list:
        res = "list|"
        for i in data: 
            res = res + str (data)
            res=res + ";"
            res=res + str(type(i))
            res = res + "|"
        return res [:-1]

    elif data_typ is dict:
        res = "dict|"
        for i in data:
            res = res + str(i)
            res = res + ":"
            res = res + str (l[i])
            res = res + ";"
            res = res + str (type (l[i]))
            res = res + "l"
        return res [:-1]

#Write the string to a file (ask user for a file name for that too).
filename = input ("Please enter a file name for serialized data")
savefile = open (filename,'w')
savefile.write (serialize(data))
savefile.close()

#read the string back from the file
openfile = open (filename)
readdata = openfile.read()
openfile.close()

#Deserialize
def deserialize(saved):
    string1 = saved.split ("|")
    typ1 = string1[0]
    string2 = string1[1:]

    if typ1 == "list":
        desrl = list()
        for i in string2:
            string3 = i.split (";")
            ele_typ = string3[1]
            ele = string3 [0]
            if ele_typ == "<class 'int'>":
                desrl.append(int(ele))
            elif ele_typ == "<class 'float'>":
                desrl.append(float(ele))
            else:
                desrl.append(str(ele))
        return(output)
    
    elif type_1 == "dict":
        desrl = dict()
        for i in string2:
            string3 = i.split(":")
            key = string3[0]
            string4 = string3[1].split(";")
            value = string4[0]
            value_typ = string4[1]
            if value_typ == "<class 'int'>":
                desrl[key] = int(value)
            elif value_type == "<class 'float'>":
                desrl[key] == float (value)
            else:
                desrl[key] = value
            return (desrl)

#Compare the two data structures
def my_compare(ds1, ds2):
    if type (ds1) != type (ds2):
        return False
    else:
        if isinstance (ds1, list):
            if ds1 == ds2:
                return True
            else:
                return False
        else:
                for i in ds1:
                    if i not in ds2:
                        return False
                    else:
                        if len(ds1) == len(ds2):
                            return True
                        else:
                            return False
                return True

