import pytest
import datetime
from ohce import Ohce

# Morning tests
def test_greeting_morning():
    ohce = Ohce("Diego", datetime.datetime(2025, 3, 28, 9, 0, 0))
    assert ohce.greet() == "¡Buenos días Diego!"

def test_greeting_morning_edge1():
    ohce = Ohce("Diego", datetime.datetime(2025, 3, 28, 6, 0, 0))
    assert ohce.greet() == "¡Buenos días Diego!"

def test_greeting_morning_edge2():
    ohce = Ohce("Diego", datetime.datetime(2025, 3, 28, 11, 59, 0))
    assert ohce.greet() == "¡Buenos días Diego!"


# Afternoon tests
def test_greeting_afternoon():
    ohce = Ohce("Diego", datetime.datetime(2025, 3, 28, 15, 0, 0))
    assert ohce.greet() == "¡Buenas tardes Diego!"

def test_greeting_afternoon_edge1():
    ohce = Ohce("Diego", datetime.datetime(2025, 3, 28, 12, 0, 0))
    assert ohce.greet() == "¡Buenas tardes Diego!"