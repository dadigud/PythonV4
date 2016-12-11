def get_from_db():
    lis = []
    file = open('db.txt', 'r')
    for i in file.readlines():
        lis.append((i.splitlines()))
    file.close()
    lis[0] = ' '.join(lis[0]).split()
    lis[1] = ' '.join(lis[1]).split()
    return lis


def a_or_r_extension(ml, l_num):
    inp = input('[1] Add\n[2] Remove\n')
    if inp == '1':
        fe = input('Add extension -->')
        if fe not in ml[l_num]:
            ml[l_num].append(' ' + fe)
    elif inp == '2':
        fe = input('Remove extension -->')
        if fe in ml[l_num]:
            ml[l_num].remove(fe)


def user_input():
    my_list = get_from_db()
    var = ''

    while var not in ['1', '2', '3']:
        var = input('[1] Clean downloads folder\n[2] Add or remove allowed movie file extensions\n[3] Add or remove banned file extensions? (files will be deleted)\n-->')
        if var not in ['1', '2', '3']:
            print('Wrong input')
        if var == '1':
            print('\nSorting...')
            return 1
        if var == '2':
            a_or_r_extension(my_list, 0)
            break
        if var == '3':
            a_or_r_extension(my_list, 1)
            break
    file = open('db.txt', 'w')
    file.seek(0)
    file.truncate()
    for i in my_list:
        file.write(' '.join(i) + '\n')
    file.close()

