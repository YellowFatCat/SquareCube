pathIn = False; # Флаг корректности введенного имени файла для чтения.

# Открытие файла с данными.
while (not pathIn):
    try:
        name = input("Введите имя файла для чтения: ");
        name += ".txt";
        file = open(name);
        pathIn = True;
    except IOError:
        pathIn = False;
        answ = input("Такого файла не существует. Продолжить? (Y/N) ");
        if (answ == 'N' or answ == 'n'):
            print("Работа программы прекращена пользователем.");
            break;
        if (answ != 'Y' and answ != 'y'):
            print("Введена неизвестная команда. Работа программы будет продолжена.");

if (pathIn):
    # Считывание данных из файла.
    arr = file.readlines();
    n = len(arr);

    # Открытие файла для записи.
    pathOut = False; # Флаг корректности введенного имени файла для записи.
    while (not pathOut):
        try:
            name = input("Введите имя файла для записи: ");
            name += ".txt";
            fileNew = open(name, "w");
            pathOut = True;
        except IOError:
            pathOut = False;
            answ = input("Некорректное имя файла. Продолжить? (Y/N) ");
            if (answ == 'N' or answ == 'n'):
                print("Запись в файл не была произведена.");
                break;
            if (answ != 'Y' and answ != 'y'):
                print("Введена неизвестная команда. Работа программы будет продолжена.");  

    # Вывод заголовка таблицы на экран и его запись в файл.
    sep = "+" + 9 * "-" + "+" + 9 * "-" + "+" + 9 * "-" + "+";
    print(sep);
    print("|  Число  | Квадрат |   Куб   |");
    print(sep);
    if (pathOut): # Запись в файл.
        fileNew.write(sep + "\n");
        fileNew.write("|  Число  | Квадрат |   Куб   |\n");
        fileNew.write(sep + "\n");

    # Обработка исходных данных и формирование таблицы.           
    for i in range (n):
        try:
            arr[i] = float(arr[i]);
            s = "|{0:9.3f}|{1:9.3f}|{2:9.3f}|".format(arr[i], arr[i]**2, arr[i]**3);
        except ValueError:
            s = "|{0:>9}|".format(arr[i].replace('\n', '')) + "  Ошибка |  Ошибка |";
        print(s);
        print(sep);
        if (pathOut): # Запись в файл.
            fileNew.write(s + "\n");
            fileNew.write(sep + "\n");

    # Закрытие файлов.
    try:
        file.close();
        fileNew.close();
    except NameError:
        pathIn = False;

input();
