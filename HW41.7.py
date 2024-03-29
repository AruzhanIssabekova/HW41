def mad_libs():
    noun = input("Введите глагол: ")
    verb = input("Введите существительное: ")
    adjective = input("Введите прилагательное: ")

    madlib = f"{adjective} {noun} {verb} над ленивой собакой."
    print(madlib)

mad_libs()
