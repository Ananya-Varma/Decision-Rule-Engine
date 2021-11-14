
def calculate_loan_amount(monthly_income, personal_loan, home_loan, interest_rate, tenure):
    amount_payable = monthly_income - personal_loan - home_loan
    emi = calculate_emi(100000, interest_rate, tenure)
    loan_amount = (amount_payable/emi) * 100000

    return loan_amount


def calculate_emi(principal, interest_rate, tenure):
    monthly_interest_rate = interest_rate / 12
    emi = principal * (monthly_interest_rate / 100) * (1 + monthly_interest_rate / 100) ** tenure
    emi = emi / ((1 + monthly_interest_rate / 100) ** tenure - 1)

    return emi


def calculate_pemi_loan_amount(monthly_income, personal_loan, home_loan, interest_rate):
    amount_payable = monthly_income - personal_loan - home_loan
    interest_rate = interest_rate/1200
    emi_per_lakh = 100000 * interest_rate
    loan_amount = (amount_payable / emi_per_lakh) * 100000

    return loan_amount


def calculate_partial_interest_emi(partial_interest, principal, partial_interest_tenure, interest_rate,
                                   remaining_tenure):
    interest_paid = partial_interest * partial_interest_tenure
    additional_loan = (principal * (interest_rate / 1200) - partial_interest) * partial_interest_tenure
    total_loan = principal + additional_loan
    emi = calculate_emi(total_loan, interest_rate, remaining_tenure)

    return interest_paid, additional_loan, total_loan, emi


def print_repayment_option_1(product, applicant):

    total_monthly_income = applicant.income_profile["monthly_income"]
    serviceable_income = applicant.serviceable_income
    personal_loan = applicant.personal_loan
    home_loan = applicant.home_loan
    interest_rate = product["Interest Rate"]
    tenure = product["Max_Term"]
    study_period = applicant.study_period
    grace_period = applicant.grace_period

    loan_amount = calculate_pemi_loan_amount(serviceable_income, personal_loan, home_loan, interest_rate)
    emi = calculate_emi(loan_amount, interest_rate, tenure-study_period-grace_period)

    foir = int(serviceable_income/total_monthly_income * 100)
    iir = int((serviceable_income-personal_loan-home_loan)/total_monthly_income * 100)

    print("Repayment Mode: Full PEMI Option")
    print()
    print("Loan Amount: " + str(int(loan_amount)))
    print("Full Monthly PEMI: " + str(int(serviceable_income-personal_loan-home_loan)))
    print("Full PEMI Tenure: " + str(study_period+grace_period) + " months")
    print("Monthly EMI: " + str(int(emi)))
    print("Full EMI Tenure: " + str(tenure-study_period-grace_period) + " months")
    print("Interest Rate: " + str(product["Interest Rate"]) + "%")
    print("FOIR: " + str(foir) + "%")
    print("IIR: " + str(iir) + "%")
    print()


def print_repayment_option_2(product, applicant):

    total_monthly_income = applicant.income_profile["monthly_income"]
    monthly_income = applicant.serviceable_income
    personal_loan = applicant.personal_loan
    home_loan = applicant.home_loan
    interest_rate = product["Interest Rate"]
    tenure = product["Max_Term"]

    loan_amount = calculate_loan_amount(monthly_income, personal_loan, home_loan, interest_rate, tenure)
    emi = calculate_emi(loan_amount, interest_rate, tenure)

    foir = int((emi + personal_loan + home_loan) / total_monthly_income * 100)
    iir = int(emi / total_monthly_income * 100)

    print("Repayment Mode: Full EMI Option")
    print()
    print("Loan Amount: " + str(int(loan_amount)))
    print("Monthly EMI: " + str(int(emi)))
    print("Full EMI Tenure: 180 months")
    print("Interest Rate: " + str(product["Interest Rate"]) + "%")
    print("FOIR: " + str(foir) + "%")
    print("IIR: " + str(iir) + "%")
    print()


def print_repayment_option_3(product, applicant):

    loan_amount = product["Credit_Limit"]
    personal_loan = applicant.personal_loan
    home_loan = applicant.home_loan
    total_monthly_income = applicant.income_profile["monthly_income"]
    partial_interest = applicant.partial_interest_amount
    partial_interest_tenure = applicant.study_period + applicant.grace_period
    interest_rate = product["Interest Rate"]
    remaining_tenure = product["Max_Term"] - partial_interest_tenure

    interest_paid, unpaid_interest, total_loan, emi = calculate_partial_interest_emi(partial_interest, loan_amount, partial_interest_tenure, interest_rate, remaining_tenure)

    foir = int((partial_interest + personal_loan + home_loan) / total_monthly_income * 100)
    iir = int(partial_interest / total_monthly_income * 100)

    print("Repayment Mode: Partial Interest Option")
    print()
    print("Loan Amount: " + str(int(loan_amount)))
    print("Partial Interest Amount: " + str(partial_interest))
    print("Partial Interest Tenure: " + str(partial_interest_tenure) + " months")
    print("Paid Interest: " + str(interest_paid))
    print("Unpaid Interest: " + str(int(unpaid_interest)))
    print("Total Outstanding Loan: " + str(int(total_loan)))
    print("Monthly EMI: " + str(int(emi)))
    print("Full EMI Tenure: " + str(remaining_tenure) + " months")
    print("Interest Rate: " + str(product["Interest Rate"]) + "%")
    print("FOIR: " + str(foir) + "%")
    print("IIR: " + str(iir) + "%")
    print()


