
class ErrorToken(Exception):
    def __init__(self,s):
        self.message = "Error Token "+ s

class UnclosedString(Exception):
    def __init__(self,s):
        self.message = "Unclosed String: "+ s

class IllegalEscapeInString(Exception):
    def __init__(self,s):
        self.message = "Illegal Escape In String: "+ s

class IllegalCharInString(Exception):
    def __init__(self,s):
        self.message = "Illegal Char In String: "+ s

