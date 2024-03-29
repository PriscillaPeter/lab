class Account:
  
  def __init__(self, name: str):
      self.__account_name = name  
      self.__account_balance = 0
  
  def deposit(self, amount: float)->bool:
    if amount > 0:  
      self.__account_balance = self.__account_balance + amount       
      return True
    else: 
      return False
        
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
    return self.__account_balance 
    
  def get_name(self):
    return self.__account_name  
