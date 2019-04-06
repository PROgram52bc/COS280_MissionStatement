from components import LeafComponent, NodeComponent
from generate import getRandom
# Custom classes

# --- Leaf components
class Noun(LeafComponent):
    pass
Noun.addToCollection("ideas", "knowledge", "oceans", "warriors")

class Preposition(LeafComponent):
    pass
Preposition.addToCollection("about", "below", "excepting", "off", "toward", "above", "beneath", "for", "on", "under", "across", "beside", "from", "onto", "underneath", "after", "between", "in", "out", "until", "against", "beyond", "in front of", "outside", "up", "along", "but", "inside", "over", "upon", "among", "by", "in spite of", "past", "up to", "around", "concerning", "instead of", "regarding", "with", "at ", "despite", "into", "since", "within", "because of", "down", "like", "through", "without", "before", "during", "near", "throughout", "with regard to", "behind", "except", "of", "to", "with respect to")

# class ProperNoun(LeafComponent):
#     pass
# ProperNoun.addToCollection()
# 
# class ProperNoun(LeafComponent):
#     pass
# ProperNoun.addToCollection()
# 
# class ProperNoun(LeafComponent):
#     pass
# ProperNoun.addToCollection()
# 
# class ProperNoun(LeafComponent):
#     pass
# ProperNoun.addToCollection()

class Verb(LeafComponent):
    pass
Verb.addToCollection("create", "bring", "inspire", "increase")

# --- Node components
class PrepositionalPhrase(NodeComponent):
    pass
PrepositionalPhrase.addConstruct(Preposition, Noun)

# class Statement(NodeComponent):
#     pass
# Statement.addConstruct()
# 
# class Statement(NodeComponent):
#     pass
# Statement.addConstruct()
# 
# class Statement(NodeComponent):
#     pass
# Statement.addConstruct()
# 
# class Statement(NodeComponent):
#     pass
# Statement.addConstruct()

class Statement(NodeComponent):
    pass
Statement.addConstruct(PrepositionalPhrase)


if __name__ == "__main__":
    st = Statement.random()
    print(str(st))
