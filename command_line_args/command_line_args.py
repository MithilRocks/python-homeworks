import sys
import argparse

# sys.argv gives command line arguments
# python abc.py dest_file src_file
# it gives list ['.\\abc.py','dest_file','src_file']
# now argparse is a module to parse command line arguments efficiently with the use of parameters

# What if the user exchanges src_file and dest_file?
# we can re-write the code as 
# python abc.py -d dest_file -s src_file
# -d and -s distinguishes

def main():
    print(sys.argv)

if __name__ == "__main__":
    main()