"""Product Profiles to be offered"""
from params import *

PRODUCT_1 = {"Product_Name": "US MS PG1",
             "Credit_Limit":  "Upto INR 50,00,000",
             "Max_Term": 156,
             "Grace": 12,
             "Interest Rate": 12.5,
             "EMI": 64988,
             "Partial Interest": "2000",
             "Prepayment": "NA",
             "Collateral": "NA",
             "Product_Info": ["Full PEMI Option to be serviced during study & grace period", "EMI Option", "Partial Int of Rs. 2000 or more to be serviced during study & grace period"],
             "Moratorium": "YES",
             "eligibility": {"courses": COURSES[:-2], "gre": 320, "toefl": 95, "ielts": 6, "max_grad_time": -1, "ug": 0, "class_12": 0, "class_10": 0, "co_borrower_entity": CO_BORROWER_ENTITIES,
                             "co_borrower_location": CO_BORROWER_LOCATIONS, "co_borrower_accommodations": CO_BORROWER_ACCOMMODATIONS,
                             "co_borrower_relationship": CO_BORROWER_RELATIONSHIP[:-1], "monthly_income": 15000, "itr": 150000,
                             "foir": 100, "iir": 100}}

PRODUCT_2 = {"Product_Name": "US MS PG2",
             "Credit_Limit":  "Upto INR 40,00,000",
             "Max_Term": 156,
             "Grace": 12,
             "Interest Rate": 12.5,
             "EMI": 50747,
             "Partial Interest": "2000",
             "Prepayment": "NA",
             "Collateral": "NA",
             "Product_Info": ["Full PEMI Option to be serviced during study & grace period", "EMI Option", "Partial Int of Rs. 2000 or more to be serviced during study & grace period"],
             "Moratorium": "YES",
             "eligibility": {"courses": COURSES[:-2], "gre": 300, "toefl": 95, "ielts": 6, "max_grad_time": -1, "ug": 0, "class_12": 0, "class_10": 0, "co_borrower_entity": CO_BORROWER_ENTITIES,
                             "co_borrower_location": CO_BORROWER_LOCATIONS, "co_borrower_accommodations": CO_BORROWER_ACCOMMODATIONS,
                             "co_borrower_relationship": CO_BORROWER_RELATIONSHIP[:-1], "monthly_income": 25000, "itr": 200000,
                             "foir": 100, "iir": 100}}

PRODUCT_3 = {"Product_Name": "US MS PG3",
             "Credit_Limit":  "Upto INR 35,00,000",
             "Max_Term": 144,
             "Grace": 12,
             "Interest Rate": 12.5,
             "EMI": 47035,
             "Partial Interest": "2000",
             "Prepayment": "NA",
             "Collateral": "NA",
             "Product_Info": ["Full PEMI Option to be serviced during study & grace period", "EMI Option", "Partial Int of Rs. 2000 or more to be serviced during study & grace period"],
             "Moratorium": "YES",
             "eligibility": {"courses": COURSES[:-2], "gre": 290, "toefl": 85, "ielts": 6, "max_grad_time": 5, "ug": 0, "class_12": 0, "class_10": 0, "co_borrower_entity": CO_BORROWER_ENTITIES,
                             "co_borrower_location": CO_BORROWER_LOCATIONS, "co_borrower_accommodations": CO_BORROWER_ACCOMMODATIONS,
                             "co_borrower_relationship": CO_BORROWER_RELATIONSHIP[:-1], "monthly_income": 25000, "itr": 200000,
                             "foir": 100, "iir": 100}}

PRODUCT_4 = {"Product_Name": "US MS PG4",
             "Credit_Limit":  "Upto INR 30,00,000",
             "Max_Term": 144,
             "Grace": 12,
             "Interest Rate": 12.5,
             "EMI": 39403,
             "Partial Interest": "NA",
             "Prepayment": "NA",
             "Collateral": "NA",
             "Product_Info": ["Full PEMI Option to be serviced during study & grace period", "EMI Option", "Partial Int of Rs. 2000 or more to be serviced during study & grace period"],
             "Moratorium": "YES",
             "eligibility": {"courses": COURSES[:-2], "gre": 0, "toefl": 80, "ielts": 5, "max_grad_time": 5, "ug": 0, "class_12": 65, "class_10": 65, "co_borrower_entity": CO_BORROWER_ENTITIES,
                             "co_borrower_location": CO_BORROWER_LOCATIONS, "co_borrower_accommodations": CO_BORROWER_ACCOMMODATIONS,
                             "co_borrower_relationship": CO_BORROWER_RELATIONSHIP, "monthly_income": 25000, "itr": 200000,
                             "foir": 65, "iir": 60}}

PRODUCT_LIST = [PRODUCT_1, PRODUCT_2, PRODUCT_3, PRODUCT_4]

