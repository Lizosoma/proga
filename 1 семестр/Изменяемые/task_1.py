a_list = [10, "hello", 42.0, True]
a_tuple = (10, "hello", 42.0, True)
a_string = "hello"
a_set = {10, "hello", 42.0, True}
a_frozenset = frozenset(a_list)  # создаем из списка
a_dict = {"cat": "mew", "posov": "python", "dog": "woof", "duck": "quack"}

#=====

def shrinkList(l):

    l_new = [x for x in l]
    l_new.pop()

    return l_new

#=====

def shrinkTuple(t):

    t = list(t)
    t.pop()
    t = tuple(t)

    return t

#====

def shrinkString(s):

    s_new = s
    s_new = s_new[0:-1]

    return s_new

#=====

def shrinkSet(s):

    s_new = {y for y in s}
    s_new.pop()

    return s_new

#=====

def shrinkFrozenset(f):

    f = set(f)
    f.pop()
    f = frozenset(f)

    return f

#=====

def shrinkDict(d):

    d_new = {z:d[z] for z in d.keys()}
    d_new.popitem()

    return d_new

### чистые функции    
print("стало", shrinkList(a_list))
print("было", a_list)
print("стало", shrinkTuple(a_tuple))
print("было", a_tuple)
print("стало", shrinkString(a_string))
print("было", a_string)
print("стало", shrinkSet(a_set))
print("было", a_set)
print("стало", shrinkFrozenset(a_frozenset))
print("было", a_frozenset)
print("стало", shrinkDict(a_dict))
print("было", a_dict)

#=====

def shrinkListInPLace(lip):

    lip.pop()


#=====

def shrinkTupleInPLace(tip):
    
    print('неизменяемый объект')

#=====

def shrinkStringInPLace(sip):

    print('неизменяемый объект')

#=====

def shrinkSetInPLace(sep):

    sep.pop()

#=====

def shrinkFrozensetInPLace(fsip):

    print('неизменяемый объект')

#=====

def shrinkDictInPLace(dip):
    
    dip.popitem()



### изменяющие функции
shrinkListInPLace(a_list)
print("изменилось так:", a_list)
shrinkTupleInPLace(a_tuple)
print("изменилось так:", a_tuple)
shrinkStringInPLace(a_string)
print("изменилось так:", a_string)
shrinkSetInPLace(a_set)
print("изменилось так:", a_set)
shrinkFrozensetInPLace(a_frozenset)
print("изменилось так:", a_frozenset)
shrinkDictInPLace(a_dict)
print("изменилось так:", a_dict)
