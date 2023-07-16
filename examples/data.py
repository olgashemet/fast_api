from devtools import debug
from typing import NamedTuple, Any, Optional

from pydantic.main import BaseModel

import dataclass



class Data(BaseModel):
    campaign_data: Any
    phone: Optional[str]
    age: int
    xxx: Optional[int] = None

def sum_age(age):
    something=10
    return something
def useful_function(age) -> Data:
    campaign_data="A"
    phone="12"
    age= sum_age(age)
    return Data(campaign_data=campaign_data, phone=phone, age=age)

def existing_endpoint(age):
    x = useful_function(age)
    print(x.phone)

def api_endpoint(age):
    resp1 = vars(useful_function(age))
    debug('resp1')
    debug(resp1)

    resp2 = useful_function(10)
    debug(resp2.xxx)


api_endpoint(10)

def get_division(df, nom, den):
    if nom in df and den in df and df[den] > 0:
        return df[nom] / df[den]
    return 0
class CampaignAggregatedDataPoint(BaseModel):
    budget_spent: float
    partner_budget_spent: Optional[float]
    items_sold: int
    attributed_gmv: float
    ad_impressions: int
    viewable_impressions: Optional[int]
    clicks_ad: int
    ctr: float
    cpc: float
    roas: float
    ropi: Optional[float]
    acos: float

def aggregate_device_data(self, data):

    budget_spent= data.budget_spent.sum()
    items_sold = data.items_sold.sum()
    attributed_gmv= data.attributed_gmv.sum()
    ad_impressions = data.ad_impressions.sum()
    partner_budget_spent= data.partner_budget_spent.sum()
    clicks_ad = data.clicks_ad.sum()
    # ctr = get_division(overview, 'clicks_ad', 'ad_impressions') * 100
    # cpc = get_division(overview, 'budget_spent', 'clicks_ad')
    # overview['roas'] = get_division(overview, 'attributed_gmv', 'budget_spent')
    # overview['acos'] = get_division(overview, 'budget_spent', 'attributed_gmv') * 100
    # overview['ropi'] = get_overview_data_1(overview).ropi

    return CampaignAggregatedDataPoint(budget_spent=budget_spent,items_sold=items_sold, attributed_gmv=attributed_gmv,
                                       ad_impressions=ad_impressions, partner_budget_spent=partner_budget_spent,clicks_ad=clicks_ad)


import pandas as pd

# initialize list of lists
data = [['budget_spent', 10], ['items_sold', 15], ['juli', 14],
        ['attributed_gmv', 10], ['ad_impressions', 15], ['partner_budget_spent', 14], ['clicks_ad', 14]]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])
