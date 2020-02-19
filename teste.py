from facebook_business.api import FacebookAdsApi
from facebook_business import adobjects
from facebook_business.adobjects.adaccountuser import AdAccountUser
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.adobjects.adreportrun import AdReportRun
import json;
import time
FacebookAdsApi.init(access_token='EAALdEhJRaNcBAAIfEz9w1MGp0ZA1P6f6GPFAKwXyknOg3Vk7h8WGwIBINlRw2Pg9u0hxFZClZBvlWJZBfT8WNXC2ZBroBk0CkcVr9KHIFA6Gv2MdWValCRCvxxVsnmjvZACMasuwGDAf3fBLpbV5WGnRjiRMi0yrYOK2CrJZCAytS4AQGcwOTEEUMWfOkGHR5YZD')
me = AdAccountUser(fbid='me')
ad_accounts = me.get_ad_accounts()
# print(ad_accounts)
params = {
        'level':'ad',
        'fields': [
        AdsInsights.Field.campaign_id,
        AdsInsights.Field.campaign_name,
        AdsInsights.Field.adset_name,
        AdsInsights.Field.ad_name,
        AdsInsights.Field.spend,
        AdsInsights.Field.impressions,
        AdsInsights.Field.clicks,
        AdsInsights.Field.buying_type,
        AdsInsights.Field.objective,        
        AdsInsights.Field.actions
      ],
        # 'breakdowns': [AdsInsights.Breakdown.hourly_stats_aggregated_by_advertiser_time_zone],
         'time_range': {
            'since':  "2019-11-02", 
            'until': "2020-02-17"
        },
        'action_attribution_windows': ['7d_click'],
    }

result =  ad_accounts[1].get_insights(params={'time_range': {
                                         'since':  "2019-11-02", 
                                            'until': "2020-02-17"},
                                            'time_increment':1,
                                           'level':'ad'
                                          },
                                          fields=[AdsInsights.Field.account_id,
                                            AdsInsights.Field.account_name,
                                           AdsInsights.Field.ad_id,
                                           AdsInsights.Field.ad_name,
                                           AdsInsights.Field.adset_id,
                                           AdsInsights.Field.adset_name,
                                           AdsInsights.Field.campaign_id,
                                           AdsInsights.Field.campaign_name,
                                           AdsInsights.Field.cost_per_outbound_click,
                                           AdsInsights.Field.outbound_clicks,
                                           AdsInsights.Field.spend
                                          ])
print (result)
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(result[0], f, ensure_ascii=False, indent=4)

