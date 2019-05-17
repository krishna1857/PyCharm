import os
import sys
import time
import pytest

sys.path.append(os.getcwd())
sys.path.insert(0, "C:/Users/kdandotiya/PycharmProjects/PyTrainingProject1/src/")
from testsuites.BASIC import basic1
from config import Constants
from testdata import data
from testutils import mailer


def test_basic():
    res = basic1.add(data.num1, data.num2)
    time.sleep(Constants.SLEEP_TIME)
    print("Test Sleeping for " + str(Constants.SLEEP_TIME)+ "sec")
    print("Running test_basic")
    assert res == 5, "Test Failed"


if __name__  == "__main__":
    test_basic()
    mailer.send_mail("krishnadandotiya00@gmail.com", "krishnadandotiya14@gmail.com", data.testModule+"_Result", "TestBasic", files="C:/Users/kdandotiya/PycharmProjects/PyTrainingProject1/src/reports/report.html")




