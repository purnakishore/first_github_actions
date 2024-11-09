# ETL Pipeline Automation with GitHub Actions

## Overview
This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline automated using GitHub Actions. The pipeline extracts data from an external source, transforms it, and loads it into a **MongoDB Atlas cluster**. The entire process is scheduled and automated to run seamlessly using GitHub Actions.

## Features
- **Automated ETL Pipeline**: Runs on a schedule using GitHub Actions.
- **Data Extraction**: Fetches data from various APIs or external sources.
- **Data Transformation**: Cleans and processes raw data for meaningful insights.
- **Data Loading**: Loads the transformed data into a MongoDB Atlas database.
- **CI/CD Integration**: Automated testing and deployment.

## Technologies Used
- **Python**: Core scripting language for the ETL pipeline.
- **MongoDB Atlas**: Cloud database for storing the transformed data.
- **GitHub Actions**: Workflow automation for CI/CD.
- **Docker** (Optional): For containerization.

## Prerequisites
- **Python: 3.8+**
- **MongoDB Atlas Account**: Ensure you have a MongoDB Atlas cluster set up.
- **GitHub Account**: For setting up GitHub Actions.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/purnakishore/first_github_actions.git
cd first_github_actions
```

### 2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Add your API keys and database credentials to GitHub Secrets.


## Running Locally
### To run the pipeline manually:

```bash
python app.py
```

## GitHub Actions
- The pipeline is triggered on a schedule (cron) or on push events.
- Configuration is defined in .github/workflows/main.yml.

## Contributing

Feel free to open issues or submit pull requests.