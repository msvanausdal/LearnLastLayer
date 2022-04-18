import casemanager
import random


def printCategory(path):
    numCases, caseList = casemanager.parseCases('path')
    random.seed()
    casemanager.printCase(caseList[random.randrange(numCases)])
