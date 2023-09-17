#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=""):
        if type(value) != str:
            print("The value must be a string.")
            self._value = ""
        else:
            self._value = value
      
    @property
    def is_sentence(self):
        return self._value.endswith(".")

    @property
    def is_question(self):
        return self._value.endswith("?")

    @property
    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        if not self._value:
            return 0
        sentences = re.split(r'[.!?]', self._value)
        return len([s for s in sentences if s.strip()])

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if type(new_value) != str:
            print("The value must be a string.")
        else:
            self._value = new_value

