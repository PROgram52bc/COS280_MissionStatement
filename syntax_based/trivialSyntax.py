from components import LeafComponent, NodeComponent
# Custom classes

class Noun(LeafComponent):
    """ A Noun """
    pass
Noun.addToCollection("John", "Mary")

class Verb(LeafComponent):
    """ A Verb """
    pass
Verb.addToCollection("loves", "hates")

class Sentence(NodeComponent):
    """ A Sentence """
Sentence.addConstruct(Noun, Verb, Noun)

if __name__ == "__main__":
    obj = Sentence.random()
    print(obj.toHumanReadable())
