""" Driver Code for Interacting with the Applicant """
from applicant import Applicant
from products import *
from utils import *


def print_products(applicant, eligible_products):

    if applicant.ineligible_all or applicant.only_emi:
        product_list = PRODUCT_LIST[:1]

    else:
        product_list = eligible_products[:1]

    if applicant.only_emi:

        for product in product_list:
            print()
            print("Product Name: " + product["Product_Name"])
            print("Loan Type: Unsecured")
            print("Loan Repayment Options: ")
            print()

            print_repayment_option_2(product, applicant)

    elif applicant.ineligible_all:
        print("(Loan Approval Subject to Location List of Kuhoo)")
        for product in product_list:
            print()
            print("Product Name: " + product["Product_Name"])
            print("Loan Type: Unsecured")
            print("Loan Repayment Options: ")
            print()

            print_repayment_option_3(product, applicant)

    else:

        for product in product_list:
            print()
            print("Product Name: " + product["Product_Name"])
            print("Loan Type: Unsecured")
            print("Loan Repayment Options: ")
            print()

            print_repayment_option_1(product, applicant)
            print_repayment_option_2(product, applicant)

            if applicant.partial_interest_amount >= 2000:
                print_repayment_option_3(product, applicant)


def main():
    print()
    print("********* Welcome to the Kuhoo Loan Application Portal! *********")
    print()
    print("Dear Applicant, Please fill in your data as per the instructions: ")
    print()

    name = input("Enter your name: ")
    print()
    print("Please select the course for which you wish to apply for loan: ")
    print()
    print("1." + '\t' + "Masters in Science (MS, MTech...)")
    print("2." + '\t' + "Masters in Management (MBA, MIM...)")
    print()
    pgcourse = input("Your choice: ")

    pgcourse = int(pgcourse)

    if pgcourse == 1:

        course = input("Enter your course name: ")
        gre_score = input("Enter your GRE Score (Key in 0 if not applicable): ")
        toefl_score = input("Enter your TOEFL Score (Key in 0 if not applicable): ")
        sat_score = 0

        if int(toefl_score) == 0:
            ielts_score = input("Enter your IELTS Score (Key in 0 if not applicable): ")

        else:
            ielts_score = 0

    elif pgcourse == 2:

        course = ""
        sat_score = input("Enter your SAT Score (Key in 0 if not applicable): ")
        toefl_score = input("Enter your TOEFL Score (Key in 0 if not applicable): ")
        sat_score = 0

        if int(toefl_score) == 0:
            ielts_score = input("Enter your IELTS Score (Key in 0 if not applicable): ")

        else:
            ielts_score = 0

        gre_score = 0

    else:

        print("Invalid Input! Please key in a valid input")
        return

    grad_time = input("Delay in education (in years): ")
    study_period = input("Enter your study period (in months): ")
    grace_period = input("Enter your grace period (in months): ")
    ug_score = input("Enter your Undergraduate CGPA as percentage: ")
    class_12_score = input("Enter your Class 12th percentage: ")
    class_10_score = input("Enter your Class 10th percentage: ")

    print()
    print("Enter the entity of your Co-borrower from one of the following options: ")
    for i in range(len(CO_BORROWER_ENTITIES)):
        print(str(i + 1) + '\t' + CO_BORROWER_ENTITIES[i])
    print("For Other Entity, press any key")
    co_borrower_entity = input("Your choice: ")

    print()
    print("Enter the location of your Co-borrower from one of the following options: ")
    for i in range(len(CO_BORROWER_LOCATIONS)):
        print(str(i + 1) + '\t' + CO_BORROWER_LOCATIONS[i])
    print("For Other Entity, press any key")
    co_borrower_location = input("Your choice: ")

    print()
    print("Enter the accommodation of your Co-borrower from one of the following options: ")
    for i in range(len(CO_BORROWER_ACCOMMODATIONS)):
        print(str(i + 1) + '\t' + CO_BORROWER_ACCOMMODATIONS[i])
    print("For Other Entity, press any key")
    co_borrower_accommodation = input("Your choice: ")

    print()
    print("Enter your relationship with the Main Co-borrower from one of the following options: ")
    for i in range(len(CO_BORROWER_RELATIONSHIP)):
        print(str(i + 1) + '\t' + CO_BORROWER_RELATIONSHIP[i])
    print("For Other Entity, press any key")
    co_borrower_relationship = input("Your choice: ")

    print()
    # foir = 0 # input("Enter your FOIR as a percentage (Key in 0 if not applicable): ")
    # iir = 0 # input("Enter your IIR as a percentage (Key in 0 if not applicable): ")

    if int(co_borrower_entity) == 1:
        monthly_income = input("Enter Monthly Income in INR (Clubbing allowed for Father/Mother): ")

    elif int(co_borrower_entity) == 4:
        monthly_income = input("Enter Monthly Pension Income in INR: ")

    else:
        monthly_income = int(input("Enter Gross Annual Income in INR: "))/12

    itr = input("Enter your Annual ITR amount in INR: ")
    partial_interest_amount = input("Enter your serviceable partial interest amount (per month): ")
    print()
    cibil_status = input("Enter your CIBIL Hit Status (YES or NO): ")
    print()

    if cibil_status == "YES":
        personal_loan = input("Enter your monthly EMI amount on personal loan: ")
        home_loan = input("Enter your monthly EMI amount on home loan: ")

        print("Enter any one of the CIBIL Hit condition that you satisfy: ")
        for i in range(len(CIBIL_CONDITIONS)):
            print(str(i + 1) + '\t' + CIBIL_CONDITIONS[i])
        print("If none of the conditions apply, press any key")
        cibil_grid = input("Your choice: ")

    else:
        cibil_grid = -1
        personal_loan = 0
        home_loan = 0

    pgcourse = int(pgcourse)
    gre_score = int(gre_score)
    toefl_score = int(toefl_score)
    ielts_score = int(ielts_score)
    sat_score = int(sat_score)
    grad_time = int(grad_time)
    study_period = int(study_period)
    grace_period = int(grace_period)
    ug_score = int(ug_score)
    class_12_score = int(class_12_score)
    class_10_score = int(class_10_score)
    co_borrower_entity = int(co_borrower_entity)
    co_borrower_location = int(co_borrower_location)
    co_borrower_accommodation = int(co_borrower_accommodation)
    co_borrower_relationship = int(co_borrower_relationship)
    monthly_income = int(monthly_income)
    itr = int(itr)
    partial_interest_amount = int(partial_interest_amount)
    cibil_grid = int(cibil_grid)
    personal_loan = int(personal_loan)
    home_loan = int(home_loan)

    if co_borrower_entity <= len(CO_BORROWER_ENTITIES):
        co_borrower_entity = CO_BORROWER_ENTITIES[co_borrower_entity - 1]

    else:
        co_borrower_entity = "Other"

    if co_borrower_location <= len(CO_BORROWER_LOCATIONS):
        co_borrower_location = CO_BORROWER_LOCATIONS[co_borrower_location - 1]

    else:
        co_borrower_location = "Other"

    if co_borrower_accommodation <= len(CO_BORROWER_ACCOMMODATIONS):
        co_borrower_accommodation = CO_BORROWER_ACCOMMODATIONS[co_borrower_accommodation - 1]

    else:
        co_borrower_accommodation = "Other"

    if co_borrower_relationship <= len(CO_BORROWER_RELATIONSHIP):
        co_borrower_relationship = CO_BORROWER_RELATIONSHIP[co_borrower_relationship - 1]

    else:
        co_borrower_relationship = "Other"

    income_profile = {"monthly_income": monthly_income, "itr": itr}

    applicant = Applicant(name, pgcourse, course, gre_score, toefl_score, ielts_score, sat_score, grad_time, study_period, grace_period, ug_score, class_12_score,
                          class_10_score,
                          co_borrower_entity, co_borrower_location, co_borrower_accommodation, co_borrower_relationship,
                          income_profile, partial_interest_amount, cibil_status, cibil_grid, personal_loan, home_loan)
    eligible_products = applicant.check_loan_eligibility()

    if applicant.ineligible_all and applicant.partial_interest_amount < 2000:
        print()
        print("Dear " + applicant.name + ", you are not eligible for any of our loan offerings. We'll get back "
                                         "to you in case of future offerings.")

    else:
        print()
        print("Dear " + applicant.name + ", you are eligible for our following loan offerings")
        print_products(applicant, eligible_products)

    print()
    print("********* Thank you for choosing to work with Kuhoo! *********")
    print()


if __name__ == "__main__":
    main()
