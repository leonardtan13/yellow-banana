from fastapi.testclient import TestClient
from app.main import app

import unittest


class TestMain(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_docs(self):
        response = self.client.get("/docs")
        self.assertEqual(200, response.status_code)

    def test_missing_field_should_return_422(self):
        request = {}
        response = self.client.post("/", data=request)
        self.assertEqual(422, response.status_code)

    def test_correct_fields_should_return_churn_value(self):
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
        response = self.client.post("/", json=request)
        self.assertEqual(200, response.status_code)
        self.assertTrue('churn' in response.json())
    

if __name__ == '__main__':
    unittest.main()