def fizzBuzzWoof():
    for i in range(1, 101):
        string = ''
        string += f'{i} '
        if i % 3 == 0: string += 'fizz '
        if i % 3 == 0: print(f'3 {i}')
        if i % 5 == 0: string += 'buzz '
        if i % 7 == 0: string += 'woof '
        if string == '': string = str(i)+' '
        print(i)
        for i in range(5):
            string += str(i)
            print(i)
            if i < 1: break # 0 % anything is true
            if i % 3 == 0: string += 'fizz '
            if i % 5 == 0: string += 'buzz '
            if i % 7 == 0: string += 'woof '
            i = i // 10
        print(string)
fizzBuzzWoof()
