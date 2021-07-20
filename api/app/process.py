import pandas as pd

columns = [
    'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
    'PhoneService', 'PaperlessBilling', 'MonthlyCharges', 'TotalCharges',
    'MultipleLines_No', 'MultipleLines_No_phone_service', 'MultipleLines_Yes',
    'InternetService_DSL', 'InternetService_Fiber_optic', 'InternetService_No',
    'OnlineSecurity_No', 'OnlineSecurity_No_internet_service',
    'OnlineSecurity_Yes', 'OnlineBackup_No',
    'OnlineBackup_No_internet_service', 'OnlineBackup_Yes',
    'DeviceProtection_No', 'DeviceProtection_No_internet_service',
    'DeviceProtection_Yes', 'TechSupport_No',
    'TechSupport_No_internet_service', 'TechSupport_Yes', 'StreamingTV_No',
    'StreamingTV_No_internet_service', 'StreamingTV_Yes', 'StreamingMovies_No',
    'StreamingMovies_No_internet_service', 'StreamingMovies_Yes',
    'Contract_Month_to_month', 'Contract_One_year', 'Contract_Two_year',
    'PaymentMethod_Bank_transfer__automatic_',
    'PaymentMethod_Credit_card__automatic_', 'PaymentMethod_Electronic_check',
    'PaymentMethod_Mailed_check'
]

binary_cols = ['Dependents', 'PaperlessBilling', 'Partner', 'PhoneService']


def process_binary(df_data):
    for col in binary_cols:
        df_data[col] = df_data[col].transform(lambda x: 1 if x == 'Yes' else 0)

    return df_data


def process_request(request_body):
    df_data = pd.DataFrame(data=request_body, index=[0])
    df_data['tenure'] = pd.to_numeric(df_data['tenure'], downcast='float')
    df_data['MonthlyCharges'] = pd.to_numeric(df_data['MonthlyCharges'],
                                              downcast='float')
    df_data['TotalCharges'] = pd.to_numeric(df_data['TotalCharges'],
                                            downcast='float')

    df_data['gender'] = df_data['gender'].transform(lambda x: 1
                                                    if x == 'Male' else 0)
    df_data = process_binary(df_data)

    dummy_columns = []

    for column in df_data.columns:
        if df_data[column].dtype == object and (column != 'gender'
                                                or column not in binary_cols):
            dummy_columns.append(column)

    df_data = pd.get_dummies(data=df_data, columns=dummy_columns)

    all_columns = []
    for column in df_data.columns:
        column = column.replace(" ", "_").replace("(", "_").replace(
            ")", "_").replace("-", "_")
        all_columns.append(column)

    df_data.columns = all_columns

    df_result = pd.DataFrame(columns=columns)

    return pd.concat([df_result, df_data], axis=0).fillna(0)
