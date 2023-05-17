"""CSE-111 BYU-I Prove assignment. Based on Turing's test, this program will generate random phrases."""
#Heitor Cazado
#Brother Christofferson

import random

def main():
    p1 = make_sentence(1, "past")
    p2 = make_sentence(1, "present")
    p3 = make_sentence(1, "future")
    p4 = make_sentence(2, "past")
    p5 = make_sentence(2, "present")
    p6 = make_sentence(2, "future")
    
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(p5)
    print(p6)


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
     
     #Randomly choose a noun
    noun = random.choice(nouns)
    
    return noun    
    
def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense.lower() == "past":
        
        verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    
    elif tense.lower() == "present" and quantity == 1:
        
        verbs = [ "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
        
    elif tense.lower() == "present" and quantity != 1:
        
        verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
        
    elif tense.lower() == "future":
        
        verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    #Picking up a random verb from the appropriate list of verbs
    verb = random.choice(verbs)
    
    return verb

def get_adjective():
    """Return a randomly chosen adjective
    from this list of adjectives: 
        "good","new","great","little","old","big","high","small","large","hungry",
        "young","important","smart","tall","bad","sad","happy"""
    
    adjectives = ["good","new","great","little","old","big","high","small","large","hungry",
        "young","important","smart","tall","bad","sad","happy"]
    
    adjective = random.choice(adjectives)
    
    return adjective

def get_adverb():
    """Return a randomly chosen adverb
    from this list of adverbs: 
        "angrily","anxiously","awkwardly","beautifully","boldly","bravely","brightly",
        "calmly","carefully","cheerfully","clearly","courageously","doubtfully","enthusiastically",
        "faithfully","fatally","fiercely","fondly","gently","gladly","gracefully","happily",
        "honestly","innocently","kindly","mysteriously","openly","successfully","suddenly",
        "suspiciously"""   
    
    adverbs = ["angrily","anxiously","awkwardly","beautifully","boldly","bravely","brightly",
        "calmly","carefully","cheerfully","clearly","courageously","doubtfully","enthusiastically",
        "faithfully","fatally","fiercely","fondly","gently","gladly","gracefully","happily",
        "honestly","innocently","kindly","mysteriously","openly","successfully","suddenly",
        "suspiciously"]
    
    adverb = random.choice(adverbs)
    
    return adverb

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
     
    Return: a randomly chosen preposition.
    """
    
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    #Randomly choosing a preporisition
    preposition = random.choice(prepositions)
    
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    
    preposition = get_preposition()
    
    determiner = get_determiner(quantity)
    
    noun = get_noun(quantity)
    
    #Building random prepositional phrase
    prepositional_phrase = f"{preposition} {determiner} {noun}"
    
    return prepositional_phrase
     
    
def make_sentence(quantity, tense):
    """Build and return a sentence. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    determiner = get_determiner(quantity)
    
    determiner_2 = get_determiner(quantity)
    
    noun = get_noun(quantity)
    
    noun_2 = get_noun(quantity)
    
    verb = get_verb(quantity, tense)
    
    adverb = get_adverb()
    
    adjective = get_adjective()
    
    adjective_2 = get_adjective()
    
    prepositional_phrase = get_prepositional_phrase(quantity)
    
    prepositional_phrase_2 = get_prepositional_phrase(quantity)
    
    #Building phrase
    phrase = f"{determiner.capitalize()} {adjective} {noun} {prepositional_phrase} {adverb}"\
                f" {verb} {determiner_2} {adjective_2} {noun_2} {prepositional_phrase_2}"
    
    return phrase
    
main()