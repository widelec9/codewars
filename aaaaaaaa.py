import unittest as ut
from sandbox import *


class InvoiceRowTests(ut.TestCase):
    def test_defaults_set(self):
        """Defaults set"""
        row = InvoiceRow("Test Row 1", 1.99)
        self.assertEqual(row.id, 0)
        self.assertEqual(row.description, "Test Row 1")
        self.assertEqual(row.quantity, 1)
        self.assertEqual(row.unit_cost, 1.99)
        self.assertEqual(row.taxable, True)
        self.assertEqual(row.value, 1.99)

    def test_non_defaults_set(self):
        """Non-defaults set"""
        row = InvoiceRow("Test Row 2", 7.00, 6, False)
        self.assertEqual(row.id, 1)
        self.assertEqual(row.description, "Test Row 2")
        self.assertEqual(row.quantity, 6)
        self.assertEqual(row.unit_cost, 7.00)
        self.assertEqual(row.taxable, False)
        self.assertEqual(row.value, 42.00)


class InvoiceTests(ut.TestCase):
    def test_defaults_set(self):
        """Defaults set"""
        invoice = Invoice()
        self.assertEqual(invoice.tax_rate, 0.20)

    def test_non_defaults_set(self):
        """Non-defaults set"""
        invoice = Invoice(0.15)
        self.assertEqual(invoice.tax_rate, 0.15)

    def test_content(self):
        """Content"""
        invoice = Invoice()
        invoice.add_row(InvoiceRow("Test Row 1", 4.95))
        self.assertEqual(len(invoice.rows), 1)
        invoice.add_row(InvoiceRow("Test Row 2", 9.95))
        self.assertEqual(len(invoice.rows), 2)
        invoice.add_row(InvoiceRow("Test Row 3", 19.95, 2))
        self.assertEqual(len(invoice.rows), 3)


class HelperMethodsTests(ut.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.debit = InvoiceRow("Debit", -1.00)
        cls.gratis = InvoiceRow("Gratis", 0.00)
        cls.credit = InvoiceRow("Credit", 1.00)

    def test_is_debit_is_credit(self):
        """is_debit/is_credit"""
        self.assertEqual(is_debit(self.debit), True)
        self.assertEqual(is_credit(self.debit), False)
        self.assertEqual(is_debit(self.gratis), False)
        self.assertEqual(is_credit(self.gratis), False)
        self.assertEqual(is_debit(self.credit), False)
        self.assertEqual(is_credit(self.credit), True)

    def test_is_taxable(self):
        """is_taxable"""
        taxed = InvoiceRow("Taxed", 1.00, taxable=True)
        untaxed = InvoiceRow("Untaxed", 1.00, taxable=False)
        self.assertEqual(is_taxable(taxed), True)
        self.assertEqual(is_taxable(untaxed), False)

    def test_printable_cost(self):
        """printable_cost"""
        self.assertEqual(printable_cost(self.debit.unit_cost), "-1.00")
        self.assertEqual(printable_cost(self.gratis.unit_cost), "Gratis")
        self.assertEqual(printable_cost(self.credit.unit_cost), "1.00")

    def test_printable_row(self):
        """printable_row"""
        taxed_row = InvoiceRow("Taxed Row", 1.00, 2, True)
        untaxed_row = InvoiceRow("Untaxed Row", 1.00, 2, False)
        large_qty_row = InvoiceRow("Large Quantity Row", 1.00, 2000, True)
        large_unit_cost_row = InvoiceRow("Large Unit Cost Row", 1000.00, 2, True)
        tax_rate = 0.10
        self.assertEqual(printable_row(taxed_row, tax_rate), ("Taxed Row", "2", "1.00", "0.10", "2.00", "2.20"))
        self.assertEqual(printable_row(untaxed_row, tax_rate), ("Untaxed Row", "2", "1.00", "0.00", "2.00", "2.00"))
        self.assertEqual(printable_row(large_qty_row, tax_rate), ("Large Quantity Row", "2,000", "1.00", "0.10", "2,000.00", "2,200.00"))
        self.assertEqual(printable_row(large_unit_cost_row, tax_rate), ("Large Unit Cost Row", "2", "1,000.00", "0.10", "2,000.00", "2,200.00"))


# class InvoicePrinterTests(ut.TestCase):
#     def test_credits_only(self):
#         """Credits only"""
#         r1 = InvoiceRow("Test Row 1", 1.00)
#         r2 = InvoiceRow("Test Row 2", 2.00, 2)
#         r3 = InvoiceRow("Test Row 3", 3.00, 3, False)
#         tax_rate = 0.10
#         invoice = Invoice(tax_rate)
#         invoice.add_row(r1)
#         invoice.add_row(r2)
#         invoice.add_row(r3)
#         output = InvoicePrinter().generate_invoice(invoice)
#         self.assertEqual(next(output), printable_row(r1, tax_rate))
#         self.assertEqual(next(output), printable_row(r2, tax_rate))
#         self.assertEqual(next(output), printable_row(r3, tax_rate))
#         self.assertEqual(next(output), ("Lines", "3"))
#         self.assertEqual(next(output), ("Items", "6"))
#         self.assertEqual(next(output), ("Sub Total", "14.00"))
#         self.assertEqual(next(output), ("Tax", "0.50"))
#         self.assertEqual(next(output), ("Total", "14.50"))
#
#     def test_debits_only(self):
#         """Debits only"""
#         r1 = InvoiceRow("Test Row 1", -1.00)
#         r2 = InvoiceRow("Test Row 2", -2.00, 2)
#         r3 = InvoiceRow("Test Row 3", -3.00, 3, False)
#         tax_rate = 0.10
#         invoice = Invoice(tax_rate)
#         invoice.add_row(r1)
#         invoice.add_row(r2)
#         invoice.add_row(r3)
#         output = InvoicePrinter().generate_invoice(invoice)
#         self.assertEqual(next(output), printable_row(r1, tax_rate))
#         self.assertEqual(next(output), printable_row(r2, tax_rate))
#         self.assertEqual(next(output), printable_row(r3, tax_rate))
#         self.assertEqual(next(output), ("Lines", "3"))
#         self.assertEqual(next(output), ("Items", "6"))
#         self.assertEqual(next(output), ("Sub Total", "-14.00"))
#         self.assertEqual(next(output), ("Tax", "-0.50"))
#         self.assertEqual(next(output), ("Total", "-14.50"))
#
#     def test_both_debits_and_credits(self):
#         """Both Debits & Credits"""
#         r1 = InvoiceRow("Test Row 1", -1.00)
#         r2 = InvoiceRow("Test Row 2", 2.00, 2)
#         r3 = InvoiceRow("Test Row 3", 3.00, 3, False)
#         tax_rate = 0.20
#         invoice = Invoice(tax_rate)
#         invoice.add_row(r1)
#         invoice.add_row(r2)
#         invoice.add_row(r3)
#         output = InvoicePrinter().generate_invoice(invoice)
#         # Expect credits, then debits
#         self.assertEqual(next(output), printable_row(r2, tax_rate))
#         self.assertEqual(next(output), printable_row(r3, tax_rate))
#         self.assertEqual(next(output), printable_row(r1, tax_rate))
#         self.assertEqual(next(output), ("Lines", "3"))
#         self.assertEqual(next(output), ("Items", "6"))
#         self.assertEqual(next(output), ("Sub Total", "12.00"))
#         self.assertEqual(next(output), ("Tax", "0.60"))
#         self.assertEqual(next(output), ("Total", "12.60"))
#
#     def test_debits_credits_and_freebies(self):
#         """Debits, Credits & Freebies"""
#         r1 = InvoiceRow("Test Row 1", 3.00, 3, False)
#         r2 = InvoiceRow("Test Row 2", 0.00, 2)
#         r3 = InvoiceRow("Test Row 3", -1.00)
#         r4 = InvoiceRow("Test Row 4", 2.00, 2)
#         r5 = InvoiceRow("Test Row 5", 0.00, 1111)
#         tax_rate = 0.20
#         invoice = Invoice(tax_rate)
#         invoice.add_row(r1)
#         invoice.add_row(r2)
#         invoice.add_row(r3)
#         invoice.add_row(r4)
#         invoice.add_row(r5)
#         output = InvoicePrinter().generate_invoice(invoice)
#         # Expect credits, then debits, then gratis
#         self.assertEqual(next(output), printable_row(r1, tax_rate))
#         self.assertEqual(next(output), printable_row(r4, tax_rate))
#         self.assertEqual(next(output), printable_row(r3, tax_rate))
#         self.assertEqual(next(output), printable_row(r2, tax_rate))
#         self.assertEqual(next(output), printable_row(r5, tax_rate))
#         self.assertEqual(next(output), ("Lines", "5"))
#         self.assertEqual(next(output), ("Items", "1119"))
#         self.assertEqual(next(output), ("Sub Total", "12.00"))
#         self.assertEqual(next(output), ("Tax", "0.60"))
#         self.assertEqual(next(output), ("Total", "12.60"))


if __name__ == '__main__':
    ut.main()
