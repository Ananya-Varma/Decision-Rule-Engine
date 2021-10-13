""" Driver Code for Interacting with the Applicant """
from applicant import Applicant
from products import *


def main():
    print("****** Welcome to the Kuhoo Loan Application Portal! *****")
    print('\n')
    print("Dear Applicant, Please fill in your data as per the instructions: ")
    print('\n')

    name = input("Enter your name: ")
    course = input("Enter your course name: ")
    gre_score = input("Enter your GRE Score (Key in 0 if not applicable): ")
    toefl_score = input("Enter your TOEFL Score (Key in 0 if not applicable): ")
    ielts_score = input("Enter your IELTS Score (Key in 0 if not applicable): ")
    ug_score = input("Enter your Undergraduate CGPA as percentage: ")
    class_12_score = input("Enter your Class 12th percentage: ")
    class_10_score = input("Enter your Class 10th percentage: ")

    print("Enter the entity of your Co-borrower from one of the following options: ")
    for i in range(len(CO_BORROWER_ENTITIES)):
        print(str(i + 1) + '\t' + CO_BORROWER_ENTITIES[i])
    print("For Other Entity, press any key" + '\n')
    co_borrower_entity = input("Your choice: ")

    print("Enter the location of your Co-borrower from one of the following options: ")
    for i in range(len(CO_BORROWER_LOCATIONS)):
        print(str(i + 1) + '\t' + CO_BORROWER_LOCATIONS[i])
    print("For Other Entity, press any key" + '\n')
    co_borrower_location = input("Your choice: ")

    print("Enter the accommodation of your Co-borrower from one of the following options: ")
    for i in range(len(CO_BORROWER_ACCOMMODATIONS)):
        print(str(i + 1) + '\t' + CO_BORROWER_ACCOMMODATIONS[i])
    print("For Other Entity, press any key" + '\n')
    co_borrower_accommodation = input("Your choice: ")

    print("Enter your relationship with the Main Co-borrower from one of the following options: ")
    for i in range(len(CO_BORROWER_RELATIONSHIP)):
        print(str(i + 1) + '\t' + CO_BORROWER_RELATIONSHIP[i])
    print("For Other Entity, press any key" + '\n')
    co_borrower_relationship = input("Your choice: ")

    foir = input("Enter your FOIR as a percentage: ")
    iir = input("Enter your IIR as a percentage: ")
    monthly_income = input("Enter Monthly Income in INR (Clubbing allowed for Father/Mother): ")
    itr = input("Enter your Annual ITR amount in INR: ")
    cibil_status = input("Enter your CIBIL Hit Status (YES or NO): ")

    cibil_grid = -1
    if cibil_status == "YES":
        print("Enter any one of the CIBIL Hit condition that you satisfy: ")
        for i in range(len(CIBIL_CONDITIONS)):
            print(str(i + 1) + '\t' + CIBIL_CONDITIONS[i])
        print("If none of the conditions apply, press any key" + '\n')
        cibil_grid = input("Your choice: ")

    gre_score = int(gre_score)
    toefl_score = int(toefl_score)
    ielts_score = int(ielts_score)
    ug_score = int(ug_score)
    class_12_score = int(class_12_score)
    class_10_score = int(class_10_score)
    co_borrower_entity = int(co_borrower_entity)
    co_borrower_location = int(co_borrower_location)
    co_borrower_accommodation = int(co_borrower_accommodation)
    co_borrower_relationship = int(co_borrower_relationship)
    foir = int(foir)
    iir = int(iir)
    monthly_income = int(monthly_income)
    itr = int(itr)
    cibil_grid = int(cibil_grid)

    if co_borrower_entity < len(CO_BORROWER_ENTITIES):
        co_borrower_entity = CO_BORROWER_ENTITIES[co_borrower_entity]

    else:
        co_borrower_entity = "Other"

    if co_borrower_location < len(CO_BORROWER_LOCATIONS):
        co_borrower_location = CO_BORROWER_LOCATIONS[co_borrower_location]

    else:
        co_borrower_location = "Other"

    if co_borrower_accommodation < len(CO_BORROWER_ACCOMMODATIONS):
        co_borrower_accommodation = CO_BORROWER_ACCOMMODATIONS[co_borrower_accommodation]

    else:
        co_borrower_accommodation = "Other"

    if co_borrower_relationship < len(CO_BORROWER_RELATIONSHIP):
        co_borrower_relationship = CO_BORROWER_RELATIONSHIP[co_borrower_relationship]

    else:
        co_borrower_relationship = "Other"

    income_profile = {"monthly_income": monthly_income, "itr": itr}

    applicant = Applicant(name, course, gre_score, toefl_score, ielts_score, ug_score, class_12_score, class_10_score,
                          co_borrower_entity, co_borrower_location, co_borrower_accommodation, co_borrower_relationship,
                          foir, iir, income_profile, cibil_status, cibil_grid)
    eligible_products = applicant.check_loan_eligibility()

    if len(eligible_products) == 0:
        print(
            "Sorry, you are not eligible for any of our loan offerings. We'll get back to you in case of future "
            "offerings.")

    else:
        print(eligible_products)


if __name__ == "__main__":
    main()