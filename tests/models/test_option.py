import unittest
from datetime import date

from tastyworks.models.option import Option, OptionType, OptionUnderlyingType


class TestOptionModel(unittest.TestCase):
    def setUp(self):
        self.test_option = Option(
            ticker='AKS',
            quantity=1,
            expiry=date(2018, 8, 10),
            strike=3.5,
            option_type=OptionType.CALL,
            underlying_type=OptionUnderlyingType.EQUITY
        )

    def test_occ2010_integer_strike(self):
        self.test_option.strike = 3
        expected_result = 'AKS   180810C00003000'

        res = self.test_option.get_occ2010_symbol()
        self.assertEqual(expected_result, res)

    def test_occ2010_fraction_strike(self):
        self.test_option.strike = 3.45
        expected_result = 'AKS   180810C00003450'

        res = self.test_option.get_occ2010_symbol()
        self.assertEqual(expected_result, res)

        self.test_option.strike = 3.5
        expected_result = 'AKS   180810C00003500'

        res = self.test_option.get_occ2010_symbol()
        self.assertEqual(expected_result, res)

    def test_occ2010_ticker_padding(self):
        self.test_option.ticker = 'BOB123'
        expected_result = 'BOB123180810C00003500'

        res = self.test_option.get_occ2010_symbol()
        self.assertEqual(expected_result, res)

        self.test_option.ticker = 'BOB'
        expected_result = 'BOB   180810C00003500'

        res = self.test_option.get_occ2010_symbol()
        self.assertEqual(expected_result, res)

    def test_occ2010_ticker_trimming(self):
        self.test_option.ticker = 'BOB123456'
        expected_result = 'BOB123180810C00003500'

        res = self.test_option.get_occ2010_symbol()
        self.assertEqual(expected_result, res)
