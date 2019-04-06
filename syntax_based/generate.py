import random

def getRandom(componentClass, noRepeat=True, usedValues=[]):
    leaf = componentClass.isLeaf()
    sequence = componentClass.bank
    value = random.choice(sequence)
    if leaf:
        # is a leaf
        while noRepeat and value in usedValues:
            # NOTE: this will break if sequence contains too few words
            value = random.choice(sequence)
        usedValues.append(value)
        instance = componentClass(value)
    else:
        # is a node
        value = [getRandom(cc, usedValues) for cc in value]
        instance = componentClass(value)
    return instance
