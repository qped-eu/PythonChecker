from sys import exit, stderr
from parser import Parser
from error import Error
import json


def main(filename):
    try:
        # read flake8 output file
        f = open(filename)
        fileparser = Parser(f)
        errors = []

        # read qf.json
        json_file = open('qf.json')
        qf = json.load(json_file)
        json_file.close()

        qf['feedback'] = []

        # for path, code, line, char, description in fileparser.parse():
        #   error = Error(path,code,line,char)
        #   qf['feedback'].append(error.toString()) #toString or toMarkdown

        for path, code, line, char, description in fileparser.parse():
            errors.append(Error(path, code, line, char))

        syntaxerrors = list(filter(lambda err: err.type == "SYNTAX", errors))

        if len(syntaxerrors) != 0:
            qf['feedback'].append("## Syntax errors")

        for error in syntaxerrors:
            qf['feedback'].append(error.toMarkdown())

        if 'mainSettings' in qf and 'semanticNeeded' in qf['mainSettings'] and qf['mainSettings'][
            'semanticNeeded'] == 'true':

            semanticerrors = list(filter(lambda err: err.type == "SEMANTIC", errors))

            if len(semanticerrors) != 0:
                qf['feedback'].append("## Semantic errors")

            for error in semanticerrors:
                qf['feedback'].append(error.toMarkdown())

        if 'mainSettings' in qf and 'styleNeeded' in qf['mainSettings'] and qf['mainSettings'][
            'styleNeeded'] == True:

            styleerrors = list(filter(lambda err: err.type == "STYLE", errors))

            if len(styleerrors) != 0:
                qf['feedback'].append("## Style errors")

            for error in styleerrors:
                qf['feedback'].append(error.toMarkdown())

        # Write qf.json
        json_file = open('qf.json', 'w')
        json.dump(qf, json_file)
        json_file.close()

    except IOError as e:
        stderr.write('Could not open file: %s' % e)
        stderr.flush()
        exit(1)


if __name__ == '__main__':
    main("./output.txt")
