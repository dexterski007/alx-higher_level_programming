#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nam = sys.argv[0]
    args = sys.argv[1:]
    totarg = len(args)
    sums = 0
#    if totarg == 1:
#        print("{} argument:\n{}: {}".format(totarg, totarg, args[0]))
#    elif totarg == 0:
#        print("{} arguments.".format(totarg))
    for i in range(totarg):
        sums += int(args[i])
    print(sums)
