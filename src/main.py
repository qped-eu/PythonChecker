from sys import exit, stderr
from parser import Parser
import json

def main(filename):
    try:
        #filename = "./output.txt"
        #f = open(filename)
        #fileparser = Parser(f)
        errors = []

        json_file = open('qf.json')
        qf = json.load(json_file)
        json_file.close()

        qf['feedback'] = {"patata","pera"}

        # for path, code, line, char, description in fileparser.parse():
        #    errors.append((code, line, char, description))

        #qf['feedback'] = {"hola"}
        json_file = open('qf.json','w')
        json.dump(qf, json_file)
        json_file.close()


    except IOError as e:
        stderr.write('Could not open file: %s' % e)
        stderr.flush()
        exit(1)

if __name__ == '__main__':
    main('hola')
