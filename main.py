#Без интерфейса

dff = int(input('''1.Создать новую заметку.
2.Открыть прошлые записи.
3.Видалити запис не працює.
4.Удалить всё.
:'''))

def read():
    with open('Book.txt', 'r') as read_file:
        for line in read_file:
            print(line, end='')
    read_file.close()
def Write():
    a = input('''Введите текст для заметки.
:''')
    with open('Book.txt', 'a') as write_file:
        write_file.write(f'\n{a}')
    write_file.close()
def cleer():
    with open('Book.txt', 'w') as cleer:
        print('Успішно')



jj = True
while jj:
    if dff == 1:
        Write()
        s = int(input('''1.Добивить ещё.
2.Не добавлять.
:'''))
        if s == 1:
            jj = True
        else:
            jj = False
    elif dff == 2:
        read()
        jj = False
    elif dff == 4:
        cleer()
        jj = False
    else:
        print('Выберете один из пунктов выше:')
        jj = True
