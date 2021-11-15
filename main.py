import importlib
import TK_1
import TK_2
import TK_3
import TK_4

def main():
    print('Testing started...')

    # TK_1.py
    print(TK_1.list_input(2))

    # TK_2.py
    print(TK_2.min_max([1, 2, 3, 4, 5, 15, 3123, 0]))

    # TK_3.py
    print(TK_3.div_list([1, 2, 8]))

    # TK_4.py
    print(TK_4.mul_list([1,6,32,765]))

    # TK_5.py
    print(TK_4.sqrt_list([1, 6, 32, 765]))

    print('Testing ended...')

if __name__ == '__main__':
    main()

