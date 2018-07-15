import shutil

def my_archive():
    rootdir = input("Enter your directory: ")
    archive = input("Enter Archive name: ")
    
    shutil.make_archive(archive, "zip", rootdir)

def main():
    my_archive()

if __name__ == "__main__":
    main()
