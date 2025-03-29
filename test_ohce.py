import pytest
import datetime
from ohce import Ohce

def test_greeting_morning():
    ohce = Ohce("Diego", datetime.datetime(2025, 3, 28, 9, 0, 0))
    assert ohce.greet() == "¡Buenos días Diego!"
