""" Simple script to return Prime Factors of a given number"""

import sys
sys.path.append('.')

from solution import prime_factors


def main():
    if len(sys.argv) < 2:
        print('No argument given')
        exit(1)
    else:
        number = sys.argv[1]
        if not number.isdigit():
            print('Please give me a number')
            exit(2)
        result = prime_factors(number)
        print(result)
        return result


if __name__ == '__main__':
    main()
