import TK_1
import TK_2
import TK_3
import TK_4
import importlib

def main():
    print('Testing started...')

    # TK_1.py
    print(TK_1.list_input(2))

    # TK_2.py
    print(TK_2.min_max([1, 2, 3, 4, 5, 15, 3123, 0]))

    # TK_3.py
    print(TK_3.div_list([1,3,5,7,8,23]))

    # TK-4.py
    print(TK_4.mul_list([1,6,32,765]))

    # TK-5.py
    TK_5 = importlib.import_module('TK-5')
    print(TK_5.sqrt_list([1,6,32,765]))

    print('Testing ended...')

if __name__ == '__main__':
    main()
