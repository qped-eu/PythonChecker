import configparser


class Error:

    def __init__(self, fileName, code, line, column):
        self.msgsSyntax = configparser.ConfigParser()
        self.msgsSyntax.read("../flake8-syntax-msgs.properties")

        self.msgsSemantic = configparser.ConfigParser()
        self.msgsSemantic.read("../flake8-semantic-msgs.properties")

        self.msgsStyle = configparser.ConfigParser()
        self.msgsStyle.read("../flake8-style-msgs.properties")

        self.fileName = fileName
        self.code = code
        self.line = line
        self.column = column

        if code in self.msgsSyntax:
            self.type = "SYNTAX"
            self.msg = self.msgsSyntax[code]
        else:
            if code in self.msgsSemantic:
                self.type = "SEMANTIC"
                self.msg = self.msgsSemantic[code]
            else:
                self.type = "STYLE"
                self.msg = self.msgsStyle #self.msgsStyle[code]

    def toString(self):
        return self.type + " - " + self.code + " (" + self.line + "," + self.column + ") --> " + self.msg
