# Finantier data science tech test

### Project structure
`/api/app` contains the Dockerfile and the FastAPI application code.

`/api/test` contains test cases 

`/notebook` contains the notebook where I explored, cleaned and trained the model, which is then saved and used in the FastAPI application.

`api` and `/notebook` contains their own respective `requirements.txt`

### Running test cases
- `cd api`
- Run `pip install -r requirements.txt` in virtual environment
- Run `bash run_coverage.sh` to run test cases and get coverage report

```
Current test coverage 

Name              Stmts   Miss  Cover
-------------------------------------
app/__init__.py       0      0   100%
app/main.py          17      0   100%
app/model.py         54      0   100%
app/process.py       26      0   100%
-------------------------------------
TOTAL                97      0   100%
```

### Running the application
- `cd api`
- Run `bash build.sh` to build the docker image
- Run `bash run.sh` to run the docker container on port 8000


### Interacting with the application

- Using swagger docs to interact
  - After running `run.sh`, the swagger docs will be avaliable at `localhost:8000/docs`
  - Try out the `/ POST` endpoint to interact
  
  
- Interacting directly with the endpoint
  - Using FastAPI's model validation, all stated fields are required, with the appopriate values.
  - For more information on the required fields and the values, the model `TelcoData` on `localhost:8000/docs` will list them
  

##### Example POST request
```
{
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
```

##### Endpoint response


- For valid requests
```
# 200 response code
{
  "churn": 1
}
```

- Requests with missing fields (eg. `tenure` field missing)
```
# 422 response code
{
  "detail": [
    {
      "loc": [
        "body",
        "tenure"
      ],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

- Requests with incorrect field values (eg. Putting "3 year" in Contract)
```
# 422 response code
{
  "detail": [
    {
      "loc": [
        "body",
        "Contract"
      ],
      "msg": "value is not a valid enumeration member; permitted: 'Month-to-month', 'Two year', 'One year'",
      "type": "type_error.enum",
      "ctx": {
        "enum_values": [
          "Month-to-month",
          "Two year",
          "One year"
        ]
      }
    }
  ]
}
```

### Room for improvements
- Endpoint improvements
  - Possibly can allow the endpoint to take in a list of TelcoData, and return a list of predicted churn values
  - Endpoint data processing is quite messy
