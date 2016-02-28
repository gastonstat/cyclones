""" Tests function counting_cyclones_per_season()
Run the test with:
    nosetests test_counting_cyclones_per_season.py
"""

# Loading modules.
import os
import sys
from nose.tools import assert_equal


# Add path to functions to the system path.
sys.path.append(os.path.join(os.path.dirname(__file__), "../functions/"))



# test
def test_counting_cyclones_per_season():
    input_seasons = ['Fall', 'Summer', 'Winter', 'Spring', 'Fall', 'Spring']
    input_counts = [10, 20, 15, 5, 5, 30]
    output_dict = {'Fall': 15, 'Spring': 35, 'Summer': 20, 'Winter': 15}
    # apply counting_cyclones_per_season
    test_dict = counting_cyclones_per_season(input_seasons, input_counts)
    #assert test_dict == output_dict
    assert_equal(test_dict == output_dict)
