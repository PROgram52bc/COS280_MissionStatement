## templates are stored in the getSentence() function.  to add a template, simply
## create a new variable to store the template and add it to the templates list
import random

wordDict = {"sNoun":["despair","growth","knowledge","conservation","information","health","learning","prevention","hunger","poverty"],
            "pNoun":["humans","countries","diseases","solutions","problems","communities","leaders","ecosystems","experiences","animals"],
            "verb":["protect","lead","provide","love","increase","develop","serve","improve","achieve","enhance"],
            "adj":["worldwide","current","precise","top-notch","high quality","effective","vulnerable","life-threatening","impressive","innovative"],
            "prep":["with","into","for","of","in addition to","without","for the purpose of","in","through","using"]}

def getWord(wordType):
    word = random.choice(wordDict[wordType])
    return word

def getAllWords(wordCount):
    words = {"sNoun":[],"pNoun":[],"verb":[],"adj":[],"prep":[]}
    wordTypes = wordCount.keys()
    for wType in wordTypes:
        for i in range(wordCount[wType]):
            word = getWord(wType)
            while word in words[wType]:
                word = getWord(wType)
            words[wType].append(word)
    return words

def countTypes(sentence):
    words = {"sNoun":0,"pNoun":0,"verb":0,"adj":0,"prep":0}
    for word in words:
        words[word] = sentence.count(word)
    return words


def createSentence(form,wordCount):
    words = getAllWords(wordCount)
    sentence = form
    wordTypes = wordCount.keys()
    for wType in wordTypes:
        while wType in sentence:
            word = words[wType][0]
            sentence = sentence.replace(wType,word,1)
            words[wType].remove(word)
    return sentence

def getSentence():
    temp1 = "To verb sNoun prep adj pNoun prep sNoun."
    temp2 = "To verb adj sNoun prep pNoun, verb sNoun prep pNoun, and verb further sNoun of those who verb."
    temp3 = "We verb pNoun to verb sNoun prep sNoun of our pNoun."
    temp4 = "Why verb sNoun when you can verb pNoun?"
    temp5 = "To bring together sNoun, sNoun, and pNoun from all nations."
    templates = [temp1,temp2,temp3,temp4,temp5]
    wordCounts = []
    for temp in templates:
        wordCounts.append(countTypes(temp))
    idx = random.randrange(0,len(templates))
    template = templates[idx]
    wordCount = wordCounts[idx]
    return createSentence(template,wordCount)

def main():
    print('\n' + "Welcome to the Random Mission Statement Generator (template based)!" + '\n')
    while True:
        amount = input("How many mission statements would you like to generate? => ")
        if amount == "quit":
            break
        for i in range(int(amount)):
            print()
            print("Statement " + str(i+1) + ":")
            print(getSentence())
        print()
        cont = input("Generate more? (type 'q' to quit) ")
        if cont == 'q':
            break

main()
