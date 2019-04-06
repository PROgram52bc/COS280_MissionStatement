# Infrastructure classes

class LanguageComponent:
    """ a base class representing a intermediate/leaf component in a language construct. """
    # contains multiple lists of derived classes
    # e.g. [[Noun, Verb, Noun],[Noun, Verb, Adverb],...]
    constructs = []
    # contains multiple strings
    collections = []

    def __init__(self, value=None, *args, **kwargs):
        # the actual value
        self.value = value
        self.setValue(value)

    def validValue(self, value):
        return True

    def setValue(self, value):
        """ validate value and set it to self.value"""
        if self.validValue(value):
            self.value = value
        else:
            raise ValueError("{} is not a valid value for {}".format(value, self.__class__.__name__))

    def getValue(self):
        return self.value

    @staticmethod
    def isLeaf():
        raise Exception("Can't call isLeaf on base class")

    def toHumanReadable(self, separator=" "):
        # Separate components by space by default
        # IDEA : have a PunctuatedClause that overrides this method to return something like __str__() + ','
        if self.value:
            if self.__class__.isLeaf():
                # is a leaf
                return self.value.__str__()
            else:
                # is a node
                return separator.join([l.__str__() for l in self.value])
        else:
            raise Exception("Cannot render human readable form of a {} without value".format(self.__class__.__name__))

    def __str__(self):
        return self.toHumanReadable()

class NodeComponent(LanguageComponent):
    """ a class representing a Node component in a language construct. e.g. a Sentence """
    collections = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    @staticmethod
    def isLeaf():
        return False

    @classmethod
    def addConstruct(cls, *args):
        cls.constructs.append(list(args))

class LeafComponent(LanguageComponent):
    """ a class representing a leaf component in a language construct. e.g. a Noun """
    constructs = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def isLeaf():
        return True
