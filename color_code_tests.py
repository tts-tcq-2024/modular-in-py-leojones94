import pair_number_from_color_test
import color_from_pair_number_test

def color_pair_number_tests():
  color_from_pair_number_test.test_number_to_pair(4, 'White', 'Brown')
  color_from_pair_number_test.test_number_to_pair(5, 'White', 'Slate')
  pair_number_from_color_test.test_pair_to_number('Black', 'Orange', 12)
  pair_number_from_color_test.test_pair_to_number('Violet', 'Slate', 25)
  pair_number_from_color_test.test_pair_to_number('Red', 'Orange', 7)
