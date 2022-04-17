import sys
import random


def scramble(numScrambles=1):
    moves = ['F', 'B', 'U', 'D', 'R', 'L']
    modifiers = [' ', '\' ', '2 ']
    random.seed()
    lastMove = 7
    currentMove = 0
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


if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        # print(f"Arg: {arg}, Next: {sys.argv[i+1] if (i < len(sys.argv)-1) else None}")
        if arg == '-s':
            if i < len(sys.argv) - 1 and sys.argv[i+1].isdigit():
                scramble(int(sys.argv[i+1]))
            else:
                scramble()
