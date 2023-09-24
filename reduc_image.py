#!/bin/python3

import argparse
import subprocess
import os
from PIL import Image

MAX_SIDE_DEFAULT = 1200
        

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Decrease size of picture of one directory")
    parser.add_argument("-d", "--directory", type=str,
                    help="name of directory")
    group = parser.add_mutually_exclusive_group()                
    group.add_argument("-p", "--percentage", type=int,
                    help="percentage decrease")
    group.add_argument("-m", "--max_side", type=int, default=MAX_SIDE_DEFAULT,
                    help="Maximum side size") 

    args = parser.parse_args()


    directory = args.directory

    try:
        os.chdir(directory)
    except:
        print("Error : missing directory")
        print("./reduc_image.py <directory name>")
        exit()


    print("Réduction des photos du dossier ", directory)

    if(args.percentage != None):
        print("Reduction de", args.percentage)
    else:
        print("Nouvelle taille du côté max est", args.max_side)

    os.chdir("..")


    picture_list = os.listdir(directory)
    
    name = directory.split("/")[-1]
    if(name == ""):
        name = directory.split("/")[-2]

    if(args.percentage != None):
        name_new = name+"_reduc_"+str(args.percentage)
        os.mkdir(name_new)
        new_route = name_new + "/"

        for elem in picture_list:
            im = Image.open(name + "/" + elem)
            width = im.size[0]
            height = im.size[1]

            new_size = (int(width*args.percentage/100), int(height*args.percentage/100)) 
            new_image = im.resize(new_size)

            print("loop 1.5")

            route_picture = new_route + elem
            new_image.save(route_picture)

            im.close()

    else:
        name_new = name + "_size_" + str(args.max_side)
        os.mkdir(name_new)

        new_route = name_new + "/"

        for elem in picture_list:
            im = Image.open(name + "/" + elem)

            maxi = max(im.size)
            width = im.size[0]
            height = im.size[1]

            percent = args.max_side/maxi

            new_size = (int(width*percent), int(height*percent))
            new_image = im.resize(new_size)

            route_picture = new_route + elem
            new_image.save(route_picture)

            im.close()