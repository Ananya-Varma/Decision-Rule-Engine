""" Template for attributes and methods of a loan applicant """
from products import *


class Applicant:

    def __init__(self, name, course, gre_score, toefl_score, ielts_score, grad_time, ug_score, class_12_score,
                 class_10_score,
                 co_borrower_entity, co_borrower_location, co_borrower_accommodations, co_borrower_relationship, foir,
                 iir, income_profile, cibil_status, cibil_grid):
        self.name = name
        self.course = course
        self.gre_score = gre_score
        self.toefl_score = toefl_score
        self.ielts_score = ielts_score
        self.grad_time = grad_time
        self.ug_score = ug_score
        self.class_12_score = class_12_score
        self.class_10_score = class_10_score
        self.co_borrower_entity = co_borrower_entity
        self.co_borrower_location = co_borrower_location
        self.co_borrower_accommodations = co_borrower_accommodations
        self.co_borrower_relationship = co_borrower_relationship
        self.foir = foir
        self.iir = iir
        self.income_profile = income_profile
        self.cibil_status = cibil_status
        self.cibil_grid = cibil_grid
        self.products = [True for i in range(len(PRODUCT_LIST))]

    def validate_course(self):

        for i in range(len(PRODUCT_LIST)):

            if self.products[i] and self.course not in PRODUCT_LIST[i]["eligibility"]["courses"]:
                self.products[i] = False

    def validate_gre_score(self):

        for i in range(len(PRODUCT_LIST)):

            if self.products[i] and self.gre_score < PRODUCT_LIST[i]["eligibility"]["gre"]:
                self.products[i] = False

    def validate_toefl_and_ielts_score(self):

        for i in range(len(PRODUCT_LIST)):

            if self.products[i] and self.toefl_score < PRODUCT_LIST[i]["eligibility"]["toefl"] and self.ielts_score < \
                    PRODUCT_LIST[i]["eligibility"]["ielts"]:
                self.products[i] = False

    def validate_grad_time(self):

        for i in range(len(PRODUCT_LIST)):

            if self.products[i] and PRODUCT_LIST[i]["eligibility"]["max_grad_time"] != -1 and self.grad_time > PRODUCT_LIST[i]["eligibility"]["max_grad_time"]:
                self.products[i] = False

    def validate_ug_score(self):

        for i in range(len(PRODUCT_LIST)):

            if self.products[i] and self.ug_score < PRODUCT_LIST[i]["eligibility"]["ug"]:
                self.products[i] = False

    def validate_class_12_and_10_score(self):

        for i in range(len(PRODUCT_LIST)):

            if self.products[i] and self.class_12_score < PRODUCT_LIST[i]["eligibility"][
                "class_12"] or self.class_10_score < PRODUCT_LIST[i]["eligibility"]["class_10"]:
                self.products[i] = False

    def validate_co_borrower_entity(self):

        for i in range(len(PRODUCT_LIST)):

            if self.products[i] and self.co_borrower_entity not in PRODUCT_LIST[i]["eligibility"]["co_borrower_entity"]:
                self.products[i] = False

    def validate_co_borrower_location(self):

        for i in range(len(PRODUCT_LIST)):

            if self.products[i] and self.co_borrower_location not in PRODUCT_LIST[i]["eligibility"][
                "co_borrower_location"]:
                self.products[i] = False

    def validate_co_borrower_accommodation(self):

        for i in range(len(PRODUCT_LIST)):

            if self.products[i] and self.co_borrower_accommodations not in PRODUCT_LIST[i]["eligibility"]["co_borrower_accommodations"]:
                self.products[i] = False

    def validate_co_borrower_relationship(self):

        for i in range(len(PRODUCT_LIST)):

            if self.products[i] and self.co_borrower_relationship not in PRODUCT_LIST[i]["eligibility"]["co_borrower_relationship"]:
                self.products[i] = False

    def validate_income_profile(self):

        itr_entities = ["Professional", "Self Employed"]

        for i in range(len(PRODUCT_LIST)):

            if self.products[i] and self.co_borrower_entity == "Salaried":
                if self.products[i] and self.income_profile["monthly_income"] < PRODUCT_LIST[i]["eligibility"]["monthly_income"]:
                    self.products[i] = False

            elif self.products[i] and self.co_borrower_entity in itr_entities:
                if self.products[i] and self.co_borrower_entity in itr_entities and self.income_profile["itr"] < \
                        PRODUCT_LIST[i]["eligibility"]["itr"]:
                    self.products[i] = False

    def validate_foir(self):

        for i in range(len(PRODUCT_LIST)):

            if self.products[i] and self.foir > PRODUCT_LIST[i]["eligibility"]["foir"]:
                self.products[i] = False

    def validate_iir(self):

        for i in range(len(PRODUCT_LIST)):

            if self.products[i] and self.iir > PRODUCT_LIST[i]["eligibility"]["iir"]:
                self.products[i] = False

    def validate_cibil_status_and_grid(self):

        if self.cibil_status == "NO":
            return

        elif self.cibil_status == "YES" and (len(CIBIL_CONDITIONS) - 2) < self.cibil_grid <= (len(CIBIL_CONDITIONS)):

            for i in range(len(PRODUCT_LIST) - 1):
                self.products[i] = False

        elif self.cibil_status == "YES" and self.cibil_grid > (len(CIBIL_CONDITIONS)) or self.cibil_grid <= 0:

            for i in range(len(PRODUCT_LIST)):
                self.products[i] = False

    def check_loan_eligibility(self):

        self.validate_course()
        self.validate_gre_score()
        self.validate_toefl_and_ielts_score()
        self.validate_grad_time()
        self.validate_ug_score()
        self.validate_class_12_and_10_score()
        self.validate_co_borrower_entity()
        self.validate_co_borrower_location()
        self.validate_co_borrower_accommodation()
        self.validate_co_borrower_relationship()
        self.validate_income_profile()
        self.validate_foir()
        self.validate_iir()
        self.validate_cibil_status_and_grid()

        eligible_products = []

        for i in range(len(self.products)):

            if self.products[i]:
                eligible_products.append(PRODUCT_LIST[i])

        return eligible_products
