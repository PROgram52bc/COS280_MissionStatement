from components import LeafComponent, NodeComponent
# Custom classes

# --- Leaf components
class Noun(LeafComponent):
    pass
Noun.addToCollection("ideas", "warriors", "knowledge", "reproduction", "protection", "exhibition", "excellence", "education", "quality", "love","anger","hate", "peace","loyalty","integrity", "pride","courage","deceit", "honesty","trust","compassion", "bravery","misery","childhood","patriotism","friendship")

class ProperNoun(LeafComponent):
    pass
ProperNoun.addToCollection("America's National Park System", "San Diego Zoo", "American Red Cross", "the U.S. Fund for UNICEF", "Donald Trump")

class RelativePronoun(LeafComponent):
    pass
RelativePronoun.addToCollection("that", "which", "of those who", "for those who", "through those who")

class SubordinateConjunction(LeafComponent):
    pass
SubordinateConjunction.addToCollection("as", "in order that", "on which", "by which", "through which")

class Adjective(LeafComponent):
    pass
Adjective.addToCollection("excellent", "life-threatening", "poor", "better", "challenging", "natural", "lasting")

class Verb(LeafComponent):
    pass
Verb.addToCollection("create", "bring", "inspire", "increase", "mobilize", "undertake", "develop", "support", "engage in")

class Preposition(LeafComponent):
    pass
Preposition.addToCollection("about", "below", "off", "toward", "above", "beneath", "for", "on", "under", "across", "beside", "from", "onto", "underneath", "after", "between", "in", "out", "until", "against", "beyond", "in front of", "outside", "up", "along", "but", "inside", "over", "upon", "among", "by", "in spite of", "past", "up to", "around", "concerning", "instead of", "regarding", "with", "at", "despite", "into", "since", "within", "because of", "down", "like", "through", "without", "before", "during", "near", "throughout", "with regard to", "behind", "of", "to", "with respect to")

# --- Node components
class PrepositionalPhrase(NodeComponent):
    pass
PrepositionalPhrase.addConstruct(Preposition, Noun)

class NounPhrase(NodeComponent):
    pass
NounPhrase.addConstruct("the", Noun)
NounPhrase.addConstruct(Adjective, Noun)
NounPhrase.addConstruct(ProperNoun)
NounPhrase.addConstruct("the", Noun, "and", Noun)

class VerbPhrase(NodeComponent):
    pass
VerbPhrase.addConstruct(Verb)
VerbPhrase.addConstruct(Verb, "and", Verb)

class SubordinateClause(NodeComponent):
    pass
SubordinateClause.addConstruct(RelativePronoun, VerbPhrase, NounPhrase)
SubordinateClause.addConstruct(SubordinateConjunction, NounPhrase, VerbPhrase, NounPhrase)

class Statement(NodeComponent):
    pass
Statement.addConstruct("to", VerbPhrase, NounPhrase, SubordinateClause)
Statement.addConstruct("to", VerbPhrase, PrepositionalPhrase, "to", VerbPhrase, NounPhrase)
Statement.addConstruct("we", VerbPhrase, NounPhrase, PrepositionalPhrase)


if __name__ == "__main__":
    st = Statement.random()
    print(str(st))
