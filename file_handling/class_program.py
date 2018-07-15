# a file is a stream of bytes
# study: buffer caching, Unix system programming by Morris Bach, advanced programming in the unix environment richard stevens

def understanding_files():
    fd = open("foo.txt","w")
    fd.write("hello") # writes string and returns number of characters. if file doesn't exists, it creates one
    fd.close()

    fd = open("foo.txt","r") # if you don't pass permission, it by default opens in read mode

    fd.read()
    fd.read() # this returns nothing as the entire file has been "read" in the last command

    fd.seek(0,0) # this makes the cursor goes to the initial position
    fd.close()
    # the open in 3.x is of object TextIOWrapper. the seek in this does not support relative seeking. thus, use the following
    # in 3.x, fd.seek(1,1) will give error

    import io

    fd = io.FileIO("foo.txt")
    fd.seek(-10,2) # goes to end of file and takes the seek back 10 characters
    fd.seek(2,1) # goes to the current seek and goes two steps forward
    fd.seek(2,0) # goes to the start of the stream and goes two steps forward

# WAP to accept a file name from user and display alternate characters
import io
import sys
import shutil
import argparse

def alternate_file_chars(filename):

    if type(filename) == str and filename != "":

        df = io.FileIO(filename)
        
        if df != None:

            print(df.read(1))
            while df.read(1) != b'':
                print(df.read(1))

            df.close()


def longest_line(filename):
    if type(filename) == str and filename != "":
        df = io.FileIO(filename)
        if df != None:
            ind, length = 0, 0
            allines = df.readlines()
            df.close()

            for x,y in enumerate(allines):
                if len(y) > length:
                    length, ind = len(y), x

            print("Longest line is: ", allines[ind])

def copy_file_contents(file1, file2, n):
    if type(file1) == str and file1 != "" and type(file2) == str and file2 != "":
        
        df1 = io.FileIO(file1)
        df2 = io.FileIO(file2, "w")

        if n == 0:
            shutil.copyfileobj(df1, df2)
        else:
            if df1 != None:
                line = df1.readline()
                
                while line!=b"" and n !=0:
                    df2.write(line)
                    line = df1.readline()
                    n -= 1
            df1.flush()

        df1.close()
        df2.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dest-file", help = "Destination File")
    parser.add_argument("-x", "--source-file", help = "Source File")
    parser.add_argument("-n", "--no", default = 0, type=int, help = "Number of lines. Set to 0 by default.")
    args = parser.parse_args()
    
    copy_file_contents(args.source_file, args.dest_file, args.no)

    # sys.argv is a list of command line arguments
    # if we give -h as one of the arguments, it'll give help options

if __name__ == "__main__":
    main()

# HW
# WAP to accept a file from user and display alternate 10 characters