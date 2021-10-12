"""Parameters to be validated for loan eligibility"""

# Courses to be validated from the given list
COURSES = ["Engineering", "Information Technology", "Computer Science", "Biotechnology", "Architecture", "Other"]

# GRE Scores to be validated
GRE_CUTOFFS = [320, 300, 290]

# TOEFL Scores to be validated
TOEFL_CUTOFFS = [95, 85, 80]

# IELTS Scores to be validated
IELTS_CUTOFFS = [6, 5]

# Maximum Graduation Time
MAX_TIME_TO_GRADUATE = 5

# UG Performance Cutoff
UG_CUTOFF = 65

# Academic performance to be validated
CLASS_12_AND_10_CUTOFF = 65

# Entity of Co-Borrower
CO_BORROWER_ENTITIES = ["Salaried", "Professional", "Self Employed", "Retired"]

# Location of Co-Borrower
CO_BORROWER_LOCATIONS = ["As per Location List", "India"]

# Accomodation of Co-Borrower
CO_BORROWER_ACCOMMODATIONS = ["KYC Norms to be Met", "Self Owned, Company or government provided (no minimum stay required) or Self rental with 3 years stability"]

# Relation with Main Co-Borrower
CO_BORROWER_RELATIONSHIP = ["Father", "Mother", "Spouse", "Brother", "Other Blood Relative"]

# FOIR Limit
FOIR_LIMIT = 65

# IIR Limit
IIR_LIMIT = 65

# Income Profiles to be validated
INCOME_PROFILES = [{"Monthly_Income": 15000, "ITR": 150000}, {"Monthly_Income": 25000, "ITR": 200000}]

# CIBIL Grid
CIBIL_CONDITIONS = ["Asset Product - Once 30 DPD in the last 12 months with no delay in last 3 months.",
                    "Asset Product - No Write Off or 30+ allowed.",
                    "Credit Cards  - Two times 0- 30 DPD allowed in last 12 months, but no delay in last 3 months.",
                    "Credit Cards - Write off up to 5k or settlement with nil outstanding balance - can be waived provided there is satisfactory PL repayment track record of at least 12 months with  nil bounces.",
                    "Asset Product - Once 30 DPD in the last 6 months with no delay in last 3 months in any Secured Asset Product(HL/LAP/Auto, etc).",
                    "Asset Product - No Write Off in Secured Asset Product (HL/LAP/Auto, etc)"]

