hex_values = "0123456789abcdef"
input='abc'
data = [
    {'budget_spent': 5102.306640625, 'partner_budget_spent': 5102.306640625, 'items_sold': 420, 'attributed_gmv': 11488.7900390625, 'ad_impressions': 922142, 'viewable_impressions': 922142, 'clicks_ad': 10460, 'ctr': 1.1343155392553423, 'cpc': 0.48779222185707455, 'roas': 2.251684048805835, 'cpmv': 5.533102971803692, 'cpm': 5.533102971803692, 'ropi': 2.251684048805835, 'acos': 44.41113641655352, 'add_to_wishlist': 651, 'add_to_cart': 2642, 'pdp_views': 22972, 'conversion_rate_clicks': 4.015296367112811, 'conversion_rate_pdp': 1.8283127285390912, 'cpsi': 12.148349144345238, 'campaign_name': "HBOD_MensDaywear_Sep'22", 'n_code': 'N1030995', 'campaign_objective': 'p', 'planned_start_date': '2022-09-23', 'planned_end_date': '2022-10-11'},
    {'budget_spent': 5093.30126953125, 'partner_budget_spent': 5093.30126953125, 'items_sold': 94, 'attributed_gmv': 3964.949951171875, 'ad_impressions': 1073726, 'viewable_impressions': 1073726, 'clicks_ad': 6822, 'ctr': 0.6353576238258177, 'cpc': 0.7465994238538918, 'roas': 0.778463854705569, 'cpmv': 4.743576358895333, 'cpm': 4.743576358895333, 'ropi': 0.778463854705569, 'acos': 128.45814624475088, 'add_to_wishlist': 498, 'add_to_cart': 706, 'pdp_views': 12408, 'conversion_rate_clicks': 1.3778950454412195, 'conversion_rate_pdp': 0.7575757575757576, 'cpsi': 54.18405605884308, 'campaign_name': "HBOD_MensNightwear_Sep'22", 'n_code': 'N1030999', 'campaign_objective': 'p', 'planned_start_date': '2022-09-23', 'planned_end_date': '2022-10-20'},
    {'budget_spent': 5105.08837890625, 'partner_budget_spent': 5105.08837890625, 'items_sold': 240, 'attributed_gmv': 7914.41015625, 'ad_impressions': 1084687, 'viewable_impressions': 1084687, 'clicks_ad': 10987, 'ctr': 1.0129189342178897, 'cpc': 0.464648073077842, 'roas': 1.5502978706056112, 'cpmv': 4.706508309684038, 'cpm': 4.706508309684038, 'ropi': 1.5502978706056112, 'acos': 64.50371384482546, 'add_to_wishlist': 845, 'add_to_cart': 1748, 'pdp_views': 21228, 'conversion_rate_clicks': 2.184399745153363, 'conversion_rate_pdp': 1.1305822498586773, 'cpsi': 21.27120157877604, 'campaign_name': "HBOD_Womens Daywear _Sep'22", 'n_code': 'N1030996', 'campaign_objective': 'p', 'planned_start_date': '2022-09-23', 'planned_end_date': '2022-10-11'}
]
result={d: hex_values.index(d) for d in input}

print(data)

lst=[1,3,5]

funct=lambda x, y : x+y


#map is in order applied to each element
# is map a function ?
b = map (int, ['1', '2'])
for x in b:
    print (type(x))

lst_new=map(lambda x: x if x > 1 else None, lst)
# why i do not see  list ??? in the print(list(lst_new))
# i want to do without else  as i want to get [ 3, 5]
print(list(lst_new))