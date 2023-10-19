import unittest

from exceptions.argument_error import ArgumentMismatchError
from exceptions.dimensional_error import DimensionalMismatchError
from shapes.circle import Circle
from shapes.cube import Cube
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


class TestCube(unittest.TestCase):
    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    def test_cube_volume(self):
        c = Cube(2, 1, 2, 3)
        self.assertEqual(c.volume, 8)

    def test_cube_surface_area(self):
        c = Cube(2, 0, 2, 3)
        self.assertEqual(c.surface_area, 24)

    def test_cube_x_and_y_change_after_translate(self):
        c = Cube(1, 0, 0, 0)
        self.assertEqual(c.x, 0)
        self.assertEqual(c.y, 0)
        self.assertEqual(c.z, 0)

        c.translate(13, 33, 37)

        self.assertEqual(c.x, 13)
        self.assertEqual(c.y, 33)
        self.assertEqual(c.z, 37)

        c.translate(13, 33, 37)

        self.assertNotEqual(c.x, 13)
        self.assertNotEqual(c.y, 33)
        self.assertNotEqual(c.z, 37)

        self.assertEqual(c.x, 26)
        self.assertEqual(c.y, 66)
        self.assertEqual(c.z, 74)

    def test_cube_sides_changes_after_resize(self):
        c = Cube(1, 0, 0, 0)

        self.assertEqual(c.side, 1)

        c.resize(1337)

        self.assertEqual(c.side, 1337)

        c.resize(1337)

        self.assertEqual(c.side, 1337)
        self.assertNotEqual(c.side, 2674)

    def test_point_is_inside_with_all_values_inside(self):
        c = Cube(2, 0, 0, 0)
        self.assertTrue(c.is_inside(0.2, 0.2, 0.2))

    def test_point_is_outside_with_all_values_on_the_edge(self):
        c = Cube(2, 0, 0, 0)
        self.assertFalse(c.is_inside(1, 1, 1))

    def test_point_is_outside_with_x_value_outside(self):
        c = Cube(2, 0, 0, 0)
        self.assertFalse(c.is_inside(3, 0.2, 0.2))

    def test_point_is_outside_with_y_value_outside(self):
        c = Cube(2, 0, 0, 0)
        self.assertFalse(c.is_inside(0.2, 3, 0.2))

    def test_point_is_outside_with_z_value_outside(self):
        c = Cube(2, 0, 0, 0)
        self.assertFalse(c.is_inside(0.2, 0.2, 3))

    def test_point_is_outside_with_x_value_on_the_edge(self):
        c = Cube(2, 0, 0, 0)
        self.assertFalse(c.is_inside(1, 0, 0))

    def test_point_is_outside_with_y_value_on_the_edge(self):
        c = Cube(2, 0, 0, 0)
        self.assertFalse(c.is_inside(0, 1, 0))

    def test_point_is_outside_with_z_value_on_the_edge(self):
        c = Cube(2, 0, 0, 0)
        self.assertFalse(c.is_inside(0, 0, 1))

    def test_point_is_outside_after_translation(self):
        c = Cube(2, 0, 0, 0)

        self.assertTrue(c.is_inside(0.2, 0.2, 0.2))

        c.translate(-4, -4, -4)

        self.assertFalse(c.is_inside(0.2, 0.2, 0.2))

    def test_cubes_are_equal_if_they_have_the_same_volume(self):
        c1 = Cube(13, 37, 1, 1)
        c2 = Cube(13, 1234, 1, 0)
        self.assertEqual(c1, c2)

    def test_cubes_is_less_than_other_cube_by_comparing_volumes(self):
        c1 = Cube(0.3, 0, 0, 0)
        c2 = Cube(1, 0, 0, 0)
        self.assertTrue(c1 < c2)

    def test_all_comparisons_with_two_cubes_that_are_of_different_volumes(self):
        c1 = Cube(0.3, 0, 0, 0)
        c2 = Cube(1, 0, 0, 0)

        self.assertFalse(c1 == c2)
        self.assertTrue(c1 != c2)

        self.assertTrue(c1 < c2)
        self.assertTrue(c1 <= c2)

        self.assertFalse(c1 > c2)
        self.assertFalse(c1 >= c2)

    def test_all_comparisons_with_two_cubes_that_are_of_equal_volumes(self):
        c1 = Cube(1, 2, 5, 8)
        c2 = Cube(1, 1, 2, 3)

        self.assertTrue(c1 == c2)
        self.assertFalse(c1 != c2)

        self.assertFalse(c1 < c2)
        self.assertTrue(c1 <= c2)

        self.assertFalse(c1 > c2)
        self.assertTrue(c1 >= c2)

    def test_raises_TypeError_on_invalid_argument_types_in_Cube_constructor(self):
        self.assertRaises(TypeError, Cube, "1", 0, 1, 1)
        self.assertRaises(TypeError, Cube, 1, "0", 1, 1)
        self.assertRaises(TypeError, Cube, 1, 0, "1", 1)
        self.assertRaises(TypeError, Cube, 1, 0, 1, "1")

    def test_raises_TypeError_on_invalid_argument_types_in_Cube_is_inside(self):
        c = Cube(1, 0, 0, 0)
        self.assertRaises(TypeError, c.is_inside, "1", 0, 0)
        self.assertRaises(TypeError, c.is_inside, 1, "0", 0)
        self.assertRaises(TypeError, c.is_inside, 1, 0, "0")

    def test_raises_TypeError_on_invalid_argument_type_in_Cube_resize(self):
        c = Cube(1, 0, 0, 0)
        self.assertRaises(TypeError, c.resize, "0")

    def test_raises_TypeError_on_invalid_argument_types_in_Cube_translate(self):
        c = Cube(1, 0, 0, 0)
        self.assertRaises(TypeError, c.translate, "1", 0, 0)
        self.assertRaises(TypeError, c.translate, 1, "0", 0)
        self.assertRaises(TypeError, c.translate, 1, 0, "0")

    def test_Cube_does_not_raise_DimensionalMismatchError_on_comparison_with_other_3D_shapes(
        self,
    ):
        cube = Cube(1, 0, 0, 0)
        sphere = Sphere(1, 0, 0, 0)

        cube == sphere
        cube != sphere

        cube < sphere
        cube <= sphere

        cube > sphere
        cube >= sphere

        # No Exception raised means they are comparable (No DimensionalMismatchError raised)

    def test_Cube_raises_DimensionalMismatchError_on_comparison_with_shapes_of_other_dimensions(
        self,
    ):
        cube = Cube(1, 0, 1, 1)
        circle = Circle(0, 1, 2)

        self.assertRaises(DimensionalMismatchError, cube.__eq__, circle)
        self.assertRaises(DimensionalMismatchError, cube.__ne__, circle)

        self.assertRaises(DimensionalMismatchError, cube.__lt__, circle)
        self.assertRaises(DimensionalMismatchError, cube.__le__, circle)

        self.assertRaises(DimensionalMismatchError, cube.__gt__, circle)
        self.assertRaises(DimensionalMismatchError, cube.__ge__, circle)

    def test_Cube_raises_ArgumentMismatchError_on_wrong_number_of_arguments_in_translate_inheritence(
        self,
    ):
        c = Cube(1, 0, 0, 0)

        # Raises if it's not exactly 3
        self.assertRaises(ArgumentMismatchError, c.translate, 0)
        self.assertRaises(ArgumentMismatchError, c.translate, 0, 0)
        self.assertRaises(ArgumentMismatchError, c.translate, 0, 0, 0, 0)


if __name__ == "__main__":
    unittest.main()
