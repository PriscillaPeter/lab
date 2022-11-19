class Account:
  """ Account class creates deposits and withdrawals and returns account holder name and account balance"""
  def __init__(self, name: str):
    
    #sets default values for account
    self.__account_name = name  
    self.__account_balance = 0
  
  def deposit(self, amount: float)->bool:
    
    #increments account balance by the specified amount.
    if amount > 0:  
      self.__account_balance = self.__account_balance + amount       
      return True
    else: 
      return False
    #decrements account balance by the specified amount.
    
  def withdraw(self, amount: float)-> bool:
    if amount > 0:  
        if amount <= self.__account_balance:  
            self.__account_balance = self.__account_balance - amount   
            return True
        else:
          return False
    else:
      return False
      
  def get_balance(self):
    #returns account value
    return self.__account_balance 
    
  def get_name(self):
    #returns account name
    return self.__account_name  
