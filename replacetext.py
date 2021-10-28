import glob, os

print('Dette scriptet erstatter strenger med det du spesifiserer.\n')

folder = input('Hvor i filsystemet ligger filene?\n')
before = input('Finn: ')
after  = input('Erstatt: ')

os.chdir(folder)
for file in glob.glob("*.ifc"):
    filename = file

    f = open(filename, "r")
    text = f.read()
    text = text.replace(before, after)

    f = open(filename, "w")
    f.write(text)
    f.close()

    print('Replaced all instances of ' + before + ' with ' + after + ' in file ' + filename)