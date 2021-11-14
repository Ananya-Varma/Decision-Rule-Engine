"""Parameters to be validated for loan eligibility"""

# Courses to be validated from the given list
COURSES = ["Engineering", "Information Technology", "Computer Science", "Biotechnology", "Architecture", "Economics"]

# GRE Scores to be validated
MAX_GRE_SCORE = 340

# TOEFL Scores to be validated
MAX_TOEFL_SCORE = 100

# IELTS Scores to be validated
MAX_IELTS_SCORE = 10

# Maximum Graduation Time
MAX_DELAY_IN_GRAD = 2

# UG Performance Cutoff
MAX_UG_SCORE = 100

# Academic performance to be validated
MAX_CLASS_12_SCORE = 100
MAX_CLASS_10_SCORE = 100

# Entity of Co-Borrower
CO_BORROWER_ENTITIES = ["Salaried", "Professional", "Self Employed", "Retired"]

# Location of Co-Borrower
CO_BORROWER_LOCATIONS = ["As per Location List", "Anywhere in India or abroad with one Local Coborrower. Repayment from ECS or DDM facility"]

# Accommodation of Co-Borrower
CO_BORROWER_ACCOMMODATIONS = ["KYC Norms to be Met", "Self Owned, Company or government provided (no minimum stay required) or Self rental with 3 years stability"]

# Relation with Main Co-Borrower
CO_BORROWER_RELATIONSHIP = ["Father", "Mother", "Spouse", "Brother", "Other Blood Relative"]

# FOIR Limit
MAX_FOIR_LIMIT = 100

# IIR Limit
MAX_IIR_LIMIT = 100

# Income Profiles to be validated
INCOME_PROFILES = [{"Monthly_Income": 15000, "ITR": 150000}, {"Monthly_Income": 25000, "ITR": 200000}]

# CIBIL Grid
CIBIL_CONDITIONS = ["Asset Product - Once 30 DPD in the last 12 months with no delay in last 3 months.",
                    "Asset Product - No Write Off or 30+ allowed.",
                    "Credit Cards  - Two times 0- 30 DPD allowed in last 12 months, but no delay in last 3 months.",
                    "Credit Cards - Write off up to 5k or settlement with nil outstanding balance - can be waived provided there is satisfactory PL repayment track record of at least 12 months with  nil bounces.",
                    "Asset Product - Once 30 DPD in the last 6 months with no delay in last 3 months in any Secured Asset Product(HL/LAP/Auto, etc).",
                    "Asset Product - No Write Off in Secured Asset Product (HL/LAP/Auto, etc)"]

# Loan Repayment Options
REPAYMENT_OPTIONS = ["PEMI Option", "EMI Option", "Partial Interest Option"]

