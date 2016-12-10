def get_from_db():
    lis = []
    file = open('db.txt', 'r')
    for i in file.readlines():
        lis.append(list(i.splitlines()))
    file.close()
    return lis


def user_input():
    my_list = get_from_db()
    var = ''

    while var not in ['1', '2', '3']:
        var = input('[1] Clean downloads folder\n[2] Change allowed movie file extensions\n[3] Changed banned file extensions? (files will be deleted)\n-->')
        if var not in ['1', '2', '3']:
            print('Wrong input')
        if var == '1':
            print('\nSorting...')
            return 1
        if var == '2':
            fe = input('-->')
            if fe not in my_list[0]:
                my_list[0].append(fe)
                break
        if var == '3':
            fe = input('-->')
            if fe not in my_list[1]:
                my_list[1].append(fe + ' ')
                break
    file = open('db.txt', 'w')
    file.seek(0)
    file.truncate()
    for i in my_list:
        file.write(''.join(i) + '\n')
    file.close()

