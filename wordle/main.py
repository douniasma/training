from wonderwords import RandomWord

r = RandomWord()

target = r.word(word_min_length=5, word_max_length=5)

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


