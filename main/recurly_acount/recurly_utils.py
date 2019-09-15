import recurly

from main.settings import RECURLY_API_KEY, RECURLY_SUBDOMAIN, RECURLY_CURRENCY


class Recurly():

    def __init__(self):
        recurly.API_KEY = RECURLY_API_KEY
        recurly.SUBDOMAIN = RECURLY_SUBDOMAIN
        recurly.DEFAULT_CURRENCY = RECURLY_CURRENCY

    def get_recurly_invoice(self, invoice_number):
        return recurly.Invoice.get(invoice_number)

    def get_recurly_account(self, account_code):
        return recurly.Account.get(account_code)

    def get_recurly_plan(self, plan_code):
        return recurly.Plan.get(plan_code)

    def get_recurly_paid_invoices(self):
        invoices = recurly.Invoice.all_paid()
        for invoice in invoices:
            print('Invoice: %s' % invoice)

    def get_users_recurly_paid_invoices(self):
        invoices = recurly.Invoice.all_paid({'account_code':'1'})
        for invoice in invoices:
            print('Invoice: %s' % invoice)

    def get_all_active_subscribers(self):
        return recurly.Account.all_active()


