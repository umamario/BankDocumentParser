import os
from datetime import datetime as dt
from typing import List, Union

import pandas as pd
from orderedset import OrderedSet


class MovementObject(object):

    def __init__(self, date: dt, transaction_type: str, amount: float, from_account: int, to_account: int):
        self.date = date
        self.transaction_type = transaction_type
        self.amount = amount
        self.from_account = from_account
        self.to_account = to_account


class BankParser(object):
    REPORT_HEADER: List[str]

    def __init__(self, input_file_path: str):
        self.df: pd.DataFrame = self.generate_dataframe(input_file_path)
        self.movements = []

    def add_data_object(self, date: dt, transaction_type: str, amount: float, from_account: int,
                        to_account: int) -> None:
        movement = MovementObject(date, transaction_type, amount, from_account, to_account)
        self.movements.append(movement)

    def generate_report(self) -> List[MovementObject]:
        self._parse_dataframe()
        return self.movements

    @staticmethod
    def generate_dataframe(input_file_path: str) -> pd.DataFrame:
        if not os.path.isfile(input_file_path):
            raise FileNotFoundError

        _, file_extension = os.path.splitext(input_file_path)

        if file_extension == ".csv":
            return pd.read_csv(input_file_path)
        elif file_extension == ".json":
            return pd.read_json(input_file_path)
        else:
            raise NotImplementedError(f"File extension {file_extension} is not implemented")

    def _parse_dataframe(self) -> None:
        raise NotImplementedError(
            "subclasses of %s must provide a _parse_dataframe() method" % self.__class__.__name__
        )

    def _raise_for_header(self, header: Union[str, List[str]], ideal_header: Union[str, List[str]] = None) -> None:
        valid = True
        if ideal_header is None:
            ideal_header = self.REPORT_HEADER
        if isinstance(ideal_header, str) and isinstance(header, str):
            if ideal_header != header:
                valid = False
        elif isinstance(ideal_header, list) and isinstance(header, list):
            if not OrderedSet(ideal_header) <= OrderedSet(header):
                valid = False
        else:
            raise NotImplementedError("For type %s and %s" % (type(header), type(ideal_header)))

        if not valid:
            raise AssertionError(f"Header expected {ideal_header} does not match with the received {header}")
