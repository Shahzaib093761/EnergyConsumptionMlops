# Energy Consumption Forecaster API

This repository contains a FastAPI application for the EnergyConsumptionForecaster model. The application provides an API endpoint to forecast energy consumption based on input parameters. 

## Table of Contents
1. [Creating and Activating Virtual Environment](#creating-and-activating-virtual-environment)
2. [Installing Requirements](#installing-requirements)
3. [Starting the Development Server](#starting-the-development-server)
4. [Navigating Documentation](#navigating-documentation)
5. [Exploratory Data Analysis and Model Training](#exploratory-data-analysis-and-model-training)

## Creating and Activating Virtual Environment

To create and activate a virtual environment, follow these steps:

1. **Create a virtual environment** (replace `venv` with your preferred name):
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

## Installing Requirements

Once the virtual environment is activated, install the required packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Starting the Development Server

To start the FastAPI development server, run the following command:

```bash
python app.py
```

The server will start on `http://127.0.0.1:8000` by default.

## Navigating Documentation

You can access the automatically generated documentation for the API at the following endpoint:

- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

This documentation provides an overview of the available API endpoints and allows you to test them interactively.

## Exploratory Data Analysis and Model Training

In addition to the API, this repository includes a Jupyter Notebook for exploratory data analysis (EDA) and model training:

- **Notebook:** `Energy_Consumption_ForeCaster_EDA.ipynb`

You can open this notebook using Jupyter Notebook or Google Colab. The requirements for running the notebook are also specified in the `requirements.txt` file.

To run the notebook in Jupyter, ensure you have Jupyter installed in your virtual environment:

```bash
pip install jupyter
```

Then, you can launch Jupyter Notebook:

```bash
jupyter notebook
```

## Conclusion

You are now set up to run the Energy Consumption Forecaster API and explore the EDA and training notebook. If you have any questions or issues, feel free to open an issue in this repository.
