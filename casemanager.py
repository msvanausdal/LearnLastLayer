import json
from termcolor import colored
import os


def parseCases(path):
    f = open(path)
    jsonData = json.load(f)
    caseList = []
    numCases = jsonData['numCases']
    for jsonCase in jsonData['cases']:
        caseList.append(Case(jsonCase['name'], jsonCase['data'], jsonCase['solution']))
    return numCases, caseList


def _color(data):
    if data == 'x':
        return colored('#', 'grey')
    elif data == 'o':
        return colored('#', 'magenta')
    elif data == 'g':
        return colored('#', 'green')
    elif data == 'b':
        return colored('#', 'blue')
    elif data == 'r':
        return colored('#', 'red')
    elif data == 'y':
        return colored('#', 'yellow')


def printCase(c):
    os.system('color')
    print(f" {_color(c.data[0])}{_color(c.data[1])}{_color(c.data[2])}")
    print(f"{_color(c.data[3])}{_color(c.data[4])}{_color(c.data[5])}{_color(c.data[6])}{_color(c.data[7])}")
    print(f"{_color(c.data[8])}{_color(c.data[9])}{_color(c.data[10])}{_color(c.data[11])}{_color(c.data[12])}")
    print(f"{_color(c.data[13])}{_color(c.data[14])}{_color(c.data[15])}{_color(c.data[16])}{_color(c.data[17])}")
    print(f" {_color(c.data[18])}{_color(c.data[19])}{_color(c.data[20])}")


class Case:
    def __init__(self, name, data, solution):
        self.name = name
        self.data = data
        self.solution = solution
