import random
def getRandom(componentClass):
    leaf = componentClass.isLeaf()
    sequence = componentClass.collections if leaf else componentClass.constructs
    value = random.choice(sequence)
    if leaf:
        instance = componentClass(value)
    else:
        value = [getRandom(cc) for cc in value]
        instance = componentClass(value)
    return instance
