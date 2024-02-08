#!/usr/bin/python3

if __name__ == "__main__":
    """don'tr read."""
    import hidden_4

    na = dir(hidden_4)
    for name in na:
        if name[:2] != "__":
            print(name)
