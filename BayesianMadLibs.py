# Bayesian Mad Libs
# Define classes POSWordList, MadLibsSentence, MadLibs

import random

class POSWordList:
#gives a part of speech or word type, e.g. noun and a list of words of that type 
    def __init__(self,POS,wordList):
    #better to make words a list or a set? I think I won't use list functionality. Better to store as Dict? We'll see.
        self.POS=POS
        self.wordList=wordList

class MadLibsSentence:
#stores a sentence and a Dictionary of POSWordLists = word type + list of words of that type/part of speech
    #The starting sentence we plan to remove text from
    sentenceOriginal=""
    #Where we'll store the new sentence after replacements
    sentenceNew=""
    #The word type/word list Dictionaries for word replacement
    POSDictRemove={}
    POSDictAdd={}
    
    def __init__(self, sentenceOriginal,POSDictRemove,POSDictAdd):
        self.sentenceOriginal=sentenceOriginal
        self.POSDictRemove=POSDictRemove
        self.POSDictAdd=POSDictAdd
        
    def replaceAll(self):
    #As written, makes replacements for all word types/parts of speech that appear in both our remove and add dictionaries
    #We could write a method letting us choose which types to replace, so for the same sentence we could choose to replace e.g. either nouns or adjectives
        self.sentenceNew=self.sentenceOriginal
        #checks for wordType in both the remove dict and the add dict
        for wordType in self.POSDictRemove.keys():
            if wordType in self.POSDictAdd.keys():
                numToReplace = min(len(self.POSDictRemove[wordType]),len(self.POSDictAdd[wordType]))
                #chooses random words from remove list, no replacement 
                #needed to make sure we don't always take the earlier entries from the list if we have more remove words than add words
                if numToReplace<len(self.POSDictRemove[wordType]):
                    indicesToRemove=random.sample(range(0,len(self.POSDictRemove[wordType])),numToReplace)
                else:
                    indicesToRemove=range(0,len(self.POSDictRemove[wordType]))
                #chooses random words from add list, no replacement
                if numToReplace<len(self.POSDictAdd[wordType]):
                    indicesToAdd=random.sample(range(0,len(self.POSDictAdd[wordType])),numToReplace)
                else:
                    indicesToAdd=range(0,len(self.POSDictAdd[wordType]))
                for i in range(0,numToReplace):
                    self.sentenceNew=self.sentenceNew.replace(self.POSDictRemove[wordType][indicesToRemove[i]],self.POSDictAdd[wordType][indicesToAdd[i]],1)
        return self.sentenceNew

class MadLibs:
    
    #list of MadLibSentences
    sentences = []
    #Add addDict that can be used for all sentences instead of their individual addDicts?
    #addDict={}

    def randomSentence(self,N=0):
        #returns a single MadLibsSentence (N=0) or a list of N MadLibsSentences to be filled
        #the same MadLibsSentence might appear multiple times
        randomSentenceList=[]
        if N==0:
            #random.sample returns a list so we add [0] here to get just the element in the list
            s=random.sample(self.sentences,1)[0]
            return s
        else:
            for index in range (0,N):
                #random.sample returns a list so we add [0] here to get just the element in the list
                s=random.sample(self.sentences,1)[0]
                randomSentenceList.append(s)
            return randomSentenceList
    
    def randomFilledSentence(self,N=0):
        #auto random fill using prestored lists for filling
        #returns a string/filled sentence
        if N==0:
            s=self.randomSentence()
            filledSentence=s.replaceAll()
            return filledSentence
        else:
            filledList=[]
            for index in range(0,N):
                s=self.randomSentence()
                filledList.append(s.replaceAll())
            return filledList
    
    def fillIndexedSentence(self,index=0,N=0):
        #use to make one or a lot of examples for a single original sentence
        #returns a single string/filled sentence (N=0) or a list of N strings/filled sentences 
        if N==0:
            s=self.sentences[index]
            return s.replaceAll()
        else:
            for index in range(0,len(self.sentences)):  
                s=self.sentences[index]
                filledList=[]
                for i in range(0,N):
                    filledList.append(s.replaceAll())
            return filledList

# Create BayesianCatsMadLibs (instance of MadLibs) and fill with Bayesian sentences (MadLibsSentences)
# Bayesian sentences with cat noun replacements

BayesianCatsMadLibs=MadLibs()

#define cat word lists to draw replacements from
catNouns = POSWordList("noun",['laser pointer', 'scratching post', 'bird', 'mouse', 'lap', 
'hiss', 'meow', 'stretch', 'tail twitch', 'ball of string', 'feather toy', 'window sill', 
'box', 'tree', 'purr', 'hairball', 'cat nap', 'catnip', 'whisker'])
catPluralNouns=POSWordList("plural noun",['fish', 'socks', 'salmon treats', 'cat beds', 
'litter boxes', 'paws', 'claws', 'feathers', 'birds', 'whiskers', 'shredded toilet paper'])
POSDictCats={catNouns.POS:catNouns.wordList,catPluralNouns.POS:catPluralNouns.wordList}

#define five Bayesian MadLibs sentences
s1='A Bayesian network is a graphical model that encodes probabilistic relationships among variables of interest.'
n1=POSWordList('noun',['network','model'])
np1=POSWordList('plural noun',['relationships','variables'])
POSDict1={n1.POS:n1.wordList,np1.POS:np1.wordList}
BayesianSentence1=MadLibsSentence(s1,POSDict1, POSDictCats)

s2='When used in conjunction with statistical techniques, the graphical model has several advantages for data analysis.'
n2=POSWordList('noun',['model','data'])
np2=POSWordList('plural noun',['techniques','advantages'])
POSDict2={n2.POS:n2.wordList,np2.POS:np2.wordList}
BayesianSentence2=MadLibsSentence(s2,POSDict2, POSDictCats)

s3='Because the model encodes dependencies among all variables, it readily handles situations where some data entries are missing.'
n3=POSWordList('noun',['model',])
np3=POSWordList('plural noun',['dependencies','variables','situations','data entries'])
POSDict3={n3.POS:n3.wordList,np3.POS:np3.wordList}
BayesianSentence3=MadLibsSentence(s3,POSDict3, POSDictCats)

s4='A Bayesian network can be used to gain understanding about a problem domain and the consequences of intervention.'
n4=POSWordList('noun',['network','problem'])
np4=POSWordList('plural noun',['intervention'])
#'intervention' isn't a plural noun but it seems like it's best replaced by a plural noun from our add list
POSDict4={n4.POS:n4.wordList,np4.POS:np4.wordList}
BayesianSentence4=MadLibsSentence(s4,POSDict4, POSDictCats)

s5='Bayesian statistical methods, with Bayesian networks, offer an efficient and principled approach to avoid overfitting of data.'
n5=POSWordList('noun',['approach'])
np5=POSWordList('plural noun',['methods','networks','data'])
POSDict5={n5.POS:n5.wordList,np5.POS:np5.wordList}
BayesianSentence5=MadLibsSentence(s5,POSDict5, POSDictCats)

s6='Hierarchical modeling is used when a information is available on several different levels of observational units.'
# no singular noun
n6=POSWordList('noun',['information'])
np6=POSWordList('plural noun', ['units'])
POSDict6={n6.POS:n6.wordList,np6.POS:np6.wordList}
BayesianSentence6=MadLibsSentence(s6, POSDict6, POSDictCats)

#put Bayesian MadLibs sentences into BayesianCatsMadLibs
BayesianCatsMadLibs.sentences=[BayesianSentence1,BayesianSentence2,BayesianSentence3,BayesianSentence4,BayesianSentence5,BayesianSentence6]


#Cat Sentences with Bayesian Replacements

#define Bayesian word lists to draw replacements from
BayesianNouns = POSWordList("noun",['posterior distribution','Metropolis-Hastings algorithm','inference','prior','model choice','likelihood function','Bayesian inference','sequential analysis','hypothesis testing','algorithm','Gibbs sampling','probability','conditional probability','inference','linear regression'])
BayesianPluralNouns=POSWordList("plural noun",['Bayesian statistics','priors','hypotheses','Markov Chain techniques', 'parameters','Bayesian methods','probabilities'])
POSDictBayesian={BayesianNouns.POS:BayesianNouns.wordList,BayesianPluralNouns.POS:BayesianPluralNouns.wordList}

#define five cat MadLibs sentences
s1='A hybrid of a domestic feline and a medium size African wild cat, the Savanna is a challenging and rewarding companion.'
n1=POSWordList('noun',['feline', 'wild cat', 'Savanna'])
np1=POSWordList('plural noun',[])
POSDict1={n1.POS:n1.wordList,np1.POS:np1.wordList}
catSentence1=MadLibsSentence(s1,POSDict1, POSDictBayesian)

s2='Banned in some parts of the United States, the Savannah elicits behavior not unlike that of its cheetah cousin.'
n2=POSWordList('noun',['Savannah','cheetah cousin'])
np2=POSWordList('plural noun',['behavior'])
POSDict2={n2.POS:n2.wordList,np2.POS:np2.wordList}
catSentence2=MadLibsSentence(s2,POSDict2, POSDictBayesian)

s3='Savannahs are noted for their tall and slender bodies and their large ears.'
n3=POSWordList('noun',[])
np3=POSWordList('plural noun',['bodies','ears'])
POSDict3={n3.POS:n3.wordList,np3.POS:np3.wordList}
catSentence3=MadLibsSentence(s3,POSDict3, POSDictBayesian)

s4='We have controlled our breeding process down to an exact science so everyone receives the perfect pet for their household.'
n4=POSWordList('noun',['breeding process','science','pet'])
np4=POSWordList('plural noun',[])
POSDict4={n4.POS:n4.wordList,np4.POS:np4.wordList}
catSentence4=MadLibsSentence(s4,POSDict4, POSDictBayesian)

s5='The carefully refined modern Siamese is characterized by blue almond-shaped eyes, a triangular head shape and a muscular body.'
n5=POSWordList('noun',['Siamese','head shape','body'])
np5=POSWordList('plural noun',['eyes'])
POSDict5={n5.POS:n5.wordList,np5.POS:np5.wordList}
catSentence5=MadLibsSentence(s5,POSDict5, POSDictBayesian)

s6='The Abyssinian, a breed of domestic short-haired cat, has a distinctive tabby coat, with individual hairs banded with different colors.'
n6=POSWordList('noun',['Abyssinian','short-haired cat','tabby coat'])
np6=POSWordList('plural noun',['hairs','colors'])
POSDict6={n6.POS:n6.wordList,np6.POS:np6.wordList}
catSentence6=MadLibsSentence(s6,POSDict6, POSDictBayesian)

#put cat MadLibs sentences into BayesianCatsMadLibs (we could separate the cat and Bayesian kinds if
# we wanted to weight them but this should leave your existing code working)
BayesianCatsMadLibs.sentences=BayesianCatsMadLibs.sentences+[catSentence1,catSentence2,catSentence3,catSentence4,catSentence5, catSentence6]

