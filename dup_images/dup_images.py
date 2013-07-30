#!/usr/bin/env python
from sys import exit
from PIL import Image
from PIL.ExifTags import TAGS
import glob
import argparse
import os

def parse_command_line():
    """ User requires to specify directory """
    parser = argparse.ArgumentParser(description='find duplicated image files.')
    parser.add_argument('directory', metavar='D', type=str, nargs='+',
                        help='directory to be searched')
    args = parser.parse_args()

    return args

def find_image_files(list_directory):
    """ Find image files only from valid directory """
    image_files = []
    for dir in list_directory.directory:
        if os.path.isdir(dir):
           image_files.extend( glob.glob(os.path.join(dir, '*.jpg')) )
        else:
           print 'Warning: "%s" is not a directory.' % dir

    return image_files

def find_a_match(list_image_file):
    """ Find duplicates only from files with EXIF data """
    list_image_file_with_exif = []
    list_exif_data = []
    for image_file in list_image_file:
        dict_exif_data = get_exif_data(image_file)
        #print dict_exif_data
        if not dict_exif_data:
            print 'Warning: "%s" has no EXIF data.' % image_file
        else: # Assume the order of elements in list is persistent
            list_image_file_with_exif.append(image_file)
            list_exif_data.append(dict_exif_data)

    #print list_image_file_with_exif
    #print list_exif_data
    total = len(list_image_file_with_exif)
    # Any better approach for finding a match? I'm keen to know/learn what others doing ;)
    for i in range(total-1, 0, -1):
        for j in range(i):
            #print 'cmp(dict_%d, dict_%d)' % (i, j),
            if not cmp(list_exif_data[i], list_exif_data[j]):
                print 'Found a match: "%s"\t"%s"' % (
                                      list_image_file_with_exif[i], 
                                      list_image_file_with_exif[j])

    return 0

def get_exif_data(fname):
    """ Get embedded EXIF data from image file. """
    exif_data = {}
    try:
        img = Image.open(fname)
    except IOError:
        print 'Error: IOError ' + fname
    else:
        if hasattr(img, '_getexif'):
            exif = img._getexif()
            if exif != None:
                for tag, value in exif.items():
                    decoded = TAGS.get(tag, tag)
                    exif_data[decoded] = value

    return exif_data

def main():
    """ 
    0. get command line arguments
    1. find image files from directory
    2. find a match by comparing exif info
    """
    list_directory = parse_command_line()
    #print list_directory.directory

    list_image_file = find_image_files(list_directory)
    #print list_image_file
    if not list_image_file:
        print 'no image file found in the directory.'
        return 1

    status = find_a_match(list_image_file)

    return 0

if __name__ == '__main__':
    exit(main())

