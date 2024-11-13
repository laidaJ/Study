travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"],
},
]

def add_new_country(country, visits, cities):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities,
        })

add_new_country("Russia", 2, ["Moscow", "Saint Peterburg"])
print(travel_log)
