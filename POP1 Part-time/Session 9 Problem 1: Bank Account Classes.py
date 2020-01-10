"""
The following class templates handle information about a person and individual and shared (joint) bank accounts. Complete the implementation of the classes using the pattern below (see lines marked with TD). Do not use inheritance to answer this question (this comes in Problem 2)

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
  '''to handle person's details'''
  
  def __init__(self, fn, ln):
    self.first_name = fn
    self.last_name = ln
    self.address = None #addresses stored as strings
    
  def set_address(self, adr):
    self.address = adr #strings

class IndividualBankAccount:
  '''to handle individual bank account data'''
  
  def __init__(self, sort_code, account_number, owner):
    '''TD implement this; creates a bank account
    with sort code as string, account number as string,
    and owner as Person'''
    self.sort_code = sort_code
    self.account_number = account_number
    self.owner = owner
    
  def set_sort_code(self, sort_code):
    '''TD implement this; updates sort code'''
    self.sort_code = sort_code
    
  def get_sort_code(self):
    '''TD implement this; returns sort code'''
    return self.sort_code
    
  def set_account_number(self, account_number):
    '''TD implement this; updates account number'''
    self.account_number = account_number
    
  def get_account_number(self):
    '''TD implement this; returns account number'''
    return self.account_number
    
  def get_account_data(self):
    '''TD implement this; returns string "FN LN SC AN"
    where FN and LN are owner's first and last names,
    SC is sort code, AN is account number'''
    return self.owner.first_name + " " + self.owner.last_name + " " + self.sort_code + " " + self.account_number

class SharedBankAccount:
  '''to handle data of an account that has several owners'''
  
  def __init__(self, sort_code, account_number, owners):
    '''TD implement this; creates a bank account
    with sort code as string, account number as string,
    and owners as a list of Persons'''
    self.sort_code = sort_code
    self.account_number = account_number
    self.owners = owners
    
  def set_sort_code(self, sort_code):
    '''TD implement this; updates sort code'''
    self.sort_code = sort_code
    
  def get_sort_code(self):
    '''TD implement this; returns sort code'''
    return self.sort_code
    
  def set_account_number(self, account_number):
    '''TD implement this; updates account number'''
    self.account_number = account_number
    
  def get_account_number(self):
    '''TD implement this; returns account number'''
    return self.account_number
    
  def get_account_data(self):
    '''TD implement this; returns string
    "FN1 LN1, FN2 LN2, ..., FNM LNM, SC AN"
    where FNi LNi is the i-th owner first and last names,
    SC is sort code, AN is account number'''
    names = ""
    for i in range(len(self.owners)):
      names += str(self.owners[i].first_name) + " " + str(self.owners[i].last_name) + ", "
    return names + self.sort_code + " " + self.account_number
