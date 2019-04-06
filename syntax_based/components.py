import random
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

    @classmethod
    def random(cls, noRepeat=True, usedValues=[]):
        """ get a random element with values set recursively """
        sequence = cls.bank
        if len(sequence) == 0:
            raise Exception("Can't get random value for {} when its bank is empty.".format(cls))
        # choose a value to set to the instance
        value = random.choice(sequence)
        while noRepeat and value in usedValues:
            value = random.choice(sequence)
        usedValues.append(value)

        def instantiate(element, usedValues=[]):
            """ Try to instantiate a LanguageComponent subclass
            if element is a string instance, return it. 
            Otherwise, raise an exception. """
            if isinstance(element, LanguageComponentMeta):
                return element.random(True, usedValues)
            elif isinstance(element, str):
                return element
            else:
                raise Exception(
                        "can't instantiate element {}! (has to be a string or a subclass of LanguageComponent)"
                        .format(element, value))
            
        if isinstance(value, list):
            # go through the list and instantiate when needed
            instantiatedValues = []
            for element in value:
                instantiatedValues.append(instantiate(element,usedValues))
            instance = cls(instantiatedValues)
        else:
            instance = cls(value)

        return instance

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
    # can also include direct strings
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
            return separator.join([str(l) for l in self.value])
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

