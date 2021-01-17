class RegexCharBase():
    def get(self):
        raise NotImplementedError('This method meant to be overriden by derived')

class Alphanumeric(RegexCharBase):
    def get(self):
        return '\w'

class NonAlphanumeric(RegexCharBase):
    def get(self):
        return '\W'

class Whitespace(RegexCharBase):
    def get(self):
        return '\s'

class Nonwhitespace(RegexCharBase):
    def get(self):
        return '\S'

class Decimal(RegexCharBase):
    def get(self):
        return '\d'

class NonDecimal(RegexCharBase):
    def get(self):
        return '\D'

class All(RegexCharBase):
    def get(self):
        return '.'

class Text(RegexCharBase):
    escaped_chars = ['\\', '|', '^', '$']
    def __init__(self, text):
        super().__init__()
        self.text = text

    def get(self):
        return [self._format_char(char) for char in self.text]

    def _format_char(self, char):
        return '\\' + char if char in Text.escaped_chars else char