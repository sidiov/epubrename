import argparse, sys
import os
import ebooklib
from ebooklib import epub
from ebooklib.utils import debug

def convertMetadata(md):
    sd = str(md[0])
    return sd

def getMetadata(md):
    book = epub.read_epub(md)

    if (args.debug):
        debug(book.metadata)

    title = convertMetadata(book.get_metadata('DC', 'title')[0])
    author = convertMetadata(book.get_metadata('DC', 'creator')[0])
    new_filename = author + " - " + title + ".epub"
    print(md + "    ====>    " + new_filename)

    #This will break if any of the names contain '\' in linux
    if not args.print_only:
        try:
            dir = os.path.dirname(md)
            newname = dir + "/" + new_filename
            #print(newname)
            os.rename(f, newname)
            print("...OK...")
        except:
            print("ERROR: Could not rename " + f)



parser = argparse.ArgumentParser(
    description='Rename an epub file based on author and title')
parser.add_argument('-p', '--print-only', action='store_true',
               help='print out new name without renaming the file')
parser.add_argument('-d', '--debug', action='store_true',
               help='print out full metadata from ebook')
parser.add_argument('path', type=str, help='epub  or directory path')

args = parser.parse_args(args=(sys.argv[1:] or ['--help']))

if args.path.endswith(".epub"):
    try:
        getMetadata(args.path)
    except:
        print("Could not open epub file " + args.path)
        exit(1)

else:
    if os.path.isdir(args.path):
        for filename in os.listdir(args.path):
            f = os.path.join(args.path, filename)
            # checking if it is a file
            if os.path.isfile(f):
                if f.endswith(".epub"):
                    try:
                        getMetadata(f)
                    except:
                        print("Could not open epub file " + f)

    else:
        print(args.path + " is not a valid directory or file.")
        exit(1)

exit(0)