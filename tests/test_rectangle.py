import unittest

from exceptions.argument_error import ArgumentMismatchError
from exceptions.dimensional_error import DimensionalMismatchError
from shapes.circle import Circle
from shapes.cube import Cube
from shapes.rectangle import Rectangle

"""
coverage report -m
########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
"""


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    def test_rectangle_area(self):
        r = Rectangle(0, 0, 2, 3)
        self.assertEqual(r.area, 6)

    def test_rectangle_perimeter(self):
        r = Rectangle(0, 0, 2, 3)
        self.assertEqual(r.perimeter, 10)

    def test_rectangle_is_square(self):
        r = Rectangle(0, 0, 3, 3)
        self.assertTrue(r.is_square())

    def test_rectangle_is_not_square_by_sides(self):
        r = Rectangle(0, 0, 2, 3)
        self.assertFalse(r.is_square())

        r2 = Rectangle(0, 0, 3, 2)
        self.assertFalse(r2.is_square())

    def test_rectangle_x_and_y_change_after_translate(self):
        r = Rectangle(0, 0, 1, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        r.translate(13, 37)

        self.assertEqual(r.x, 13)
        self.assertEqual(r.y, 37)

        r.translate(13, 37)

        self.assertNotEqual(r.x, 13)
        self.assertNotEqual(r.y, 37)

        self.assertEqual(r.x, 26)
        self.assertEqual(r.y, 74)

    def test_rectangle_sides_changes_after_resize(self):
        r = Rectangle(0, 0, 1, 1)
        self.assertEqual(r.side1, 1)
        self.assertEqual(r.side2, 1)

        r.resize(13, 37)

        self.assertEqual(r.side1, 13)
        self.assertEqual(r.side2, 37)

        r.resize(15, 15)

        self.assertEqual(r.side1, 15)
        self.assertEqual(r.side2, 15)

        self.assertNotEqual(r.side1, 28)
        self.assertNotEqual(r.side2, 52)

    def test_point_is_inside_with_both_values_inside(self):
        r = Rectangle(0, 0, 2, 2)
        self.assertTrue(r.is_inside(0.2, 0.2))

    def test_point_is_outside_with_both_values_outside(self):
        r = Rectangle(0, 0, 2, 2)
        self.assertFalse(r.is_inside(3, 3))

    def test_point_is_outside_with_x_value_outside(self):
        r = Rectangle(0, 0, 2, 2)
        self.assertFalse(r.is_inside(3, 0.2))

    def test_point_is_outside_with_y_value_outside(self):
        r = Rectangle(0, 0, 2, 2)
        self.assertFalse(r.is_inside(0.2, 3))

    def test_point_is_outside_with_x_value_on_the_edge(self):
        r = Rectangle(0, 0, 2, 2)
        self.assertFalse(r.is_inside(1, 0))

    def test_point_is_outside_with_y_value_on_the_edge(self):
        r = Rectangle(0, 0, 2, 2)
        self.assertFalse(r.is_inside(0, 1))

    def test_point_is_outside_with_both_values_on_the_edge(self):
        r = Rectangle(0, 0, 2, 2)
        self.assertFalse(r.is_inside(1, 1))

    def test_point_is_outside_after_translation(self):
        r = Rectangle(0, 0, 2, 1)

        self.assertTrue(r.is_inside(0.2, 0.2))

        r.translate(-4, -4)

        self.assertFalse(r.is_inside(0.2, 0.2))

    def test_rectangles_are_equal_if_they_have_the_same_area(self):
        c1 = Rectangle(13, 37, 1, 1)
        c2 = Rectangle(-999, 1234, 1, 1)
        self.assertEqual(c1, c2)

    def test_rectangles_is_less_than_other_rectangle_by_comparing_areas(self):
        c1 = Rectangle(0, 0, 0.3, 0.3)
        c2 = Rectangle(0, 0, 1, 1)
        self.assertTrue(c1 < c2)

    def test_all_comparisons_with_two_rectangles_that_are_of_different_areas(self):
        c1 = Rectangle(0, 0, 0.3, 0.3)
        c2 = Rectangle(0, 0, 1, 1)

        self.assertFalse(c1 == c2)
        self.assertTrue(c1 != c2)

        self.assertTrue(c1 < c2)
        self.assertTrue(c1 <= c2)

        self.assertFalse(c1 > c2)
        self.assertFalse(c1 >= c2)

    def test_all_comparisons_with_two_rectangles_that_are_of_equal_areas(self):
        c1 = Rectangle(1, 0, 1, 1)
        c2 = Rectangle(0, 1, 2, 0.5)

        self.assertTrue(c1 == c2)
        self.assertFalse(c1 != c2)

        self.assertFalse(c1 < c2)
        self.assertTrue(c1 <= c2)

        self.assertFalse(c1 > c2)
        self.assertTrue(c1 >= c2)

    def test_raises_TypeError_on_invalid_argument_types_in_Rectangle_constructor(self):
        self.assertRaises(TypeError, Rectangle, "1", 0, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, "0", 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 0, "1", 1)
        self.assertRaises(TypeError, Rectangle, 1, 0, 1, "1")

    def test_raises_TypeError_on_invalid_argument_types_in_Rectangle_is_inside(self):
        r = Rectangle(0, 0, 1, 1)
        self.assertRaises(TypeError, r.is_inside, "1", 0)
        self.assertRaises(TypeError, r.is_inside, 1, "0")

    def test_raises_TypeError_on_invalid_argument_type_in_Rectangle_resize(self):
        r = Rectangle(0, 0, 1, 1)
        self.assertRaises(TypeError, r.resize, "0", 1)
        self.assertRaises(TypeError, r.resize, 0, "1")

    def test_raises_TypeError_on_invalid_argument_types_in_Rectangle_translate(self):
        r = Rectangle(0, 0, 1, 1)
        self.assertRaises(TypeError, r.translate, "1", 0)
        self.assertRaises(TypeError, r.translate, 1, "0")

    def test_Rectangle_does_not_raise_DimensionalMismatchError_on_comparison_with_other_2D_shapes(
        self,
    ):
        rectangle = Rectangle(1, 0, 1, 1)
        circle = Circle(1, 0, 0)

        rectangle == circle
        rectangle != circle

        rectangle < circle
        rectangle <= circle

        rectangle > circle
        rectangle >= circle

        # No Exception raised means they are comparable (No DimensionalMismatchError raised)

    def test_Rectangle_raises_DimensionalMismatchError_on_comparison_with_shapes_of_other_dimensions(
        self,
    ):
        rectangle = Rectangle(1, 0, 1, 1)
        cube = Cube(0, 1, 2, 0.5)

        self.assertRaises(DimensionalMismatchError, rectangle.__eq__, cube)
        self.assertRaises(DimensionalMismatchError, rectangle.__ne__, cube)

        self.assertRaises(DimensionalMismatchError, rectangle.__lt__, cube)
        self.assertRaises(DimensionalMismatchError, rectangle.__le__, cube)

        self.assertRaises(DimensionalMismatchError, rectangle.__gt__, cube)
        self.assertRaises(DimensionalMismatchError, rectangle.__ge__, cube)

    def test_Rectangle_raises_ArgumentMismatchError_on_wrong_number_of_arguments_in_translate_inheritence(
        self,
    ):
        r = Rectangle(0, 0, 1, 1)

        # Raises if it's not exactly 2
        self.assertRaises(ArgumentMismatchError, r.translate, 0)
        self.assertRaises(ArgumentMismatchError, r.translate, 0, 0, 0)


if __name__ == "__main__":
    unittest.main()
