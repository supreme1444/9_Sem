lst = [1, 2, 3, 4]
def to_dict(lst):   
    komp = {element: element for element in lst}  
    return komp
s=to_dict(lst)    
print(s)
