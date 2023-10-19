import unittest

from exceptions.argument_error import ArgumentMismatchError
from exceptions.dimensional_error import DimensionalMismatchError
from shapes.circle import Circle
from shapes.cube import Cube
from shapes.rectangle import Rectangle
from shapes.sphere import Sphere


class TestSphere(unittest.TestCase):
    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    def test_sphere_volume(self):
        s = Sphere(2, 0, 0, 0)
        self.assertAlmostEqual(s.volume, 33.51, places=2)

    def test_sphere_surface_area(self):
        s = Sphere(3, 0, 0, 0)
        self.assertAlmostEqual(s.surface_area, 113.1, places=2)

    def test_sphere_is_unit_sphere(self):
        s = Sphere(1, 0, 0, 0)
        self.assertTrue(s.is_unit_sphere())

    def test_sphere_is_not_unit_sphere_by_radius(self):
        s = Sphere(2, 0, 0, 0)
        self.assertFalse(s.is_unit_sphere())

    def test_sphere_is_not_unit_sphere_by_position(self):
        c1 = Sphere(1, 1, 0, 0)
        self.assertFalse(c1.is_unit_sphere())

        c2 = Sphere(1, 0, 1, 0)
        self.assertFalse(c2.is_unit_sphere())

        c3 = Sphere(1, 0, 0, 1)
        self.assertFalse(c3.is_unit_sphere())

    def test_sphere_x_and_y_change_after_translate(self):
        s = Sphere(1, 0, 0, 0)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.z, 0)

        s.translate(13, 33, 37)

        self.assertEqual(s.x, 13)
        self.assertEqual(s.y, 33)
        self.assertEqual(s.z, 37)

        s.translate(13, 33, 37)

        self.assertNotEqual(s.x, 13)
        self.assertNotEqual(s.y, 33)
        self.assertNotEqual(s.z, 37)

        self.assertEqual(s.x, 26)
        self.assertEqual(s.y, 66)
        self.assertEqual(s.z, 74)

    def test_sphere_radius_changes_after_resize(self):
        s = Sphere(1, 0, 0, 0)
        self.assertEqual(s.radius, 1)

        s.resize(2)

        self.assertEqual(s.radius, 2)

    def test_point_is_inside_with_all_values_inside(self):
        s = Sphere(1, 0, 0, 0)
        self.assertTrue(s.is_inside(0.2, 0.2, 0.2))

    def test_point_is_outside_with_all_values_outside(self):
        s = Sphere(1, 0, 0, 0)
        self.assertFalse(s.is_inside(3, 3, 3))

    def test_point_is_outside_with_x_value_outside(self):
        s = Sphere(1, 0, 0, 0)
        self.assertFalse(s.is_inside(3, 0.2, 0.2))

    def test_point_is_outside_with_y_value_outside(self):
        s = Sphere(1, 0, 0, 0)
        self.assertFalse(s.is_inside(0.2, 3, 0.2))

    def test_point_is_outside_with_z_value_outside(self):
        s = Sphere(1, 0, 0, 0)
        self.assertFalse(s.is_inside(0.2, 0.2, 3))

    def test_point_is_outside_on_the_edge_with_both_values_non_zero_(self):
        """For more info on how to choose x, y and z:
        https://stackoverflow.com/questions/969798/plotting-a-point-on-the-edge-of-a-sphere/50086913#50086913
        """
        from math import acos, atan2, cos, sin, sqrt

        s = Sphere(3, 0, 0, 0)

        x = sin(1 / sqrt(2))
        y = -sin(1 / sqrt(2))
        z = sin(1 / sqrt(2))

        self.assertNotEqual(x, 0)
        self.assertNotEqual(y, 0)
        self.assertNotEqual(z, 0)

        phi = atan2(y, x)
        theta = acos((z / s.radius))

        x = s.radius * sin(theta) * cos(phi)
        y = s.radius * sin(theta) * sin(phi)
        z = s.radius * cos(theta)

        self.assertNotEqual(x, 0)
        self.assertNotEqual(y, 0)
        self.assertNotEqual(z, 0)

        # 0.000000000000001 (14 zeros after the decimal point)
        very_small_number = 1.0e-15

        self.assertTrue(sqrt(x**2 + y**2 + z**2) == s.radius)

        self.assertFalse(sqrt(x**2 + y**2 + z**2) + very_small_number == s.radius)

        # Should count as outside on the edge
        self.assertFalse(s.is_inside(x, y, z))

        # Take a veeerrry small step towards the center of the sphere and check if it's now inside
        self.assertTrue(s.is_inside(x - very_small_number, y, z))
        self.assertTrue(s.is_inside(x, y + very_small_number, z))
        self.assertTrue(s.is_inside(x, y, z - very_small_number))

    def test_point_is_outside_with_x_value_on_the_edge(self):
        s = Sphere(1, 0, 0, 0)
        self.assertFalse(s.is_inside(1, 0, 0))

    def test_point_is_outside_with_y_value_on_the_edge(self):
        s = Sphere(1, 0, 0, 0)
        self.assertFalse(s.is_inside(0, 1, 0))

    def test_point_is_outside_with_z_value_on_the_edge(self):
        s = Sphere(1, 0, 0, 0)
        self.assertFalse(s.is_inside(0, 0, 1))

    def test_point_is_outside_after_translation(self):
        s = Sphere(1, 0, 0, 0)

        self.assertTrue(s.is_inside(0.2, 0.2, 0.2))

        s.translate(-4, -4, -4)

        self.assertFalse(s.is_inside(0.2, 0.2, 0.2))

    def test_spheres_are_equal_if_they_have_the_same_volume(self):
        c1 = Sphere(1, 13, 37, 0)
        c2 = Sphere(1, -999, 1234, 0)
        self.assertEqual(c1, c2)

    def test_spheres_is_less_than_other_sphere_by_comparing_volumes(self):
        c1 = Sphere(0.3, 0, 0, 0)
        c2 = Sphere(1, 0, 0, 0)
        self.assertTrue(c1 < c2)

    def test_all_comparisons_with_two_spheres_that_are_of_different_sizes(self):
        c1 = Sphere(0.3, 0, 0, 0)
        c2 = Sphere(1, 0, 0, 0)

        self.assertFalse(c1 == c2)
        self.assertTrue(c1 != c2)

        self.assertTrue(c1 < c2)
        self.assertTrue(c1 <= c2)

        self.assertFalse(c1 > c2)
        self.assertFalse(c1 >= c2)

    def test_all_comparisons_with_two_spheres_that_are_of_equal_sizes(self):
        c1 = Sphere(1, 0, 0, 0)
        c2 = Sphere(1, 0, 0, 0)

        self.assertTrue(c1 == c2)
        self.assertFalse(c1 != c2)

        self.assertFalse(c1 < c2)
        self.assertTrue(c1 <= c2)

        self.assertFalse(c1 > c2)
        self.assertTrue(c1 >= c2)

    def test_raises_TypeError_on_invalid_argument_types_in_Sphere_constructor(self):
        self.assertRaises(TypeError, Sphere, "1", 0, 1, 1)
        self.assertRaises(TypeError, Sphere, 1, "0", 1, 1)
        self.assertRaises(TypeError, Sphere, 1, 0, "1", 1)
        self.assertRaises(TypeError, Sphere, 1, 0, 1, "1")

    def test_raises_TypeError_on_invalid_argument_types_in_Sphere_is_inside(self):
        s = Sphere(1, 0, 0, 0)
        self.assertRaises(TypeError, s.is_inside, "1", 0, 0)
        self.assertRaises(TypeError, s.is_inside, 1, "0", 0)
        self.assertRaises(TypeError, s.is_inside, 1, 0, "0")

    def test_raises_TypeError_on_invalid_argument_type_in_Sphere_resize(self):
        s = Sphere(1, 0, 0, 0)
        self.assertRaises(TypeError, s.resize, "0")

    def test_raises_TypeError_on_invalid_argument_types_in_Sphere_translate(self):
        s = Sphere(1, 0, 0, 0)
        self.assertRaises(TypeError, s.translate, "1", 0, 0)
        self.assertRaises(TypeError, s.translate, 1, "0", 0)
        self.assertRaises(TypeError, s.translate, 1, 0, "0")

    def test_Sphere_does_not_raise_DimensionalMismatchError_on_comparison_with_other_3D_shapes(
        self,
    ):
        sphere = Sphere(1, 0, 0, 0)
        cube = Cube(1, 0, 1, 1)

        sphere == cube
        sphere != cube

        sphere < cube
        sphere <= cube

        sphere > cube
        sphere >= cube

        # No Exception raised means they are comparable (No DimensionalMismatchError raised)

    def test_Sphere_raises_DimensionalMismatchError_on_comparison_with_shapes_of_other_dimensions(
        self,
    ):
        sphere = Sphere(1, 0, 0, 0)
        circle = Circle(0, 1, 2)

        self.assertRaises(DimensionalMismatchError, sphere.__eq__, circle)
        self.assertRaises(DimensionalMismatchError, sphere.__ne__, circle)

        self.assertRaises(DimensionalMismatchError, sphere.__lt__, circle)
        self.assertRaises(DimensionalMismatchError, sphere.__le__, circle)

        self.assertRaises(DimensionalMismatchError, sphere.__gt__, circle)
        self.assertRaises(DimensionalMismatchError, sphere.__ge__, circle)

    def test_Sphere_raises_ArgumentMismatchError_on_wrong_number_of_arguments_in_translate_inheritence(
        self,
    ):
        s = Sphere(1, 0, 0, 0)

        # Raises if it's not exactly 3
        self.assertRaises(ArgumentMismatchError, s.translate, 0)
        self.assertRaises(ArgumentMismatchError, s.translate, 0, 0)
        self.assertRaises(ArgumentMismatchError, s.translate, 0, 0, 0, 0)


if __name__ == "__main__":
    unittest.main()
