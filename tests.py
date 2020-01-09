import datetime
import unittest

from parsers.bank1 import Bank1Parser
from parsers.bank2 import Bank2Parser
from parsers.bank3 import Bank3Parser


class BankParserTestCase(unittest.TestCase):
    def setUp(self):
        path = "./test_files/{}.csv"
        self.bank1_movements = Bank1Parser(path.format("bank1")).generate_report()
        self.bank2_movements = Bank2Parser(path.format("bank2")).generate_report()
        self.bank3_movements = Bank3Parser(path.format("bank3")).generate_report()

    def test_first_bank(self):
        result = {
            'date': datetime.date(2019, 10, 1), 'transaction_type': 'remove',
            'amount': 99.1, 'from_account': 198, 'to_account': 182
        }
        self.assertEqual(vars(self.bank1_movements[0]), result)

    def test_second_bank(self):
        result = {
            'date': datetime.date(2019, 10, 3), 'transaction_type': 'remove',
            'amount': 99.99, 'from_account': 198, 'to_account': 182
        }
        self.assertEqual(vars(self.bank2_movements[0]), result)

    def test_third_bank(self):
        result = {
            'date': datetime.date(2019, 10, 5), 'transaction_type': 'remove',
            'amount': 5.44, 'from_account': 198, 'to_account': 182
        }
        self.assertEqual(vars(self.bank3_movements[0]), result)
