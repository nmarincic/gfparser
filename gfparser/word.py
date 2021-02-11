# AUTOGENERATED! DO NOT EDIT! File to edit: 03_word.ipynb (unless otherwise specified).

__all__ = ['Word']

# Cell
from .wordtype import format_caption
from .config import _line_width

# Cell
class Word:
    def __init__(self, title, page_id, wikitext, url):
        self.title = title
        self.pageid = page_id
        self.wikitext = wikitext
        self.url = url
        self.word_types = []

    def __repr__(self):
        return self.title

    def __eq__(self, other):
        if hash(self) == hash(other):
            return True
        return False

    def __hash__(self):
        return hash(self.wikitext)

    def __str__(self):
        print (format_caption(self.title, _line_width, '='))
        for word_type in self.word_types:
            print (word_type)
        return ''