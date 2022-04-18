import sys
import categories
from scramble import scramble


if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        # print(f"Arg: {arg}, Next: {sys.argv[i+1] if (i < len(sys.argv)-1) else None}")
        if arg == '-s':
            # Shows a random scramble algorithm for a solved cube. If the next argument is an integer, it shows that
            # many cube scrambles
            if i < len(sys.argv) - 1 and sys.argv[i+1].isdigit():
                scramble(int(sys.argv[i+1]))
            else:
                scramble()
        if arg == '-bpll':
            categories.bpll()
        if arg == '-boll':
            categories.boll()
