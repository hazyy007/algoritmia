def find_duplicates(lst: list)-> list:
    list1=[]    
    dupli = set()
    visto = set()
    for i in lst:
        if i in visto:
            if i not in dupli:
                list1.append(i)
                dupli.add(i)
        else:
            visto.add(i)
    return list1
            
        