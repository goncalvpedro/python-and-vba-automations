# PDF Manipulation

This project aims to work with basic pdf manipulation, such as, rotation, merge, encrypt, decrypt and more using PyPDF2 python module. As a extra content I brought you a example of usage of Gemini AI from Google (for free in this context). 

## Table of Contents

- [PDF Manipulation](#pdf-manipulation)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Usage](#usage)

## Introduction

This project is an introduction for PDF manipulation. PyPDF2 is not the most complete module but it has everything that you need to start and practice pdf manipulation. For more complex project, I would use **MuPDF** *https://mupdf.readthedocs.io/en/latest/index.html* which also works for JavaScript, C# and C++ and it is much more customizable and you can get better results in data extraction, resizing it and also with the PDF encryption. 


**----------------------------------------------------------------------------------------------------------------------------------**


## Features

- Python 3.11
- PyPDF2 3.0.1
- Google Generative AI - Gemini AI 0.4.0
- pandas 2.2.1
- tkinter


**----------------------------------------------------------------------------------------------------------------------------------**


## Usage

**File description**

*Pdf Manipulation*

- **app.py**

    Works as a menu where the user can choose what to do with the pdf by typing the number correspondinf to the action.

- **file_explorer.py**

    Opens the local file explorer so the user can choose the desired files. Attention to the fact that for some fuctions only one file will be manipulated at a time, even if the user selects more than one file.

- **pdf-reader.py**

    It is where I built all functions to manipulate files. It is called by the option that the user choose on the 'menu'. Could be done as a Class? Yes, but I didn't, feel free to do it and pull a request here, I will be glad to have collaborators!!

***Generative AI - Gemini***

Get your API key in Google AI Studio for free.

- **gemini-ai.py**

    This file is just an example on how to import the ai and give to it a simple prompt, such as, "Give me 5 recipes with rice"

- **embedding.py**

    This file is the beginning of a bigger project that consists in a AI that would interpret a document and be trained by it to answer and create questions about it and give insights. 

    Read Gemini AI documentation to learn what is embedding and why is important, it will boost you AI techniques! Every AI-related script here is based on theirs.

**----------------------------------------------------------------------------------------------------------------------------------**

**Gemini AI Overview**

*#https://ai.google.dev/docs/gemini_api_overview?authuser=1#python_2*
