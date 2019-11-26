class InvoiceRow(object):
    id = -1

    def __init__(self, description: str, unit_cost: float, quantity: int = 1, taxable: bool = True):
        InvoiceRow.id += 1
        self.description = description
        self.quantity = quantity
        self.unit_cost = unit_cost
        self.taxable = taxable

    @property
    def value(self):
        return self.quantity * self.unit_cost


class Invoice(object):
    def __init__(self, rate: float = 0.2):
        self.tax_rate = rate
        self.rows = []

    def add_row(self, row_: InvoiceRow):
        self.rows += [row_]


class InvoicePrinter(object):
    @staticmethod
    def get_credit_rows(invoice_):
        return [row_ for row_ in invoice_.rows if is_credit(row_)]

    @staticmethod
    def get_debit_rows(invoice_):
        return [row_ for row_ in invoice_.rows if is_debit(row_)]

    @staticmethod
    def get_free_rows(invoice_):
        return [row_ for row_ in invoice_.rows if not (is_debit(row_) or is_credit(row_))]

    @staticmethod
    def get_sub_total(invoice_):
        return sum([row_.value for row_ in invoice_.rows])

    @staticmethod
    def get_tax_total(invoice_):
        return sum([row_.value for row_ in invoice_.rows if is_taxable(row_)]) * invoice_.tax_rate

    @staticmethod
    def get_grand_total(invoice_):
        return InvoicePrinter.get_sub_total(invoice_) + InvoicePrinter.get_tax_total(invoice_)

    @staticmethod
    def generate_invoice(invoice_):
        lines = 0
        items = 0

        tax_rate_ = round(invoice_.tax_rate, 2)

        for row_ in InvoicePrinter.get_credit_rows(invoice_):
            lines += 1
            items += row_.quantity
            yield printable_row(row_, tax_rate_)

        for row_ in InvoicePrinter.get_debit_rows(invoice_):
            lines += 1
            items += row_.quantity
            yield printable_row(row_, tax_rate_)

        for row_ in InvoicePrinter.get_free_rows(invoice_):
            lines += 1
            items += row_.quantity
            yield printable_row(row_, tax_rate_)

        yield ("Lines", str(lines))
        yield ("Items", str(items))
        yield ("Sub Total", "{:.2f}".format(InvoicePrinter.get_sub_total(invoice_)))
        yield ("Tax", "{:.2f}".format(InvoicePrinter.get_tax_total(invoice_)))
        yield ("Total", "{:.2f}".format(InvoicePrinter.get_grand_total(invoice_)))


def printable_row(row_: InvoiceRow, tax_rate_: float):
    if not row_.taxable:
        tax_rate_ = 0
    return row_.description, '{:,}'.format(row_.quantity), '{:,.2f}'.format(row_.unit_cost), '{:,.2f}'.format(tax_rate_), \
        '{:,.2f}'.format(row_.value), '{:,.2f}'.format(row_.value * (1 + tax_rate_))


def printable_cost(cost_: float):
    return '{:,.2f}'.format(cost_) if cost_ else 'Gratis'


def is_taxable(row_: InvoiceRow):
    return row_.taxable


def is_debit(row_: InvoiceRow):
    return row_.unit_cost < 0


def is_credit(row_: InvoiceRow):
    return row_.unit_cost > 0
