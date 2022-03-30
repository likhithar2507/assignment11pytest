import program_1
import pytest

@pytest.mark.xfail
@pytest.mark.parametrize("x,result",[(153,True),(371,True),(300,True),(407,False)])
def test_armstrong(x,result):
    armstrong=program_1.armstrong(x)
    assert armstrong == result

@pytest.mark.skip(reason="no need")
@pytest.mark.parametrize("x,result",[(15,True),(80,True),(40,True),(48,False)])
def test_Divisible_or_not(x,result):
    divisible=program_1.Divisible_or_not(x)
    assert divisible == result

@pytest.mark.xfail
@pytest.mark.parametrize("x,y,z,result",[(2,3,4,2),(12,1,23,12)])
def test_Smallest_of_threenum(x,y,z,result):
    smallest=program_1.Smallest_of_threenum(x,y,z)
    assert smallest == result

@pytest.mark.xfail
@pytest.mark.parametrize("x,result",[(4,"even"),(3,"odd"),(45,"even")])
def test_check_even_odd(x,result):
    oddeven=program_1.check_even_odd(x)
    assert oddeven == result

@pytest.mark.xfail
@pytest.mark.parametrize("my_str,result",[("wow",True),("hi",False),("good",True)])
def test_palindrome(my_str,result):
    palindrome=program_1.palindrome(my_str)
    assert palindrome == result

