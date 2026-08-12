import random

dictionary= ['rests',"kills","anchor","holes","write","alien","cards"]
index = random.randrange(len(dictionary))
target=dictionary[index]


tries=5
while tries !=0:
    word= input()
    if len(word) !=5: print("casse toi")
    elif word == target : print("yep")
    elif word != target : 
        for idx,let in enumerate(word):
            for idxs,lets in enumerate(target):
                if idx==idxs and let==lets:
                    print('letter at pos '+str(idx +1)+' is correct')
                    break
                if idx !=idxs and let==lets : 
                     print('letter at pos '+str(idx +1)+' is in the wrong position')
    tries-= 1


print("Kemlo drahmek")


