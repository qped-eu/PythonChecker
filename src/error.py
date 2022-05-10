class Error:

    def __init__(self, fileName, code, line, column):
        self.msgsSyntax = self.load_properties("./flake8-syntax-msgs.properties")

        self.msgsSemantic = self.load_properties("./flake8-semantic-msgs.properties")

        self.msgsStyle = self.load_properties("./flake8-style-msgs.properties")

        self.fileName = fileName
        self.code = code
        self.line = line
        self.column = column

        if code in self.msgsSyntax:
            self.type = "SYNTAX"
            self.msg = self.msgsSyntax['syntax'][code]
        else:
            if code in self.msgsSemantic:
                self.type = "SEMANTIC"
                self.msg = self.msgsSemantic['semantic'][code]
            else:
                self.type = "STYLE"
                self.msg = self.msgsStyle['style']['E101'] #self.msgsStyle[code]

    def toString(self):
        return self.type + " - " + self.code + " (" + self.line + "," + self.column + ") --> " + self.msg

    def load_properties(self,filepath, sep='=', comment_char='#'):
        """
        Read the file passed as parameter as a properties file.
        """
        props = {}
        with open(filepath, "rt") as f:
            for line in f:
                l = line.strip()
                if l and not l.startswith(comment_char):
                    key_value = l.split(sep)
                    key = key_value[0].strip()
                    value = sep.join(key_value[1:]).strip().strip('"')
                    props[key] = value
        return props
