""" Tests function naming_seasons()
Run the test with:
    nosetests test_naming_seasons.py
"""

# Loading modules.
import os
import sys
from nose.tools import assert_equal


# Add path to functions to the system path.
sys.path.append(os.path.join(os.path.dirname(__file__), "../functions/"))


def test_naming_seasons():
	# create test data
    input_values = ['1', '4', '2', '1', '3']
    output_values = ['Fall', 'Summer', 'Winter', 'Fall', 'Spring']
    # apply naming_seasons
    test_values = naming_seasons(input_values)
    #assert test_values == output_values
    assert_equal(test_values == output_values)
