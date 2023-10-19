import unittest

from exceptions.argument_error import ArgumentMismatchError
from exceptions.dimensional_error import DimensionalMismatchError
from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.sphere import Sphere

"""
coverage report -m
########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
"""


class TestCircle(unittest.TestCase):
    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    def test_circle_area(self):
        c = Circle(2, 0, 0)
        self.assertAlmostEqual(c.area, 12.57, places=2)

    def test_circle_circumference(self):
        c = Circle(3, 0, 0)
        self.assertAlmostEqual(c.circumference, 18.85, places=2)

    def test_circle_is_unit_circle(self):
        c = Circle(1, 0, 0)
        self.assertTrue(c.is_unit_circle())

    def test_circle_is_not_unit_circle_by_radius(self):
        c = Circle(2, 0, 0)
        self.assertFalse(c.is_unit_circle())

    def test_circle_is_not_unit_circle_by_position(self):
        c1 = Circle(1, 1, 0)
        self.assertFalse(c1.is_unit_circle())

        c2 = Circle(1, 0, 1)
        self.assertFalse(c2.is_unit_circle())

        c3 = Circle(1, 13, 37)
        self.assertFalse(c3.is_unit_circle())

    def test_circle_x_and_y_change_after_translate(self):
        c = Circle(1, 0, 0)
        self.assertEqual(c.x, 0)
        self.assertEqual(c.y, 0)

        c.translate(13, 37)

        self.assertEqual(c.x, 13)
        self.assertEqual(c.y, 37)

        c.translate(13, 37)

        self.assertNotEqual(c.x, 13)
        self.assertNotEqual(c.y, 37)

        self.assertEqual(c.x, 26)
        self.assertEqual(c.y, 74)

    def test_circle_radius_changes_after_resize(self):
        c = Circle(1, 0, 0)
        self.assertEqual(c.radius, 1)

        c.resize(2)

        self.assertEqual(c.radius, 2)

    def test_point_is_inside_with_both_values_inside(self):
        c = Circle(1, 0, 0)
        self.assertTrue(c.is_inside(0.2, 0.2))

    def test_point_is_outside_with_both_values_outside(self):
        c = Circle(1, 0, 0)
        self.assertFalse(c.is_inside(3, 3))

    def test_point_is_outside_with_x_value_outside(self):
        c = Circle(1, 0, 0)
        self.assertFalse(c.is_inside(3, 0.2))

    def test_point_is_outside_with_y_value_outside(self):
        c = Circle(1, 0, 0)
        self.assertFalse(c.is_inside(0.2, 3))

    def test_point_is_outside_on_the_edge_with_both_values_non_zero_(self):
        """Test the point at (cos(45°), sin(45°)), which is on the edge of the circle."""
        from math import cos, sin, sqrt

        c = Circle(3, 0, 0)

        x = -cos(1 / sqrt(2)) * c.radius
        y = sin(1 / sqrt(2)) * c.radius

        # 0.000000000000001 (14 zeros after the decimal point)
        very_small_number = 1.0e-15

        self.assertTrue(sqrt(x**2 + y**2) == c.radius)

        self.assertFalse(sqrt(x**2 + y**2) + very_small_number == c.radius)

        # Should count as outside on the edge
        self.assertFalse(c.is_inside(x, y))

        # Take a veeerrry small step towards the center of the circle and check if it's now inside
        self.assertTrue(c.is_inside(x + very_small_number, y))
        self.assertTrue(c.is_inside(x, y - very_small_number))
        self.assertTrue(c.is_inside(x + very_small_number, y - very_small_number))

    def test_point_is_outside_with_x_value_on_the_edge(self):
        c = Circle(1, 0, 0)
        self.assertFalse(c.is_inside(1, 0))

    def test_point_is_outside_with_y_value_on_the_edge(self):
        c = Circle(1, 0, 0)
        self.assertFalse(c.is_inside(0, 1))

    def test_point_is_outside_after_translation(self):
        c = Circle(1, 0, 0)

        self.assertTrue(c.is_inside(0.2, 0.2))

        c.translate(-4, -4)

        self.assertFalse(c.is_inside(0.2, 0.2))

    def test_circles_are_equal_if_they_have_the_same_area(self):
        c1 = Circle(1, 13, 37)
        c2 = Circle(1, -999, 1234)
        self.assertEqual(c1, c2)

    def test_circles_is_less_than_other_circle_by_comparing_areas(self):
        c1 = Circle(0.3, 0, 0)
        c2 = Circle(1, 0, 0)
        self.assertTrue(c1 < c2)

    def test_all_comparisons_with_two_circles_that_are_of_different_sizes(self):
        c1 = Circle(0.3, 0, 0)
        c2 = Circle(1, 0, 0)

        self.assertFalse(c1 == c2)
        self.assertTrue(c1 != c2)

        self.assertTrue(c1 < c2)
        self.assertTrue(c1 <= c2)

        self.assertFalse(c1 > c2)
        self.assertFalse(c1 >= c2)

    def test_all_comparisons_with_two_circles_that_are_of_equal_sizes(self):
        c1 = Circle(1, 0, 0)
        c2 = Circle(1, 0, 0)

        self.assertTrue(c1 == c2)
        self.assertFalse(c1 != c2)

        self.assertFalse(c1 < c2)
        self.assertTrue(c1 <= c2)

        self.assertFalse(c1 > c2)
        self.assertTrue(c1 >= c2)

    def test_raises_TypeError_on_invalid_argument_types_in_Circle_constructor(self):
        self.assertRaises(TypeError, Circle, "1", 0, 1)
        self.assertRaises(TypeError, Circle, 1, "0", 1)
        self.assertRaises(TypeError, Circle, 1, 0, "1")

    def test_raises_TypeError_on_invalid_argument_types_in_Circle_is_inside(self):
        c = Circle(1, 0, 0)
        self.assertRaises(TypeError, c.is_inside, "1", 0)
        self.assertRaises(TypeError, c.is_inside, 1, "0")

    def test_raises_TypeError_on_invalid_argument_type_in_Circle_resize(self):
        c = Circle(1, 0, 0)
        self.assertRaises(TypeError, c.resize, "0")

    def test_raises_TypeError_on_invalid_argument_types_in_Circle_translate(self):
        c = Circle(1, 0, 0)
        self.assertRaises(TypeError, c.translate, "1", 0)
        self.assertRaises(TypeError, c.translate, 1, "0")

    def test_Circle_does_not_raise_DimensionalMismatchError_on_comparison_with_other_2D_shapes(
        self,
    ):
        circle = Circle(1, 0, 0)
        rectangle = Rectangle(1, 0, 1, 1)

        circle == rectangle
        circle != rectangle

        circle < rectangle
        circle <= rectangle

        circle > rectangle
        circle >= rectangle

        # No Exception raised means they are comparable (No DimensionalMismatchError raised)

    def test_Circle_raises_DimensionalMismatchError_on_comparison_with_shapes_of_other_dimensions(
        self,
    ):
        circle = Circle(1, 0, 0)
        sphere = Sphere(0, 1, 2, 0.5)

        self.assertRaises(DimensionalMismatchError, circle.__eq__, sphere)
        self.assertRaises(DimensionalMismatchError, circle.__ne__, sphere)

        self.assertRaises(DimensionalMismatchError, circle.__lt__, sphere)
        self.assertRaises(DimensionalMismatchError, circle.__le__, sphere)

        self.assertRaises(DimensionalMismatchError, circle.__gt__, sphere)
        self.assertRaises(DimensionalMismatchError, circle.__ge__, sphere)

    def test_Circle_raises_ArgumentMismatchError_on_wrong_number_of_arguments_in_translate_inheritence(
        self,
    ):
        c = Circle(1, 0, 0)

        # Raises if it's not exactly 2
        self.assertRaises(ArgumentMismatchError, c.translate, 0)
        self.assertRaises(ArgumentMismatchError, c.translate, 0, 0, 0)


if __name__ == "__main__":
    unittest.main()
