import os
import random
class TextGenerator:
    def __init__(self):
        self.dictionary = {}
        self.first_words = set()
    
    def fit(self):
        directory = 'texts'
        files = os.listdir(directory)
        for i in files:
            file = open(directory+'\\'+i,'r').read()
            file.replace("!",".")
            file.replace("?",".")
            file.replace("...",".")
            file = file.split(". ")
            for sentence in file:
                line = sentence.translate(',:;-!.')
                line = line.lower().split()
                self.first_words.add(line[0])
                for j in range(len(line)-1):
                    res = self.dictionary.get(line[j])
                    if (res!=None and not line[j+1] in res):
                        res.append(line[j+1])
                    else:
                        res = [line[j+1]]
                    self.dictionary.update([(line[j],res)])
    def generate(self,length):
        while(length>0):
            next_w = random.choice(list(self.first_words))
            #print(next_w[0].upper()+next_w[1::],end = " ")
            while(self.dictionary.get(next_w)!=None and length>0):
                print(next_w,end = " ")
                next_w = random.choice(self.dictionary.get(next_w))
                length-=1

if __name__ == "__main__":
    textGenerator = TextGenerator()
    textGenerator.fit()
    textGenerator.generate(int(input()))
