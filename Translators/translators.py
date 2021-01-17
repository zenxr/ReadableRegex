from .base import ReadableBase
from .characters import RegexCharBase

def RegexFactory(name, *args):
    return ReadableBase(args)

class ReadableBase(object):
    def __init__(self):
        self.child = None

    def convert(self):
        return

    def __str__(self):
        return

    def _to_regex(self):
        raise TypeError('This method meant to be overriden by derived classes.')

    def _selfstr(self):
        raise TypeError('This method meant to be overriden by derived classes.')

    def __getattr__(self, name: str, *args):
        generated_object = RegexFactory(name)
        if not generated_object:
            raise AttributeError(f"{self} has no attribute '{name}' and '{name} is not a valid RegexTranslator")
        self.child = generated_object
        return self.child

class ReadableCharsBase(ReadableBase):
    def __init__(self, text: RegexCharBase):
        super().__init__()
        self.text = text

    def convert(self):
        raise TypeError('This method meant to be overriden by derived classes.')

class OneOrMore(ReadableCharsBase):
    def convert(self):
        return

class ZeroOrMore(ReadableCharsBase):
    def convert(self):
        return

class StartsWith(ReadableBase):
    def convert(self):
        return self.child._to_regex + '$'

    def __str__(self):
        return 'ends with ' + str(self.child)

class EndsWith(ReadableBase):
    def __init__(self, text: RegexCharBase):
        super().__init__()

    def convert(self):
        return '^' + self.child.convert()

    def __str__(self):
        return 'starts with ' + str(self.child)

# TODO this is not a ReadableBase inheritor; this should be a choice when searching
class Multiline(ReadableBase):
    def __init__(self, text: RegexCharBase):
        super().__init__()

    def convert(self):
        return