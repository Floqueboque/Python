class Grammatik:

    @property
    def NichtTerminale(self):
        return self.nichtTerminale

    @property
    def Alphabet(self):
        return self.alphabet

    @property
    def Produktionen(self):
        return self.produktionen
    
    @property
    def Startsymbol(self):
        return self.startsymbol

    def __init__(self, nichtTerminale, alphabet, produktionen, startsymbol ):
        self.nichtTerminale = nichtTerminale
        self.alphabet = alphabet
        self.produktionen = produktionen
        self.startsymbol = startsymbol

import pprint

def main():
    nichtTerminale = ["S", "A", "B", "C"]
    alphabet = ["a", "b"]
    produktionen = {
    "S": ["AB", "AC"],
    "A": ['a', "BA"],
    "B": ['b', "CC"],
    "C": ['a', "AB"]
    }
    

    g = Grammatik(nichtTerminale, alphabet, produktionen, "S")
    CYK(g, "acbab")


def CYK(g:Grammatik, word:str):
    w, h = 5, 5
    Matrix = [[0 for x in range(w)] for y in range(h)]

    for i in range(len(word)):
        char = word[i]
        temp = checkValueIsInDict(g.Produktionen, char)
        #   Zeile Spalte
        Matrix[0][i] = temp

    j=1
    while j < len(word):
        i=0
        while i < (len(word)+1-(j+1)):
            Matrix[j][i] = 0
            k=0
            temp = ""
            while k <= j-1:
                field1 = Matrix[k][i]
                field2 = Matrix[(j-k)-1][(i+k)+1]
                toCheck = ""
                if type(field1) is str and type(field2) is str:                    
                    for c1 in field1:                        
                        toCheck = toCheck + c1
                        cntC2 = 0
                        for c2 in field2:
                            cntC2 = cntC2+1
                            toCheck = toCheck + c2
                            temp = temp + checkValueIsInDict(g.Produktionen, toCheck)
                            if cntC2 == len(field2):
                                toCheck = ""
                            else:                                                                       
                                toCheck = toCheck[0]           
                k=k+1
            Matrix[j][i] = temp
            i=i+1
        j=j+1

    pprint.pprint(Matrix)

def checkValueIsInDict(dict, value):
    temp = ""
    for key, val in dict.items():
                if value in val:
                    temp = temp + key
    return temp
                
    
if __name__ == "__main__":
    main()


