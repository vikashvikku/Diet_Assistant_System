""" pytest """
# import pytest


from diet_assistant import calorie


def testcase1():
    """ testcase 1 """
    assert calorie(50, 60) == 752.4


def testcase2():
    """ testcase 2 """
    assert calorie(55, 35) == 615.6


def testcase3():
    """ testcase 3 """
    assert calorie(85, 21) == 725.04
