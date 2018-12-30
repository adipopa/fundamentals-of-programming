from unittest import TestCase

from datetime import date

from utils.helper import Helper


class TestHelper(TestCase):

    def test_resolve_date(self):
        self.assertEqual(Helper.resolve_date("29/11/2018"), date(2018, 11, 29))
        self.assertRaises(ValueError, Helper.resolve_date, "07/17/2018")
        self.assertRaises(ValueError, Helper.resolve_date, "")
