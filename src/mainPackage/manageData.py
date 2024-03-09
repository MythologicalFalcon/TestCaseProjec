import pandas as pd
import ast
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder 

def is_preprocessed(data):
    # Check if the data has the correct number of columns
    expected_columns = [
        "Test Case",
        "Input",
        "Maximum Subarray Sum",
        "Branch_Coverage",
        "Statement_Coverage",
        "Function_Coverage",
        "Execution_Time",
        "Adequacy_Score",
        "Adequacy_Label"
    ]
    if len(data[0]) != len(expected_columns):
        return False

    # Check if all rows have the correct number of elements
    for row in data:
        if len(row) != len(expected_columns):
            return False

    # Check if the "Input" column contains lists of integers
    for row in data:
        try:
            input_list = ast.literal_eval(row[1])
            if not isinstance(input_list, list):
                return False
            for item in input_list:
                if not isinstance(item, int):
                    return False
        except (SyntaxError, ValueError):
            return False

    # Check if other columns have valid data types or formats
    for row in data:
        try:
            float(row[2])  # Maximum Subarray Sum
            float(row[3])  # Branch_Coverage
            float(row[4])  # Statement_Coverage
            if not row[5].endswith('%'):  # Function_Coverage
                return False
            float(row[6])  # Execution_Time
            float(row[7])  # Adequacy_Score
            if row[8] not in ['low', 'mid']:  # Adequacy_Label
                return False
        except ValueError:
            return False

    return True

def randomForestClassifier(df):
    df['Function_Coverage'] = df['Function_Coverage'].str.rstrip('%').astype(float) / 100.0
    df['Maximum Subarray Sum'] = pd.to_numeric(df['Maximum Subarray Sum'], errors='coerce')
    df['Execution_Time'] = pd.to_numeric(df['Execution_Time'], errors='coerce')
    df = df.dropna()
    df['Input'] = df['Input'].apply(lambda x: len(eval(x)))
    label_encoder = LabelEncoder()
    df['Adequacy_Label'] = label_encoder.fit_transform(df['Adequacy_Label'])
    numeric_columns = ['Input', 'Maximum Subarray Sum', 'Branch_Coverage', 'Statement_Coverage','Function_Coverage', 'Execution_Time', 'Adequacy_Score', 'Adequacy_Label']
    df = df[numeric_columns].astype(float)
    X = df.drop('Adequacy_Label', axis=1)
    y = df['Adequacy_Label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=50)
    rf_classifier = RandomForestClassifier(n_estimators=10000, random_state=50)
    rf_classifier.fit(X_train, y_train)
    y_pred = rf_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)


df = pd.read_csv('./src/resources/final_test_dataset_RF.csv')
data = df.values.tolist()

if is_preprocessed(data):
    print("The data is preprocessed.")
    randomForestClassifier(df)
else:
    # Call the preprocessing function
    print("The data is not preprocessed.")
    randomForestClassifier(df)


