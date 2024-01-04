#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    listd = dir(hidden_4)
    l = len(listd)
    for i in range(l):
        txt = listd[i]
        if not txt.startswith("__"):
            print("{}".format(txt))
