from typing import Any

from devtools import debug

try:
    from mcr_client import get_campaign_country  # type: ignore
except ImportError:
    debug(unknown_module="mcr_client")


hex_values = "0123456789abcdef"
input_value = "abc"
data = [
    {
        "budget_spent": 5102.306640625,
        "partner_budget_spent": 5102.306640625,
        "items_sold": 420,
        "attributed_gmv": 11488.7900390625,
        "ad_impressions": 922142,
        "viewable_impressions": 922142,
        "clicks_ad": 10460,
        "ctr": 1.1343155392553423,
        "cpc": 0.48779222185707455,
        "roas": 2.251684048805835,
        "cpmv": 5.533102971803692,
        "cpm": 5.533102971803692,
        "ropi": 2.251684048805835,
        "acos": 44.41113641655352,
        "add_to_wishlist": 651,
        "add_to_cart": 2642,
        "pdp_views": 22972,
        "conversion_rate_clicks": 4.015296367112811,
        "conversion_rate_pdp": 1.8283127285390912,
        "cpsi": 12.148349144345238,
        "campaign_name": "HBOD_MensDaywear_Sep'22",
        "n_code": "N1030995",
        "campaign_objective": "p",
        "planned_start_date": "2022-09-23",
        "planned_end_date": "2022-10-11",
    },
    {
        "budget_spent": 5093.30126953125,
        "partner_budget_spent": 5093.30126953125,
        "items_sold": 94,
        "attributed_gmv": 3964.949951171875,
        "ad_impressions": 1073726,
        "viewable_impressions": 1073726,
        "clicks_ad": 6822,
        "ctr": 0.6353576238258177,
        "cpc": 0.7465994238538918,
        "roas": 0.778463854705569,
        "cpmv": 4.743576358895333,
        "cpm": 4.743576358895333,
        "ropi": 0.778463854705569,
        "acos": 128.45814624475088,
        "add_to_wishlist": 498,
        "add_to_cart": 706,
        "pdp_views": 12408,
        "conversion_rate_clicks": 1.3778950454412195,
        "conversion_rate_pdp": 0.7575757575757576,
        "cpsi": 54.18405605884308,
        "campaign_name": "HBOD_MensNightwear_Sep'22",
        "n_code": "N1030999",
        "campaign_objective": "p",
        "planned_start_date": "2022-09-23",
        "planned_end_date": "2022-10-20",
    },
    {
        "budget_spent": 5105.08837890625,
        "partner_budget_spent": 5105.08837890625,
        "items_sold": 240,
        "attributed_gmv": 7914.41015625,
        "ad_impressions": 1084687,
        "viewable_impressions": 1084687,
        "clicks_ad": 10987,
        "ctr": 1.0129189342178897,
        "cpc": 0.464648073077842,
        "roas": 1.5502978706056112,
        "cpmv": 4.706508309684038,
        "cpm": 4.706508309684038,
        "ropi": 1.5502978706056112,
        "acos": 64.50371384482546,
        "add_to_wishlist": 845,
        "add_to_cart": 1748,
        "pdp_views": 21228,
        "conversion_rate_clicks": 2.184399745153363,
        "conversion_rate_pdp": 1.1305822498586773,
        "cpsi": 21.27120157877604,
        "campaign_name": "HBOD_Womens Daywear _Sep'22",
        "n_code": "N1030996",
        "campaign_objective": "p",
        "planned_start_date": "2022-09-23",
        "planned_end_date": "2022-10-11",
    },
]
result = {d: hex_values.index(d) for d in input_value}

debug(data)

lst = [1, 3, 5]

funct = lambda x, y: x + y  # noqa: E731


# map is in order applied to each element
# is map a function ?
ints = map(int, ["1", "2"])
for item in ints:
    debug(type(item))

lst = [1, 2, 3, 4]
new_lst = lambda x: x if x > 1 else None  # noqa: E731

lst_new = map(lambda x: x if x > 1 else None, lst)  # noqa: C417
# why i do not see  list ??? in the print(list(lst_new))
# i want to do without else  as i want to get [ 3, 5]
debug(list(lst_new))


country = {
    "n_code": "N1030995",
    "campaign_name": "HBOD_MensDaywear_Sep'22",
    "campaign_objective": "p",
    "overview_data": {
        "budget_spent": 5102.306496786885,
        "partner_budget_spent": 5102.306496786885,
        "items_sold": 420,
        "attributed_gmv": 11488.789942741394,
        "ad_impressions": 922142,
        "viewable_impressions": 922142,
        "clicks_ad": 10460,
        "ctr": 1.1343155392553423,
        "cpc": 0.48779220810582075,
        "roas": 2.251685575920678,
        "cpmv": 5.533102815821083,
        "cpm": 5.533102815821083,
        "ropi": 225.1685575920678,
        "acos": 44.41117404196703,
        "add_to_wishlist": 0,
        "add_to_cart": 0,
        "pdp_views": 0,
    },
    "country_data": [
        {
            "budget_spent": 1229.1486729383469,
            "partner_budget_spent": 1229.1486729383469,
            "items_sold": 34,
            "attributed_gmv": 1177.2000007629395,
            "ad_impressions": 215469,
            "viewable_impressions": 215469,
            "clicks_ad": 1558,
            "ctr": 0.7230738528512223,
            "cpc": 0.7889272611927772,
            "roas": 0.957736054783982,
            "cpmv": 5.704526743700239,
            "cpm": 5.704526743700239,
            "ropi": 95.77360547839821,
            "acos": 104.4129011333452,
            "add_to_wishlist": 0,
            "add_to_cart": 0,
            "pdp_views": 0,
            "country": "AT",
        },
        {
            "budget_spent": 3873.157823848538,
            "partner_budget_spent": 3873.157823848538,
            "items_sold": 386,
            "attributed_gmv": 10311.589941978455,
            "ad_impressions": 706673,
            "viewable_impressions": 706673,
            "clicks_ad": 8902,
            "ctr": 1.2597056913169173,
            "cpc": 0.43508849964598273,
            "roas": 2.6623211371573827,
            "cpmv": 5.480834592305831,
            "cpm": 5.480834592305831,
            "ropi": 266.23211371573825,
            "acos": 37.56120875289002,
            "add_to_wishlist": 0,
            "add_to_cart": 0,
            "pdp_views": 0,
            "country": "DE",
        },
    ],
}


def get_country_data_v2(data: Any, kpi: Any, sort: str) -> dict:
    debug(data, kpi, sort)

    # Using the max() function with a custom key
    # to find the dictionary with the highest pdp_views
    if sort == "max":
        item_with_extremum_kpi = max(data, key=lambda x: x.get(kpi, 0))
    elif sort == "min":
        item_with_extremum_kpi = min(data, key=lambda x: x.get(kpi, 0))
        debug(sort, data, item_with_extremum_kpi.get("n_code"))

    n_code = item_with_extremum_kpi.get("n_code")
    country_data = get_campaign_country(n_code)["country_data"]
    country_data.sort(key=lambda x: x[kpi] if sort == "min" else -1 * x[kpi])

    def sort_my_data(kpi: dict, direction: str = "min") -> list:
        return sorted(
            country_data,
            key=lambda x: x[kpi],
            reverse=direction != "min",
        )

    sort_my_data(data, "budget")

    debug(**{"sorted data": country_data})
    # countires = [
    #     {
    #         "country": d["country"],
    #         kpi: d[kpi],
    #     }
    #     for d in country_data
    # ]

    compact_list = [f'{x["country"]}- {x[kpi]}' for x in country_data]
    [d["campaign_name"] for d in data][0]
    return {
        "format": "str_list",
        "data": [
            {
                "type": "string",
                "content": (
                    "here are your "
                    f'{"top" if sort == "max" else "last" }'
                    f" markets sorted by {kpi}"
                ),
            },
            {"type": "array", "content": compact_list},
        ],
    }

    # Returning the campaign_name
    # from the dictionary with the highest pdp_views
    # return countires
