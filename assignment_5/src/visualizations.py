import os
import pandas as pd 
import matplotlib.pyplot as plt

def plot_all_assignments(df, out_folderpath):

    # Groups the entire dataframe by the 'project_name' column and sums the values in the 'emissions' column
    df_filtered = df.groupby('project_name')['emissions'].sum().reset_index()

    # Creates a plot of the emissions for each assignment
    plt.figure(figsize=(15, 10))
    plt.bar(df_filtered['project_name'], df_filtered['emissions'])
    plt.xlabel('Assignment', weight="bold")
    plt.ylabel('Emissions', weight="bold")
    plt.title('Emissions from each assignment', weight="bold")
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(out_folderpath, "all_assignments.png")) 
    plt.close()

def plot_assignment_1(df, out_folderpath):
    
    # List containing the project name
    linguistic = ['linguistic_analysis']

    # Checks if the values in the 'project_name' column is in the list, then adds the 'task_name' and 'emissions' columns to the new dataframe
    df_linguistic = df[df['project_name'].isin(linguistic)][['task_name', 'emissions']]

    # Creates a plot of tasks in assignment 1
    plt.figure(figsize=(15, 10))
    plt.bar(df_linguistic['task_name'], df_linguistic['emissions'])
    plt.xlabel('Task Name', weight="bold")
    plt.ylabel('Emissions', weight="bold")
    plt.title('CO2 emissions from each task', weight="bold")
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(out_folderpath, "linguistic_analysis.png")) 
    plt.close()

def plot_assignment_2(df, out_folderpath):

    # List containing the project name
    text = ['text_classification']

    # Checks if the values in the 'project_name' column is in the list, then adds the 'task_name' and 'emissions' columns to the new dataframe
    df_text = df[df['project_name'].isin(text)][['task_name', 'emissions']]

    # Creates a plot of tasks in assignment 2
    plt.figure(figsize=(15, 10))
    plt.bar(df_text['task_name'], df_text['emissions'])
    plt.xlabel('Task Name', weight="bold")
    plt.ylabel('Emissions', weight="bold")
    plt.title('CO2 emissions from each task', weight="bold")
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(out_folderpath, "text_classification.png")) 
    plt.close()

def plot_assignment_3(df, out_folderpath):

    # List containing the project name
    query = ['query_expansion']

    # Checks if the values in the 'project_name' column is in the list, then adds the 'task_name' and 'emissions' columns to the new dataframe
    df_query = df[df['project_name'].isin(query)][['task_name', 'emissions']]

    # Creates a plot of tasks in assignment 3
    plt.figure(figsize=(15, 10))
    plt.bar(df_query['task_name'], df_query['emissions'])
    plt.xlabel('Task Name', weight="bold")
    plt.ylabel('Emissions', weight="bold")
    plt.title('CO2 emissions from each task', weight="bold")
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(out_folderpath, "query_expansion.png")) 
    plt.close()

def plot_assignment_4(df, out_folderpath):

    # List containing the project name
    emotion = ['emotion_analysis']

    # Checks if the values in the 'project_name' column is in the list, then adds the 'task_name' and 'emissions' columns to the new dataframe
    df_emotion = df[df['project_name'].isin(emotion)][['task_name', 'emissions']]

    # Creates a plot of tasks in assignment 4
    plt.figure(figsize=(15, 10))
    plt.bar(df_emotion['task_name'], df_emotion['emissions'])
    plt.xlabel('Task Name', weight="bold")
    plt.ylabel('Emissions', weight="bold")
    plt.title('CO2 emissions from each task', weight="bold")
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(out_folderpath, "emotion_analysis.png")) 
    plt.close()


def process_csv_files(in_folderpath):

    # Checks if the faulty emissions file is in the directory, if so it removes it
    if os.path.exists(os.path.join(in_folderpath,"emissions.csv")):
        os.remove(os.path.join(in_folderpath,"emissions.csv"))
    else:
        print("The emissions.csv file does not exist")

    # Creates a list of filenames for each file in the emissions folder
    filenames = os.listdir(in_folderpath)

    # Iterates over each file in the list of filenames
    for i, file in enumerate(filenames):

        # If a file with the specified filename does not exist then rename the files in the emissions folder
        if not os.path.exists(os.path.join(in_folderpath, f"emissions_base_{i}.csv")):

            old = os.path.join(in_folderpath, file)
        
            new = os.path.join(in_folderpath, f"emissions_base_{i}.csv")

            os.rename(old, new)
        
        else:

            print(f"emissions_base_{i}.csv already exists")
    
    return filenames


def create_dataframes(filenames, in_folderpath, out_folderpath):

    # Creates a list of new filenames corresponding to the length of the old filenames list
    new_filenames = [f"emissions_base_{i}.csv" for i in range(len(filenames))]

    # Creates a filepath for each filename in the list of new filenames
    filepaths = [os.path.join(in_folderpath, filename) for filename in new_filenames]

    # Merges all the csv files together into one dataframe
    df = pd.concat(map(pd.read_csv, filepaths)) ### check what this does

    # Saves the dataframe in the out folder
    df.to_csv(os.path.join(out_folderpath, "all_emissions.csv"))

    return df


def main():

    # Creates a folderpath for each directory and makes the directory if it does not exist
    in_folderpath = os.path.join("emissions")
    out_folderpath = os.path.join("out")
    os.makedirs(os.path.join(out_folderpath), exist_ok=True)

    # Processes each csv file 
    filenames = process_csv_files(in_folderpath)

    # Creates a dataframe that contains all the csv files
    df = create_dataframes(filenames, in_folderpath, out_folderpath)

    # Filters the dataframes by the 'project_name' column, then adds the 'task_name' and 'emissions' columns to the dataframe and plots the results
    plot_assignment_1(df, out_folderpath)
    plot_assignment_2(df, out_folderpath)
    plot_assignment_3(df, out_folderpath)
    plot_assignment_4(df, out_folderpath)
    plot_all_assignments(df, out_folderpath)

if __name__ == "__main__":
    main()



