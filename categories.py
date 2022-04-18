import casemanager
import random


def bpll():
    numCases, caseList = casemanager.parseCases('data/bpll.txt')
    random.seed()
    casemanager.printCase(caseList[random.randrange(numCases)])


def boll():
    numCases, caseList = casemanager.parseCases('data/boll.txt')
    random.seed()
    casemanager.printCase(caseList[random.randrange(numCases)])
