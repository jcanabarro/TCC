import sys
from bagging import Bagging


def main():
    x = Bagging("C:\\Users\\Mateus\\Downloads\\TCC\\classifiers\\Monk.csv", 'MonkSubSet', 10, 100, 'Class')
    x.subset()


if __name__ == '__main__':
    main()