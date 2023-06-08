#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    hidden = dir(hidden_4)
    for st in hidden:
        if not st[:2] == "__":
            print(st)
