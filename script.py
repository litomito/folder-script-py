import os


os.chdir('Desktop/TE4')

headname = input('What would you like for your head folder name? ')
print(headname)

os.mkdir(headname)

title = input("What would you like the tittle to be? ")

os.chdir(headname)
i = open("index.html", "x")

with open("index.html", "w") as file:
    file.write(f'<!DOCTYPE html> \n<html lang="en"> \n<head> \n    <meta charset="UTF-8"> \n    <meta name="viewport" content="width=device-width, initial-scale=1.0"> \n    <title>{title}</title> \n    <link rel="stylesheet" href="./css/style.css"> \n</head> \n<body> \n \n    <script src="./js/script.js"></script> \n</body> \n</html>')
file.close()


subfolders = ["css", "img", "js", "html"]
for x in subfolders:
    os.mkdir(x)


os.chdir("css")
s = open("style.css", "x")

os.chdir("../js")
j = open("script.js", "x")


Q_html = input('Do you want more HTML files in html folder? (y/n): ')
os.chdir("../html")

if Q_html == "y":
    num = int(input('How many HTML files would you like? '))

    for i in range(num):
        file_name = input('Enter the name for the HTMl file: ')
        with open(f'{file_name}.html', 'w') as html_file:
            html_file.write(f'<!DOCTYPE html> \n<html lang="en"> \n<head> \n    <meta charset="UTF-8"> \n    <meta name="viewport" content="width=device-width, initial-scale=1.0"> \n    <title>{file_name}</title> \n    <link rel="stylesheet" href="./css/style.css"> \n</head> \n<body> \n \n    <script src="./js/script.js"></script> \n</body> \n</html>')
else:
    print('')

Q_css = input('Would you like more CSS files in your css folder (y/n): ')
os.chdir("../css")

if Q_css == "y":
    num2 = int(input('How many CSS files would you like? '))

    for i in range(num2):
        file_name_css = input('Enter the name for the CSS file: ')
        with open(f'{file_name_css}.css', 'w') as css_file:
            pass
else:
    print('Goodbye')
