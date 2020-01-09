from dateutil.parser import parse

from bank_parser import BankParser


class Bank2Parser(BankParser):
    REPORT_HEADER = ["date", "transaction", "amounts", "to", "from"]

    def _parse_dataframe(self):
        self._raise_for_header(list(self.df.columns))

        for _, transaction in self.df.iterrows():
            self.add_data_object(
                date=parse(transaction["date"], dayfirst=True).date(),
                transaction_type=transaction["transaction"],
                amount=transaction["amounts"],
                from_account=transaction["from"],
                to_account=transaction["to"]
            )
