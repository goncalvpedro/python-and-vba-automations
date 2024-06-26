Cloud File Organization

Project 99freelas
https://www.99freelas.com.br/project/organizacao-automatizada-de-arquivos-em-nuvem-495519

I have an accounting firm and distribute documents that must be sent to clients through Google Drive.
With the increase in the number of clients, the distribution of documents in each client's folder is becoming a slow and inefficient process.

I need an automated way to deposit these documents. The number of clients increases every month.

This is the main demand, there are other intrinsic characteristics to the project. I will provide more details to those interested.

-------------------------------------------------------------------------------------

Project Involves:
- Creation of a virtual environment to run the code on the client's computer
- Creation of an interface "form" for the user to enter their information ---- OK
    - PySimpleGUI
    - Tkinter
    - Time

    Step by step
    1. Creation of the "file organizer" folder
    2. Creation of a readme.txt file for instructions and step by step
    3. Creation of a Python file organizer_de_arquivos.py in a virtual environment
    4. Installation of libraries for the project
        a. Upgrade pip
        b. PySimpleGUI
        c. Time
        d. OS
        e. Google API

- Communication with Google Drive to create folders and files
    Step by step:
    1. Open an account on Google Cloud Service
    2. Create an OAuth 2.0 client credential to authenticate the Google account
    3. Generate the client_secret.json file
    4. Create a folder on Google Drive
    5. Associate input data in the interface with the directory folder

Unfortunately, in some cases, the program insists on not uploading the files, but most formats have worked.

The next step is to create subfolders on Google Drive.
