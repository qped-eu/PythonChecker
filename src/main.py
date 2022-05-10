from sys import exit, stderr
from parser import Parser
from error import Error
import json


def main(filename):
    try:



        #read flake8 output file
        filename = "./output.txt"
        f = open(filename)
        fileparser = Parser(f)
        errors = []

        #read qf.json
        json_file = open('qf.json')
        qf = json.load(json_file)
        json_file.close()

        for path, code, line, char, description in fileparser.parse():
            #errors.append((code, line, char, description))
            errors.append(Error(path,code,line,char))

        for error in errors:
            qf['feedback'].append(error.toString())

        #qf['feedback'] = errors

        #Write qf.json
        json_file = open('qf.json', 'w')
        json.dump(qf, json_file)
        json_file.close()

    except IOError as e:
        stderr.write('Could not open file: %s' % e)
        stderr.flush()
        exit(1)


if __name__ == '__main__':
    main('hola')
