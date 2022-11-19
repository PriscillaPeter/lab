import pytest
from account import *

def test_init():
    account_1 = Account('Family Trust')
    assert account_1.get_name() == 'Family Trust' 
    assert account_1.get_balance() == 10  

def test_deposit(): 
    account_1 = Account('Family Trust')
    assert account_1.deposit(-10) is False
    assert account_1.deposit(10)  
    assert account_1.get_balance() == 10  
      
def test_withdraw():
    account_1 = Account('Family Trust')
    assert account_1.get_name() == "Family Trust"
    account_1.deposit(10)
    account_1.withdraw(5)
    assert account_1.getbalance() == 5 
