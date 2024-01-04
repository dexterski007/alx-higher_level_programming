#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    listd = dir(hidden_4)
    leng = len(listd)
    for i in range(leng):
        txt = listd[i]
        if not txt.startswith("__"):
            print("{}".format(txt))
