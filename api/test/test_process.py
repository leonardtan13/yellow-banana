import unittest

import pandas as pd
from app.main import app
from app.process import process_binary, process_request
from fastapi.testclient import TestClient


class TestMain(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_process_binary(self):
        df = pd.DataFrame(data={
            'Dependents': ['Yes'],
            'PaperlessBilling': ['No'],
            'Partner': ['No'],
            'PhoneService': ['No']
        })

        df_result = process_binary(df)
        self.assertEqual(1, df_result.Dependents[0])
        self.assertEqual(0, df_result.PaperlessBilling[0])
        self.assertEqual(0, df_result.Partner[0])
        self.assertEqual(0, df_result.PhoneService[0])

    def test_process_request_have_correct_columns(self):
        request = {
            "Contract": "Month-to-month",
            "Dependents": "Yes",
            "DeviceProtection": "Yes",
            "InternetService": "Fiber optic",
            "MultipleLines": "Yes",
            "OnlineBackup": "Yes",
            "OnlineSecurity": "Yes",
            "PaperlessBilling": "Yes",
            "Partner": "Yes",
            "PaymentMethod": "Electronic check",
            "PhoneService": "Yes",
            "SeniorCitizen": 0,
            "StreamingMovies": "Yes",
            "StreamingTV": "Yes",
            "TechSupport": "Yes",
            "gender": "Male",
            "tenure": 0,
            "MonthlyCharges": 0,
            "TotalCharges": 0
            }

        columns = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
       'PhoneService', 'PaperlessBilling', 'MonthlyCharges', 'TotalCharges',
       'MultipleLines_No', 'MultipleLines_No_phone_service',
       'MultipleLines_Yes', 'InternetService_DSL',
       'InternetService_Fiber_optic', 'InternetService_No',
       'OnlineSecurity_No', 'OnlineSecurity_No_internet_service',
       'OnlineSecurity_Yes', 'OnlineBackup_No',
       'OnlineBackup_No_internet_service', 'OnlineBackup_Yes',
       'DeviceProtection_No', 'DeviceProtection_No_internet_service',
       'DeviceProtection_Yes', 'TechSupport_No',
       'TechSupport_No_internet_service', 'TechSupport_Yes', 'StreamingTV_No',
       'StreamingTV_No_internet_service', 'StreamingTV_Yes',
       'StreamingMovies_No', 'StreamingMovies_No_internet_service',
       'StreamingMovies_Yes', 'Contract_Month_to_month', 'Contract_One_year',
       'Contract_Two_year', 'PaymentMethod_Bank_transfer__automatic_',
       'PaymentMethod_Credit_card__automatic_',
       'PaymentMethod_Electronic_check', 'PaymentMethod_Mailed_check']

        df = process_request(request)

        self.assertEqual(40, df.shape[1])
        for col in columns:
            self.assertTrue(col in df.columns)



if __name__ == '__main__':
    unittest.main()
