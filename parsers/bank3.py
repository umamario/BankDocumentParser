from dateutil.parser import parse

from bank_parser import BankParser


class Bank3Parser(BankParser):
    REPORT_HEADER = ["date_readable", "type", "euro", "cents", "to", "from"]

    def _parse_dataframe(self):
        self._raise_for_header(list(self.df.columns))

        for _, transaction in self.df.iterrows():
            self.add_data_object(
                date=parse(transaction["date_readable"]).date(),
                transaction_type=transaction["type"],
                amount=float(f"{transaction['euro']}.{transaction['cents']}"),
                from_account=transaction["from"],
                to_account=transaction["to"]
            )
