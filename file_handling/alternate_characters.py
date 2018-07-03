import io

def alternate_characters(filename):
    if type(filename) == str and filename != "":

        fh = io.FileIO(filename)
        
        if fh != None:
            
            while True:
                line = fh.read(10)
                if line == b'':
                    break

                print(line)

                fh.seek(10,1)

def main():
    user_input_file = input("Enter your file name: ")
    alternate_characters(user_input_file)

if __name__ == "__main__":
    main()
