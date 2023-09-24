#!/bin/python3

import argparse
import subprocess # just to call an arbitrary command e.g. 'ls'
import os

PERCENTAGE_DEFAULT = 50
        

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Log and plot sensors from file, serial line or mqtt msg...")
    parser.add_argument("-d", "--directory", type=str,
                    help="name of directory") 
    parser.add_argument("-p", "--percentage", type=int, default=PERCENTAGE_DEFAULT,
                    help="percentage decrease")


    args = parser.parse_args()

    # Check if directory is existing



    directory = args.directory

    print("Réduction des photos du dossier ", directory)
    print("Reduction de", args.percentage)
    try:
        os.chdir(directory)
    except:
        print("Error : missing directory")
        print("./reduc_image.py <directory name>")
        exit()

    print("Dossier :", os.getcwd())
    os.chdir("..")
    print("Dossier :", os.getcwd())


    picture_list = os.listdir(directory)
    
    name = directory.split("/")[-1]
    if(name == ""):
        print("Condition")
        name = directory.split("/")[-2]

    name_new = name+"_reduc_"+str(args.percentage)
    os.mkdir(name_new)
    for elem in picture_list:
        commande = "convert -resize " + str(args.percentage)  + "% '"  + name + "'/" + elem + " '" + name_new + "'/" + elem 
        os.system(commande)
