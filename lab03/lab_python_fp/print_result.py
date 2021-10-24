def print_result(func_to_decorate):
    def wrapper(*args, **kwargs):
        #print(func_to_decorate.__name__)
        res = func_to_decorate(*args, **kwargs)
        if type(res) == list:
            print(*res, sep = "\n")
        elif type(res) == dict:
            for k, v in res.items():
                print(k, '=', v)
        else:
            print(res)

    return wrapper

'''
@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
    
'''