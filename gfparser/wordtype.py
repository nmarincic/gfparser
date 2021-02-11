# AUTOGENERATED! DO NOT EDIT! File to edit: 01_wordtype.ipynb (unless otherwise specified).

__all__ = ['santa', 'format_caption', 'WordType']

# Cell
from fastcore.test import *
from .config import _line_width
from prettytable import PrettyTable

# Cell
def santa(feature):
    "Prints a list of elements as strings, and connects them with commas"
    feat_len = len(feature)
    for i, f in enumerate(feature):
        if (feat_len-i>1):
            print (f'{f}, ', end = '')
        else:
            print (f'{f}')

# Cell
def format_caption(text, no_lines, delimiter):
    output = delimiter[0] * no_lines +"\n"
    cen = text.center(no_lines-2*len(delimiter), ' ')
    output += delimiter + cen + delimiter[::-1] + "\n"
    output += delimiter[0] * no_lines
    return output

# Cell
class WordType:
    """Stores a word type (noun, verb, adjective, etc.) of a specific german word (Hund, Katze, etc.)
    Attributes:
    word: a german word
    name: name of the word type
    wikitext: wikitext for the current word type extracted from wiktionary"""
    def __init__(self, word, name, wikitext):
        self.word = word
        self.name = name
        self.wikitext = wikitext

        self.substantiv = ''
        self.verb = ''
        self.IPA = ''
        self.adjektiv = ''
        self.pronomen = ''
        self.article = ''
        self.examples = ''

    """Returns the type of the word.
    """
    def __repr__(self):
        return self.name

    """Defines when two word types are equal.
    """
    def __eq__(self, other):
        if hash(self) == hash(other):
            return True
        return False

    """Hash is defined in terms of the wikitext.
    """
    def __hash__(self):
        return hash(self.wikitext)

    """
    Prints all the information about the word type.
    """
    def __str__(self):
#         print (format_caption(self.word,_line_width,'-'))
        print (format_caption(self.name, _line_width, ' '))
        self.print_ipa()
        print ()
        self.print_substantive()
        self.print_verb()
        self.print_pronomen(self.pronomen)
        self.print_adjektive()
        print ()
        self.print_examples()
        return ''

    """Prints the International phonetic alphabet representation.
    """
    def print_ipa(self):
        if self.IPA:
            IPA = ['['+i+']' for i in self.IPA]
            santa(IPA)
        else:
            print ('[]')

    """Prints out the sentance examples using the current word in its type.
    """
    def print_examples(self):
        if self.examples:
            for i, example in enumerate(self.examples):
                print (f'{i+1}: {example}')

    """Prints pronouns.
    """
    def print_pronomen(self, pronomen):
        if self.pronomen:
            t = PrettyTable([' ','Masculine', 'Feminine', 'Neuter', 'Plural'])
            t.add_row(['Nominativ',
                   pronomen['Nominativ Singular m'][0],
                   pronomen['Nominativ Singular f'][0],
                   pronomen['Nominativ Singular n'][0],
                   pronomen['Nominativ Plural'][0]])
            t.add_row(['Genitiv',
                   pronomen['Genitiv Singular m'][0],
                   pronomen['Genitiv Singular f'][0],
                   pronomen['Genitiv Singular n'][0],
                   pronomen['Genitiv Plural'][0]])
            t.add_row(['Dativ',
                   pronomen['Dativ Singular m'][0],
                   pronomen['Dativ Singular f'][0],
                   pronomen['Dativ Singular n'][0],
                   pronomen['Dativ Plural'][0]])
            t.add_row(['Akkusativ',
                   pronomen['Akkusativ Singular m'][0],
                   pronomen['Akkusativ Singular f'][0],
                   pronomen['Akkusativ Singular n'][0],
                   pronomen['Akkusativ Plural'][0]])
            print(t)

    """Prints out noun information of the current word.
    """
    def print_substantive(self):
        if self.substantiv:
            santa(self.substantiv[0])
            santa(self.substantiv[1])

    """Prints out verb information of the current word.
    """
    def print_verb(self):
        if self.verb:
            santa(self.verb[0])
            santa(self.verb[1])

            len_partizip_ii = len(self.verb[2])
            len_hilfsverb = len(self.verb[3])

            if (len_hilfsverb==1):
                v = self.verb[3][0]
                for k, pzip in enumerate(self.verb[2]):
                    if (len_partizip_ii-k>1):
                        print (f'{v} {pzip}, ', end = '')
                    else:
                        print (f'{v} {pzip}')
            else:
                for l, hilfs in enumerate(self.verb[3]):
                    for k, pzip in enumerate(self.verb[2]):
                        if (len_partizip_ii-k>1):
                            print (f'{hilfs} {pzip}', end = '')
                        else:
                            print (f'{hilfs} {pzip}')

    """Prints out adjective information of the current word.
    """
    def print_adjektive(self):
        if self.adjektiv:
            santa(self.adjektiv[0])
            santa(self.adjektiv[1])
            santa(self.adjektiv[2])