from dateutil.parser import parse

from bank_parser import BankParser


class Bank1Parser(BankParser):
    REPORT_HEADER = ["timestamp", "type", "amount", "from", "to"]

    def _parse_dataframe(self):
        self._raise_for_header(list(self.df.columns))

        for _, transaction in self.df.iterrows():
            self.add_data_object(
                date=parse(transaction["timestamp"]).date(),
                transaction_type=transaction["type"],
                amount=transaction["amount"],
                from_account=transaction["from"],
                to_account=transaction["to"]
            )
