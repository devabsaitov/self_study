import os

while True:
    command = input(f"{os.getcwd()}$ ").split()
    c = command[-1]
    match command[0]:
        case "yaratish_papka":
            os.mkdir(c)
        case "yaratish":
            os.mknod(c)
        case "kirish":
            os.chdir(c)
        case "orqaga":
            os.chdir('../')

