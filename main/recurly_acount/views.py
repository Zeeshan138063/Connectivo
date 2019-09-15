from django.shortcuts import render

# Create your views here.
import uuid
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views import View
from iso8601 import iso8601
from recurly import PageError

# from mapport.core.views import BaseView

import json
# from mapport.core.util import JSONEncoder
import xml.etree.ElementTree as ET
from xmljson import yahoo as yh
import requests
import recurly
from django.core import serializers
from django.urls import resolve
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt
import re
import datetime
import pandas as pd

from recurly_acount.recurly_utils import Recurly


class SubscribeView(View):

    def __init__(self):
        self.recurly_obj = Recurly()
        # super(UserView, self).__init__()


    def get_paid_invoices(self):
        #  Step1: get all active accounts
        self.recurly_obj = Recurly()
        all_active_accounts = pd.DataFrame(self.recurly_obj.get_all_active_subscribers())

        # Step2: for each account check if subscription is live or active,Fetch the paid invoices
        '''
        has_live_subscription
        True if the account has at least one live subscription.
        
        has_active_subscription
        True if the account has at least one active subscription.
        '''
        for index, row in all_active_accounts.iterrows():
            account = row[0]
            if account.has_live_subscription or account.has_active_subscription:
                invoices_df = pd.DataFrame(account.invoices(state='paid'))

                # Step3: Fetch plans for each account
                subscriptions_df =pd.DataFrame(account.subscriptions(state='active', order='desc'))
                for index_subscription, row_subscription in subscriptions_df.iterrows():
                    subscription =row_subscription[0]
                    print(subscription.plan)



        # Step4: IF NEW INVOICE OR PLAN save to PostgreSQL
        # Step5: Save to Fortnox






