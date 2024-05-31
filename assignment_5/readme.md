# Assignment 5: Evaluating environmental impact of my exam portfolio


## About

This project evaluates how much CO2 (measured as kilograms of CO₂-equivalent) the four assignments in this exam portfolio emit, tracking each task with ``code carbon``. The objective is to examine the environmental impact of each assignment and the portfolio as a whole.

The ``src`` directory contains one script: 

- **codecarbon.py:** Processes the csv files produce by code carbon and merges them into on large data frame. It then filters the data frame by project name and creates a new one for each of the four assignments, and from these creates a plot displaying CO2 emissions for each task in the assignment, as well as across all assignments.


### Data

Each of the four portfolio assignments produce the csv files used for this project and places them in the emissions folder. For each assignment code carbon initializes an [EmissionsTracker][] object, which tracks each function placed in the main function, and returns the emissions files. *See the approach used in this portfolio down below.*

```sh
from codecarbon import EmissionsTracker

tracker = EmissionsTracker(project_name="emotion_analysis",
                               output_file="emissions.csv",
                               output_dir=emissions_folderpath) 

tracker.start_task("initialize_argparse")

# Function to track

tracker.stop_task()

tracker.stop()

```

##  File Structure

```
└── assignment_5
        |
        |
        ├── emissions
        |   ├── emissions_base_0.csv
        |   ├── emissions_base_1.csv
        |   ├── ...
        │   └── emissions_base_5.csv
        |
        ├── out
        |   ├── all_assignments.png
        |   ├── all_emissions.csv
        |   ├── emotion_analysis.png
        |   ├── linguistic_analysis.png
        |   ├── query_expansion.png
        |   └── text_classification.png
        |
        ├── src
        │   └── codecarbon.py
        │     
        ├── readme.md
        ├── requirements.txt
        ├── run.sh
        └── setup.sh

```

## Usage

If you want to reproduce this project, please follow the steps below. The instructions will help you set up the environment and run the script.

### Pre-Requisites

*Please make sure to install the following requirements before running the script.*

**Python**: version 3.12.3

### Installation

**1.** Clone the repository using Git.
```sh
git clone https://github.com/trinerye/language_analytics_2024.git 
```

**2.** Change directory to the assignment folder.
```sh
cd assignment_5
```

**3.** Run ``setup.sh`` to create an environment and install the dependencies needed for this project. 

```sh
bash setup.sh
```
**4.** Run ``run.sh`` to activate the environment and run the main script. 
  
```sh
bash run.sh
```
```sh
...
# Activate the environment (Unix/macOS)
source ./LA_A5_env/bin/activate

# Run the code
python src/codecarbon.py

# Deactivate the environment
deactivate
```

## Results 


### Limitations and future improvments 









