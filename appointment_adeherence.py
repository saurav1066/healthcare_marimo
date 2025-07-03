#%%

# import marimo

# __generated_with = "0.14.9"
# app = marimo.App()


# @app.cell
# def _():
#     import marimo as mo
#     import pandas as pd
#     return (pd,)


# @app.cell
# def _(pd):
#     df = pd.read_csv('data/medical_appointment.csv')
#     df.head()
#     return (df,)


# @app.cell
# def _(df):
#     df.describe()
#     return


# @app.cell
# def _():
#     return


# if __name__ == "__main__":
#     app.run()
#

import marimo

__generated_with = "0.14.9"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import pandas as pd

    return (pd,)


@app.cell
def _(pd):
    df =pd.read_csv('data/medical_appointment.csv')
    df.head()
    return (df,)


@app.cell
def _(df):
    df.describe()
    return


@app.cell
def _(df):
    # finding null values each column
    df.isnull().sum()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
