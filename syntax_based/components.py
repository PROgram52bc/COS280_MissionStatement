# Infrastructure classes
class LanguageComponentMeta(type):
    def __new__(cls, clsname, bases, dct):
        dct['bank'] = [] # initialize a new list for every inherited class
        return super().__new__(cls, clsname, bases, dct)


class LanguageComponent(metaclass=LanguageComponentMeta):
    """ a base class representing a intermediate/leaf component in a language construct. """

    def __init__(self, value=None, *args, **kwargs):
        # the actual value
        self.setValue(value)

    def validValue(self, value):
        # redefine this
        return True

    def setValue(self, value):
        """ validate value and set it to self.value"""
        if self.validValue(value):
            self.value = value
        else:
            raise ValueError("{} is not a valid value for {}".format(value, self.__class__.__name__))

    def getValue(self):
        return self.value

    def toHumanReadable(self):
        # Redefine this in subclass
        # IDEA : have a PunctuatedClause that overrides this method to return something like __str__() + ','
        raise Exception("Undefined toHumanReadable method in {}".format(self.__class__))

    def __str__(self):
        return self.toHumanReadable()

class NodeComponent(LanguageComponent):
    """ a class representing a Node component in a language construct. e.g. a Sentence """
    # contains multiple lists of derived classes
    # e.g. [[Noun, Verb, Noun],[Noun, Verb, Adverb],...]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def addConstruct(cls, *args):
        cls.bank.append(list(args))

    @staticmethod
    def isLeaf():
        return False

    def toHumanReadable(self, separator=" "):
        # Separate components by space by default
        if self.value:
            return separator.join([l.__str__() for l in self.value])
        else:
            raise Exception("Cannot render human readable form of a {} without value".format(self.__class__.__name__))

class LeafComponent(LanguageComponent):
    """ a class representing a leaf component in a language construct. e.g. a Noun """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def addToCollection(cls, *args):
        cls.bank += list(args)

    @staticmethod
    def isLeaf():
        return True

    def toHumanReadable(self, separator=" "):
        # Separate components by space by default
        if self.value:
            return str(self.value)
        else:
            raise Exception("Cannot render human readable form of a {} without value".format(self.__class__.__name__))

