import pytest
from account import *

def test_init():
    assert Account.get_name() == "Family Trust" 
    assert Account.get_balance() == 10  
    assert Account.get_balance() == -10 
    assert Account.get_balance() == -10.5  
    
def test_deposit(): 
    Account.getbalance(10)
    assert Account.get_balance() == 10  
    assert Account.get_balance() == -10 
    assert Account.get_balance() == -10.5  
      
  
def test_withdraw():
    assert Account.get_name() == "Family Trust"
    Account.deposit(10)
    Account.withdraw(5)
    assert Account.getbalance() == 5 
    
