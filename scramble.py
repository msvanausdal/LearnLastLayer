import random


def scramble(numScrambles=1):
    moves = ['F', 'B', 'U', 'D', 'R', 'L']
    modifiers = [' ', '\' ', '2 ']
    random.seed()
    lastMove = 7
    for i in range(numScrambles):
        moveList = ''
        for j in range(20):
            while True:
                currentMove = random.randrange(len(moves))
                if currentMove != lastMove:
                    if currentMove % 2 == 0:
                        if currentMove != currentMove + 1:
                            break
                    else:
                        if currentMove != currentMove - 1:
                            break
            moveList += moves[currentMove]
            lastMove = currentMove
            currentMod = random.randrange(len(modifiers))
            moveList += modifiers[currentMod]
        print(moveList)
