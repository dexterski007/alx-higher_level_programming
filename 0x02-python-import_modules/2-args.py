#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nam = sys.argv[0]
    args = sys.argv[1:]
    totarg = len(args)
    if totarg == 1:
        print("{} argument:\n{}: {}".format(totarg, totarg, args[0]))
    elif totarg == 0:
        print("{} arguments.".format(totarg))
    else:
        print("{} arguments:".format(totarg))
        for i in range(totarg):
            print("{}: {}".format(i + 1, args[i]))
            i += 1
