#project - CRUD operations

from pathlib import Path # yah path humko batata  hai ki hum work konse folder,file mai kr rahaa hai
import os
def readfileandfolder():
    try:
        p = Path('')
        items = list(p.rglob('*')) #rglob humko sbhi folder ke ander ke file ko (find karne mai help krta hai/batata hai ki woh kaha hai)
        for index , file in enumerate(items):
            print(f'{index+1} - {file}')
    except Exception as e:  #code mai yadi error aayega toh yeh line humko easy/short way mai bata degi ki error kaha hai 
        print(e)




def create_file():
    try:
        readfileandfolder()
        file_name = input("Enter name of your file:")
        p = Path(file_name)
        if p.exists():
            print('FILE ALREADY EXISTS')
        else:
            with open(file_name,'w') as file:
                content = input('Enter your file content:')
                file.write(content)
                print('FILE ADDED!')
    except Exception as e:
        print(e)


def read_file():
    readfileandfolder()
    file_name = input('Enter name of your file:')
    p = Path(file_name)
    if p.exists():
        with open(file_name,'r') as file:
            print(file.read())
    else:
        print('FILE NOT FOUND!')

def update_file():
    try:
        readfileandfolder()
        file_name = input("Enter name of your File:")
        p = Path(file_name)
        if p.exists():
            print('press 1 to overwrite the content')
            print('press 2 to append new content')

            option = int(input('Enter your choice for updating a file:'))
            if option == 1:
                with open (file_name,'w') as file:
                    content = input('Enter your content:')
                    file.write(content)
                    print('CONTENT CHANGED...')
            elif option == 2:
                with open (file_name,'a') as file:
                    content = input('Enter your content:')
                    file.write(content)
                    print('CONTENT CHANGED...')
            else:
                print ("INVALID INPUT")
        else:
            print("FILE DOES NOT EXIST!")
    except Exception as e:
        print(e) 




def delete_file():
    readfileandfolder()
    file_name = input('Enter name of your file:')
    p = Path(file_name) 
    if p.exists():
        os.remove(p)  #os os remoing path of that filecompletely from the system
        print("FILE DELETED") 
    else:
        print("FILE DOES NOT EXISTS!!")         



def rename_file():
    readfileandfolder()
    file_name = input("Enter name of your files:")
    p = Path(file_name)
    if p.exists():
        new_file = input('Enter new name of your file:')
        p.rename(new_file)
        print('FILE RENAME!')
    else:
        print('FILE NOT FOUND!')


def create_folder():
    readfileandfolder()
    folder_name = input('Enter name of your folder')
    p = Path(folder_name)
    if p.exists():
        print('FOLDER ALREADY EXISTS!')
    else:
        p.mkdir()
        print('FOLDER CREATED!')



def delete_folder():
    readfileandfolder()
    folder_name = input('Enter name of your folder')
    p = Path(folder_name)
    if p.exists():
        print('FOLDER DELETED!')
    else:
        p.rmkdir()
        print('FOLDER NOT FOUND!')


def create_file_in_folder():
    folder_name = input('Enter name of your folder:')
    file_name = input('Enter name of your file:')
    p = Path(folder_name/file_name) 
    if p.exists():
        print('FILE ALDEARY EXISTS!')
    else:
               


while True:
    print("press 1 for creating a file")
    print("press 2 for reading a file")
    print("press 3 for updating a file")
    print("press 4 for deleting a file")
    print("press 5 for renaming a file")
    print("press 6 for creating a folder")
    print("press 7 for deleting a folder")
    print("press 0 for existing....")

    option = int(input("Enter your choice:"))
    if option == 1:
        create_file()

    if option == 2:
        read_file()

    if option == 3:
        update_file()

    if option == 4:
        delete_file()

    if option == 5:
        rename_file() 

    if option == 6:
        create_folder() 

    if option == 7:
        delete_folder()          

    if option == 0:
        break        
