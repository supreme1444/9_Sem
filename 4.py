from itertools import repeat
dict_one = {'fierst_one':'we can do it'}
def biggest_dich(**kwargs):
    for _ in repeat(0):
        br= input("Введите s что бы остановить или a что бы продолжить")
        if br == "s":
         break
        elif br == "a":
            key1 = input("key")
            value1 = input("value")
            key,value = key1,value1
            dict_one.update({key:value}) 
        print(dict_one)
    return (dict_one)
mes = biggest_dich() 
print(mes)


    
