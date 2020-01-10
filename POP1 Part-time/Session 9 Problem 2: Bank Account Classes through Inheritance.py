"""
Assuming that you are starting with this problem after completing the Bank Account Classes problem (which is recommended), you must have noticed that the code in Bank Account Classes is highly redundant (contains large duplications). The purpose of this problem is to refactor that code using inheritance. Complete the implementation of the new classes using the pattern on the right (see lines marked with TD). See below the examples of use and test cases:

john01 = Person("John", "Doe")
john01.set_address("Birkbeck, Malet st., WC1E 7HX")
john01s_account = IndividualBankAccount("12-34-56", "12345678", john01)
#Test1 checks john01s_account.get_account_data()=="John Doe 12-34-56 12345678"
john01s_account.set_sort_code("11-11-11")
#Test2 check john01s_account.get_sort_code()=="11-11-11"
mary01 = Person("Mary", "Ann")
mary01.set_address("UCL, Gower st., WC1E 6BT")
mary01s_account = IndividualBankAccount("65-43-21", "87654321", mary01)
#Test3 checks mary01s_account.get_account_data()=="Mary Ann 65-43-21 87654321"
mary01s_account.set_account_number("99999999")
#Test4 checks mary01s_account.get_account_number()=="99999999"
acc02 = SharedBankAccount("11-22-33", "11223344", [john01, mary01])
#Test5 checks acc02.get_account_data()=="John Doe, Mary Ann, 11-22-33 11223344"
"""
class Person:
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln
        self.address = None 
    def set_address(self, adr):
        self.address = adr 

class BankAccount:
    def __init__(self, sort_code, account_number):
      self.sc = sort_code
      self.an = account_number
    def set_sort_code(self, sort_code):
      self.sc = sort_code
    def get_sort_code(self):
      return self.sc
    def set_account_number(self, account_number):
      self.an = account_number
    def get_account_number(self):
      return self.an
    def get_account_data(self):
      return self.sc + " " + self.an


class IndividualBankAccount(BankAccount):
    def __init__(self, sort_code, account_number, owner):
        super().__init__(sort_code, account_number)
        self.own = owner
    def get_account_data(self):
      return self.own.first_name + " " + self.own.last_name + " " + \
      super().get_account_data()


class SharedBankAccount(BankAccount):
    def __init__(self, sort_code, account_number, owners):
        super().__init__(sort_code, account_number)
        self.owns = owners
    def get_account_data(self):
      dat = ""
      for pers in range(len(self.owns)):
        dat += self.owns[pers].first_name + " " + self.owns[pers].last_name + ", "
      return dat + super().get_account_data()
