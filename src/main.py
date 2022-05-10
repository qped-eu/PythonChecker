from sys import exit, stderr
from parser import Parser
import json

def main(filename):
    try:
        #filename = "./output.txt"
        #f = open(filename)
        #fileparser = Parser(f)
        errors = []

        qf = open('qf.json', 'w')
        qf['feedback'] = {};

        # for path, code, line, char, description in fileparser.parse():
        #    errors.append((code, line, char, description))

        qf['feedback'] = "hola"
        qf.close()


    except IOError as e:
        stderr.write('Could not open file: %s' % e)
        stderr.flush()
        exit(1)
