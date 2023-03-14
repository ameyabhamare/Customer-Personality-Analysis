![example workflow](https://github.com/ameyabhamare/FitMe/actions/workflows/build_test.yml/badge.svg)

## Fitness Tracker: A Usage Trends Analysis

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

### Continuous deployment
We're using Heroku to automatically deploy our application to our `prod` environment, which is available here: [http://fitme.herokuapp.com](http://fitme.herokuapp.com).

To deploy to `production`, dev can simply push on the Heroku remote `git push heroku main`. This step is automated in our CI build, which deploys automatically to Heroku if all unit tests are passing.

### Code health
#### Linting
We provided a `.pylintrc` file for you to use and configure your dev environment. 

### Questions
We propose a tool **FitMe** that allows you to feed in your smart watch data to provide you with answer to questions
* How active are your days? Do you spend a considerable amount of time being sedentary?
* How does this data vary on weekdays vs weekends?
* What factors contribute to the highest calorie burn?
* Have you been following a steady sleep schedule? What factors influence it?
* Understand the sleep stages and find out what it takes to get a better deep sleep.
* What is the impact of a Netflix binge on weekend sleep?
* Use Machine Learning to see if there is a hidden pattern to attain better sleep

### Goal
The end product will be a tool that functions as described above. We will host it on the Cloud with an ML model and EDA pipelines running in the background. 

### Data sources
The [FitBit Fitness Tracker Data](https://www.kaggle.com/datasets/arashnic/fitbit) is a rich collection of 18 different csv files that collates information about daily activities, calorie, heartrate, sleep cycles, intensities and steps, among others.

### Contributors
Ameya Bhamare, Akshit Miglani, Harshit Rai, Jeremie Poisson
