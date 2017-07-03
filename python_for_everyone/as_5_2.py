num_list = []

while True:
    try:
        string = input('enter an integer: ')
        if isinstance(string,int):
            num_list.append(int(string))
        else:
            continue
    except NameError:
        if string == 'done':
            num_list.sort()
            print('Minimum is {}'.format(num_list[0]))
            print('Maximum is {}'.format(num_list[-1]))
            break
        else:
            print('Invalid entry\n')
            continue
