world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Аргентина'

for year, champion in world_champions.items():
    print(year, '-', champion)

country = 'Италия'

#print('Италия cтановилась чемпионом мира по футболу в 21 веке!' if 'Италия' in world_champions.values() else 'Италия не выигрывала чемпионат мира по футболу в 21 веке.')

print(country + ' становилась чемпионом мира по футболу в 21 веке!' if country in world_champions.values() else country + ' не выигрывала чемпионат мира по футболу в 21 веке.')