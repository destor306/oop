"""Word Finder: finds random words from a dictionary."""

from random import randint

class WordFinder:
    
    def __init__(self, address):
        self.file = open(address ,'r')
        self.words = self.read(self.file)
        
        
        self.file.close()
        print(f"{len(self.words)} words read")
    
    def read(self,file):
        return [word.strip() for word in file]
    
    
    def showwords(self):
        for i in range(len(self.words)):
            print(self.words[i])
    
    def random(self):
        return f"{self.words[randint(0,len(self.words))-1]}"
    

class SpecialWordFinder(WordFinder):
    
    def read(self, file):
        return [word.strip() for word in file if word.strip() and not word.startswith("#")]