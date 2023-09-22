import os


os.chdir('Desktop/TE4')

headname = input('What would you like for your head folder name? ')
print(headname)

os.mkdir(headname)

title = input("What would you like the tittle to be? ")

os.chdir(headname)
i = open("index.html", "x")

file = open("index.html","w")
file.write(f'<!DOCTYPE html> \n<html lang="en"> \n<head> \n    <meta charset="UTF-8"> \n    <meta name="viewport" content="width=device-width, initial-scale=1.0"> \n    <title>{title}</title> \n    <link rel="stylesheet" href="./css/style.css"> \n</head> \n<body> \n \n    <script src="./js/script.js"></script> \n</body> \n</html>')
file.close()


subfolders = ["css", "img", "js", "html"]
for x in subfolders:
    os.mkdir(x)


os.chdir("css")
s = open("style.css", "x")

os.chdir("../js")
j = open("script.js", "x")