from singleton import SingletonBasedOnMeta


if __name__ == '__main__':
    print('SingletonBasedOnMeta:')

    test_meta = SingletonBasedOnMeta()
    print(test_meta)

    test_meta1 = SingletonBasedOnMeta()
    print(test_meta1)
