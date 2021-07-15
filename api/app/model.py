from enum import Enum

from pydantic import BaseModel


class Contract(str, Enum):
    month_to_month = "Month-to-month"
    two_year= "Two year"
    one_year = "One year"

class YesNoEnum(str, Enum):
    yes = "Yes"
    no = "No"

class YesNoWithInternetServiceEnum(str, Enum):
    yes = "Yes"
    no = "No"
    no_internet_service = "No internet service"

class YesNoWithPhoneServiceEnum(str, Enum):
    yes = "Yes"
    no = "No"
    no_phone_service = "No phone service"

class InternetServiceEnum(str, Enum):
    fiber_optic = "Fiber optic"
    dsl = "DSL"
    no = "No"

class PaymentMethodEnum(str, Enum):
    electronic_check = "Electronic check"
    mailed_check = "Mailed check"
    bank_transfer_auto = "Bank transfer (automatic)"
    credit_card_auto = "Credit card (automatic)"

class SeniorCitizenEnum(float, Enum):
    no = 0
    yes = 1

class GenderEnum(str, Enum):
    male = "Male"
    female = "Female"

class TelcoData(BaseModel):
    Contract: Contract
    Dependents: YesNoEnum
    DeviceProtection: YesNoWithInternetServiceEnum
    InternetService: InternetServiceEnum
    MultipleLines: YesNoWithPhoneServiceEnum
    OnlineBackup: YesNoWithInternetServiceEnum
    OnlineSecurity: YesNoWithInternetServiceEnum
    PaperlessBilling: YesNoEnum
    Partner: YesNoEnum
    PaymentMethod: PaymentMethodEnum
    PhoneService: YesNoEnum
    SeniorCitizen: SeniorCitizenEnum
    StreamingMovies: YesNoWithInternetServiceEnum
    StreamingTV: YesNoWithInternetServiceEnum
    TechSupport: YesNoWithInternetServiceEnum
    gender: GenderEnum
    tenure: float
    MonthlyCharges: float
    TotalCharges: float

    class Config:  
        use_enum_values = True 
