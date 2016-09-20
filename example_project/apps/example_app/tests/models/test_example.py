from django.core.exceptions import ValidationError
from django.test import TestCase

from example_project.apps.example_app.models import Example


class ExampleTestCase(TestCase):
    """
    An example of model testing
    """

    def test_nominal_example(self):
        Example(name='My example name').save()

    def test_fail_validation(self):
        with self.assertRaises(ValidationError) as ex:
            Example(name='').save()
        self.assertEqual(ex.exception.error_dict['name'][0].message, 'This field cannot be blank.')

    def test_fail_duplicate(self):
        """
        Also notice how these have a clean database to work with.
        """
        e = Example(name='My example name')
        e.save()

        with self.assertRaises(ValidationError):
            Example(name='My example name').save()
