def is_ancestor(name1,name2,pdict):
    while name2 != name1:
        if pdict.get(name2) != None:
            name2 = pdict[name2]
        else:
            return False
    return True

def is_related(name1,name2,pdict):
    list1 = [name1]
    while pdict.get(name1) != None:
        list1.append(pdict.get(name1))
        name1 = pdict.get(name1)
    list2 = [name2]
    while pdict.get(name2) != None:
        list1.append(pdict.get(name2))
        name1 = pdict.get(name2)
    for i in list1:
        if i in list2:
            return True
    return False

parent = {'Amy':'Ben', 'May':'Tom', 'Tom':'Ben',
 'Ben':'Howard', 'Howard':'George', 'Frank':'Amy',
 'Joe':'Bill', 'Bill':'Mary', 'Mary':'Philip', 'Simon':'Bill',
 'Zoe':'Mary'}
print(is_ancestor('Mary','Simon',parent))