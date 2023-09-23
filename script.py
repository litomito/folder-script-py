import os


# The path you want to nake the folder structure. So mine folder will be in TE4. CHANGE THIS FOR YOUR COMPUTER
os.chdir('Desktop/TE4')

# Asks the user want they would want to name the head folder
headname = input('What would you like for your head folder name? ')

# Prints the name that the user typed in the question above
print(headname)

# Makes the head folder
os.mkdir(headname)

# Asks what the user what they would like there index.html tittle to be
title = input("What would you like the tittle to be? ")

# Changes the path so every other folders and files would be in (Desktop/TE4/"THE_NAME_FOR_HEAD_FOLDER")
os.chdir(headname)

# Creates an index.html in the head folder
i = open("index.html", "x")

# Opens the index.html file, and writes the <!DOCTYPE html> for you. It will link a style.css and a script.js for you
with open("index.html", "w") as file:
    file.write(f'<!DOCTYPE html> \n<html lang="en"> \n<head> \n    <meta charset="UTF-8"> \n    <meta name="viewport" content="width=device-width, initial-scale=1.0"> \n    <title>{title}</title> \n    <link rel="stylesheet" href="./css/style.css"> \n</head> \n<body> \n \n    <script src="./js/script.js"></script> \n</body> \n</html>')
file.close()

# Creates four folders in the head folder css, img, js, html
subfolders = ["css", "img", "js", "html"]
for x in subfolders:
    os.mkdir(x)

# Changes path to (Desktop/TE4/"THE_NAME_FOR_HEAD_FOLDER"/css). In there it will create a style.css that's linked to index.html
os.chdir("css")
s = open("style.css", "x")

# Changes path to (Desktop/TE4/"THE_NAME_FOR_HEAD_FOLDER"/js). In there it will create a script.js that's linked to index.html
os.chdir("../js")
j = open("script.js", "x")

# Asks the user if they would like to make html files in the html folder (y/n = Yes or No).
# And changes path to (Desktop/TE4/"THE_NAME_FOR_HEAD_FOLDER"/html)
Q_html = input('Do you want more HTML files in html folder? (y/n): ')
os.chdir("../html")

# Checks if the user answered y or n. If the user answered y it will ask how many html files the user want to make.
# If the user type 2 it will ask the user what they would like to name the files and add .html to them.
# It will also write the <!DOCTYPE html> and give it the same tittle as the file name.
# This will link style.css and script.js to your new html file
# if the user answerd n it will skip the code and not make any html files in the html folder
if Q_html == "y":
    num = int(input('How many HTML files would you like? '))

    for i in range(num):
        file_name = input(f'Enter the name for the HTMl file {i + 1}: ')
        with open(f'{file_name}.html', 'w') as html_file:
            html_file.write(f'<!DOCTYPE html> \n<html lang="en"> \n<head> \n    <meta charset="UTF-8"> \n    <meta name="viewport" content="width=device-width, initial-scale=1.0"> \n    <title>{file_name}</title> \n    <link rel="stylesheet" href="./css/style.css"> \n</head> \n<body> \n \n    <script src="./js/script.js"></script> \n</body> \n</html>')
else:
    print('')

# This code will ask the user if it would like more css files in the css folder
Q_css = input('Would you like more CSS files in your css folder? (y/n): ')
os.chdir("../css")

# This code will cheack if the user typed y or n, if the user typed n it will skip this code,
# and if the user typed y it will ask the user how many css files it would like.
# It will create the css files in the css folder that the user typed
if Q_css == "y":
    num2 = int(input('How many CSS files would you like? '))

    for i in range(num2):
        file_name_css = input(f'Enter the name for the CSS file {i + 1}: ')
        with open(f'{file_name_css}.css', 'w') as css_file:
            pass
else:
    print('')

# This code asks the user if they would like to link the new css files to the new html files and changes path to html folder
Q_link = input('Would you like to link the new CSS to the new HTML? (y/n): ')
os.chdir("../html")

# This code will cheack if the user answerd y or n. If the user typed n it will skip everything
# If th user typed y it will ask the user what css you want to link and then ask you what html you want to link it to
# Once it's done linking it will print out the css th user typed to the html the user typed (linked css to html)
#
if Q_link == "y":
        num3 = int(input('How many css files would you like to link to html files? '))
        
        for i in range(num3):
            file_name = input("Tell me what CSS you want to link? ")
            file_name_css = input(f'Tell me what HTMl you want to link to {file_name}? ')
            with open(f'{file_name}.html', "w") as html_file:
                html_file.write(f'<!DOCTYPE html> \n<html lang="en"> \n<head> \n    <meta charset="UTF-8"> \n    <meta name="viewport" content="width=device-width, initial-scale=1.0"> \n    <title>{file_name}</title> \n    <link rel="stylesheet" href="../css/{file_name_css}.css"> \n</head> \n<body> \n \n    <script src="./js/script.js"></script> \n</body> \n</html>')
            html_file.close()
            print(f'Linking {file_name} to {file_name_css} ') 

        pass
else:
    print('')

Q_js = input("Would you like to make more JS files? (y/n): ")
os.chdir("../js")

if Q_js == "y":
     num4 = int(input('How many JS files would you like? '))

     for i in range(num4):
         file_name_js = input(f'Enter the name you would like for the js file {i + 1} ')
         open(f'{file_name_js}.js', 'x')
         pass
else:
    print('')

link_js = input("Do you want to link your new JS files to HTML files? (y/n): ")
os.chdir("../html")

if link_js == "y":
    num5 = int(input(f'How many JS files do you want to link to HTML '))

    for i in range(num5):
        file_name_js = input("Tell me what JS you want to link? ")
        file_name = input(f'Tell me what HTMl you want to link to {file_name_js}? ')
        with open(f'{file_name}.html', "w") as html_file:
            html_file.write(f'<!DOCTYPE html> \n<html lang="en"> \n<head> \n    <meta charset="UTF-8"> \n    <meta name="viewport" content="width=device-width, initial-scale=1.0"> \n    <title>{file_name}</title> \n    <link rel="stylesheet" href="../css/{file_name_css}.css"> \n</head> \n<body> \n \n    <script src="./js/{file_name_js}.js"></script> \n</body> \n</html>')
        html_file.close()
        print(f'Linking {file_name_js} to {file_name} ')
    pass
else:
    print("Goodbye")