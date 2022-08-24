"""Classes for melon orders."""

import random
import datetime


# class DomesticMelonOrder:
#     """A melon order within the USA."""

#     def __init__(self, species, qty):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.shipped = False
#         self.order_type = "domestic"
#         self.tax = 0.08

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True


# class InternationalMelonOrder:
#     """An international (non-US) melon order."""

#     def __init__(self, species, qty, country_code):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.country_code = country_code
#         self.shipped = False
#         self.order_type = "international"
#         self.tax = 0.17

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True

#     def get_country_code(self):
#         """Return the country code."""

#         return self.country_code

# --------------------------------------------------------

# create base class: AbstractMelonOrder
#   capture the common variables between international and domestic 
#   def __init__(self):
    # self.shipped = False
    # self.tax = 0  

#   def get_total():
    # """Calculate price, including tax."""
    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price
    #     return total

# def mark_shipped(self):
        # """Record the fact than an order has been shipped."""
        # self.shipped = True



# create InternationalMelonOrder(AbstractMelonOrder) class
#   capture the diff variable in international order
#   def __init__(self, species, qty, country_code):
        # super().__init__()
        # self.species = species
        # self.qty = qty
        # self.country_code = country_code
        # self.order_type = "international"
        # self.tax = 0.17
    
    # def get_country_code(self):
    #        """Return the country code."""
    #         return self.country_code



# create DomesticMelonOrder(AbstractMelonOrder) class
#   capture the diff variable in domestic order
#   def __init__(self, species, qty):
        # super().__init__()
        # self.species = species
        # self.qty = qty
        # self.order_type = "domestic"
        # self.tax = 0.08



class AbstractMelonOrder:
    """ Create an abstract melon order class """

    def __init__(self):
        self.shipped = False
        self.tax = 0  
        self.qty = 0

#  import datetime library
#  get variables; day of the week = date.isoweekday() ; time = datetime.time()
#  if day of the week < 6 and 8 <= time <= 11:
#       base_price = random.choice(list(range(5,9))) +4
# else:
#       base_price = random.choice(list(range(5,9)))


    def get_base_price(self):
        """get the random base_price"""

        now = datetime.datetime.now()
        
        print(now.weekday())
        # if now.hour >= 8 and now.hour <= 11 and now.weekday() < 5:
        #     base_price = random.choice(list(range(5,9))) + 4
        # else:
        #    base_price = random.choice(list(range(5,9)))
        # return base_price


    def get_total(self):
        """Calculate price, including tax."""

        if self.species == "Christmas melons":
            base_price = self.get_base_price() * 1.5
        else:
            base_price = self.get_base_price()
        
        if self.order_type == "international" and self.qty < 10:
            total = ((1 + self.tax) * self.qty * base_price) + 3
        else:
            total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """capture the diff variable in international order"""

    def __init__(self, species, qty, country_code):
        super().__init__()
        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17
    
        if qty > 100:
            raise TooManyMelonsError 

    def get_country_code(self):
        """Return the country code."""
        return self.country_code

class DomesticeMelonOrder(AbstractMelonOrder):
    """create DomesticMelonOrder(AbstractMelonOrder) class
    capture the diff variable in domestic order"""

    def __init__(self, species, qty):
        super().__init__()
        self.species = species
        self.qty = qty
        self.order_type = "domestic"
        self.tax = 0.08

        if qty>100:
            raise TooManyMelonsError 

class GovernmentMelonOrder(AbstractMelonOrder):
    """ Create a government melon order class """

    def __init__(self):
        self.tax = 0
        self.passed_inspection = False
    
    def mark_inspection(self, passed):
        """ Marks that melon has passed inspection """
        
        if passed == True:
            self.passed_inspection == True


# create a class that shows the error
# trigger a message ("No more than 100 melons")

# in the InternationalMelonOrder and domestic one, add if qty>100, raise TooManyMelonsError 

class TooManyMelonsError(ValueError):
    """" calling out the order with more than 100 order quantity"""

    def __init__(self):

        super().__init__('No more than 100 melons')
    