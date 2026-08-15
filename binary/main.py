


def d_to_b(num:int):
    target= ''
    while num > 0 :
        rmd = num % 2
        num = int(num / 2)
        target = str(rmd)+target 
    return target 

def b_to_d(binary:str):
    binary= binary[::-1]
    target= 0 
    for idx,element in enumerate(binary):
        target+= int(element)* (2**idx)
    return target 



if __name__=='__main__':
    num=int(input())
    target = d_to_b(num)
    print(target)
    get =b_to_d(target)
    print(get)