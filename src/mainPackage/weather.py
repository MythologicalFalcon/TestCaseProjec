import pandas as pd


def getColumns(df):
  return df.columns


def getMinTemp(df):
  return df['MinTemp'].min()


def getMaxTemp(df):
  return df['MaxTemp'].max()


def avgTemp(df):
  combined_average = (df['MinTemp'] + df['MaxTemp']).mean()
  return combined_average


def calculate_average(row):
  selected_columns = [
      'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
      'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am',
      'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm',
      'Temp9am', 'Temp3pm'
  ]
  total = sum([row[col] for col in selected_columns])
  return total / len(selected_columns)


def readData():
  df = pd.read_csv('src/resources/weather.csv')
  print(df.head())
  print(getColumns(df))
  print(getMinTemp(df))
  print(getMaxTemp(df))
  print(avgTemp(df))
  df['average'] = df.apply(calculate_average, axis=1)
  print(df['average'].head())
