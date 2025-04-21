""""
=================================
-----> Exceptions Handling <-----
        Advanced Example
=================================
[1] try => Test the code for errors
[2] except => Handle the errors
# -------------------------------
[3] else => If no errors
[4] finally => Run the code
==================================
"""

file = None
tries = 5

while tries > 0:

    try:
        print('\n'
            f"You have {tries} tries to open your file"'\n''\n'
            "Enter file name with it's path to open"'\n'
            "For example: C:\Python\Files\Filename.extension"'\n'
            )
        file_and_path = input("Enter your file here => ").strip()
        file = open(file_and_path, 'r')
        print(f"\nThis is the file content:\n{file.read()}\n")
        break
    
    except FileNotFoundError:
        print(f"File '{file_and_path}' NOT found, be sure that the name is correct!")
        tries -= 1

    except:
        print("Error Happen")

    finally:
        if file is not None:
            file.close()
            print("The file was closed")

else:
    print("All tries are done")