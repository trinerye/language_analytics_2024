import os
import sys

def main():

    in_folderpath = os.path.join("emissions")
    out_folderpath = os.path.join("out")
    os.makedirs(os.path.join(out_folderpath), exist_ok=True)

    if os.path.exists(os.path.join(in_folderpath,"emissions.csv")):
        os.remove(os.path.join(in_folderpath,"emissions.csv"))
    else:
        print("The file does not exist")

    filenames = [file for file in os.listdir(in_folderpath) if file.endswith('.csv')]

    for i, file in enumerate(filenames):
        source = os.path.join(in_folderpath, file)
        distination = os.path.join(in_folderpath, f"emissions_base_{i}.csv")
        os.rename(source, distination)
        print(f"Renames {source} to {distination}")







if __name__ == "__main__":
    main()

## Import the files to a folder in this direcotry 

## Delete the emissions csv for each folder 

## Create a path file for each csv in the folder

## Rename the emissions_base

# Make a plot from each csv 