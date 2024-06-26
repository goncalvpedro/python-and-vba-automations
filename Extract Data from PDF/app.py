import pdf_reader

def menu():
    while True:
        menu = input("\nWelcome to Pdf Manipulator!\n What do you need?" +
                "\n1 - Merge\n2 - Rotate\n3 - Extract text\n4 - Extract images" +
                "\n5 - Encrypt\n6 - Decrypt\n7 - Resize\n8 - Exit\n")
        
        try:
            menu = int(menu)
        except:
            print("Invalid input. Type the number corresponding to what you need.")

        if menu == 1:
            pdf_reader.mergePdf()

        elif menu == 2:
            pdf_reader.rotatePdf()

        elif menu == 3:
            pdf_reader.extractText()

        elif menu == 4:
            pdf_reader.extractImages()
            
        elif menu == 5:
            pdf_reader.encryptPdf()

        elif menu == 6:
            pdf_reader.decryptPdf()

        elif menu == 7:
            pdf_reader.resizePdf()

        elif menu == 8:
            break
        else:
            print("Invalid input")
            menu = input("Welcome to Pdf Manipulator!\n What do you need?" /
                        "\n1 - Merge\n2 - Rotate\n3 - Extract text\n4 - Extract images" /
                        "\n5 - Encrypt\n6 - Decrypt\n7 - Resize\n8 - Exit")
            continue
        