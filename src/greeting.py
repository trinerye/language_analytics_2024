#%%
import argparse
from person import Person

#%%

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name",
                        "-n",
                        required = True)

    parser.add_argument("--likes",
                        "-l",
                        required = True)

    return parser.parse_args()

def main():
    args = parser()
    person = Person(args.name, args.likes)
    person.hello()
    person.preferences()
    print(person.species)

if __name__=="__main__":
    main()
# %%
