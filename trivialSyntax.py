from components import LeafComponent, NodeComponent
from generate import getRandom
# Custom classes

class Noun(LeafComponent):
    """ A Noun """
    collections = LeafComponent.collections + ['John', 'Mary']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Verb(LeafComponent):
    """ A Verb """
    collections = LeafComponent.collections + ['loves', 'hates']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Sentence(NodeComponent):
    """ A Sentence """
    NodeComponent.addConstruct(Noun, Verb, Noun)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

if __name__ == "__main__":
    obj = getRandom(Sentence)
    print(obj.toHumanReadable())
