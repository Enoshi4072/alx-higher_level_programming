#!/usr/bin/python3
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Addition that is infinite')
    parser.add_argument(
            'nums',
            type=int,
            nargs='*',
            default=[0],
            help='Enter nums to add'
            )
    argums = parser.parse_args()
    answer = sum(argums.nums)
    print(answer)
