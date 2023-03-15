![example workflow](https://github.com/ameyabhamare/FitMe/actions/workflows/build_test.yml/badge.svg)

[![Coverage Status](https://coveralls.io/repos/github/ameyabhamare/FitMe/badge.svg)](https://coveralls.io/github/ameyabhamare/FitMe)

## Fitness Tracker: A Usage Trends Analysis

### Goal
The end product is a tool that allows the user to upload their fitbit data and presents them with relevant insights pertaining to weight, activity, heartrate and calorific needs.

### Theme 
Human temporal routine behavioral analysis and pattern recognition.

## Development Environment
*We encourage using [pyenv](https://github.com/pyenv/pyenv) to set up and configure your Python development environment.*
*This repo was built using Python 3.8.5*

### Installation instructions
- Install dev dependencies by running `pip install -r requirements.txt`
- Download the [FitBit Kaggle dataset](https://www.kaggle.com/datasets/arashnic/fitbit) and extract it to the `data/` directory at the root of this project.

### Running the app
- We conveniently have a `./run.sh 80080` script you can run to start the application (this will launch app on port :8080)
OR
- Otherwise, you can use the `streamlit run app.py` command to run the application **after** installing the Python dependencies through pip.

### Testing
We have a suite of unit test that covers code within the `analysis` and `utils` Python module. You can easily run all the test suite using the `python run_tests.py` command which will execute the tests suites within the `tests/` folder. 

### Project structure
```
FitMe/                              # FitMe python module
├── app.py                          # main entrypoint
├── data/
│   ├── [sample datasets from kaggle]
├── analysis/                       # Analysis python module
│   ├── activity_analysis.py        # contains functions for processing activity data
│   ├── calories_analysis.py        # contains functions for processing calories data
│   ├── heartrate_analysis.py       # contains functions for processing heart rate data
│   ├── sleep_analysis.py           # contains functions for processing sleep data
│   ├── steps_analysis.py           # contains functions for processing steps data
├── utils/                          # Utils python module
│   ├── graph_utils.py              # contains utility functions for data visualization
│   ├── analysis_utils.py           # contains utility functions for analysis module
├── tests/                          # Tests python module
│   ├── [test files]
├── examples/
│   ├── [example files]
├── docs/
│   ├── [project documentation]
├── run_tests.py
├── run.sh
├── .github/
│   ├── [continuous integration environment config]
└── .vscode/
    ├── [vscode settings & extension recommendations]
```

### Continuous deployment
We're using Heroku to automatically deploy our application to our `prod` environment, which is available here: [http://fitme.herokuapp.com](http://fitme.herokuapp.com).

To deploy to `production`, dev can simply push on the Heroku remote `git push heroku main`. This step is automated in our CI build, which deploys automatically to Heroku if all unit tests are passing.

### Code health
#### Linting
We provided a `.pylintrc` file for you to use and configure your dev environment. 

### Questions
Our tool **FitMe** allows you to feed in your smart watch data to provide you with answer to questions like:
* How active are your days? Do you spend a considerable amount of time being sedentary?
* How does this data vary on weekdays vs weekends?
* What factors contribute to the highest calorie burn?
* Have you been following a steady sleep schedule? What factors influence it?
* Understand the sleep stages and find out what it takes to get a better deep sleep.
* What is the impact of a Netflix binge on weekend sleep?
* Use Machine Learning to see if there is a hidden pattern to attain better sleep

### Data sources
The [FitBit Fitness Tracker Data](https://www.kaggle.com/datasets/arashnic/fitbit) is a rich collection of 18 different csv files that collates information about daily activities, calorie, heartrate, sleep cycles, intensities and steps, among others.

### Contributors
* [Ameya Bhamare](https://github.com/ameyabhamare): ameyarb@uw.edu
* Akshit Miglani: amiglani@uw.edu | akshit.miglani09@gmail.com
* Harshit Rai: harshit@uw.edu
* Jeremie Poisson: jepoisso@uw.edu
