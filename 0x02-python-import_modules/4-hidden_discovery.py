#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    allfun = dir()
    for a in range(0, len(allfun)):
        if allfun[a][:2] != "__":
            print("{:s}".format(allfun[a]))
