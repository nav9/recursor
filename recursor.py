import os

def folders():
    contents=os.listdir()
    "print('Contents of this folder are')"
    "print(contents)"
    onlyfileshere = 1

    for i in contents:
        if os.path.isfile(i):
            if 'Desktop.ini' in i:
                os.remove("Desktop.ini")
                print('Deleted Desktop.ini')
        else:
            onlyfileshere = 0
            print('--------- entering directory: ' + i )
            os.chdir(i)
            folders()

    os.chdir('..')
    return

folders()

