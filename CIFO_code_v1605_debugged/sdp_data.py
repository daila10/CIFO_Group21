#data from https://www.kaggle.com/datasets/ofrancisco/emoji-diet-nutritional-data-sr28?select=Emoji+Diet+Nutritional+Data+%28g%29+-+EmojiFoods+%28g%29.csv

import pandas as pd

data = pd.read_excel('complete_diet.xlsx')

data[['Price','Calories (kcal)','Carbohydrates (g)','Protein (g)','Total Fat (g)','Vitamin B6 (mg)','Vitamin A (IU)',
'Vitamin B12 (ug)','Vitamin C (mg)','Vitamin D (IU)','Vitamin E (IU)','Vitamin K (ug)','Thiamin (mg)','Riboflavin (mg)',
'Niacin (mg)','Pantothenic Acid (mg)']] = data[['Price','Calories (kcal)','Carbohydrates (g)','Protein (g)','Total Fat (g)','Vitamin B6 (mg)','Vitamin A (IU)',
'Vitamin B12 (ug)','Vitamin C (mg)','Vitamin D (IU)','Vitamin E (IU)','Vitamin K (ug)','Thiamin (mg)','Riboflavin (mg)',
'Niacin (mg)','Pantothenic Acid (mg)']] * 50

data = data[['name','Price','Calories (kcal)','Carbohydrates (g)','Protein (g)','Total Fat (g)','Vitamin B6 (mg)','Vitamin A (IU)',
'Vitamin B12 (ug)','Vitamin C (mg)','Vitamin D (IU)','Vitamin E (IU)','Vitamin K (ug)','Thiamin (mg)','Riboflavin (mg)',
'Niacin (mg)','Pantothenic Acid (mg)']]

data = data.values.tolist()

# Nutrient minimums.
nutrients = [
    ['Calories (kcal)', 1200], 
    ['Carbohydrates (g)', 130],
    ['Protein (g)', 70], 
    ['Total Fat (g)', 44], 
    ['Vitamin B6 (mg)', 1.3], 
    ['Vitamin A (IU)', 1000], 
    ['Vitamin B12 (ug)', 2.4], 
    ['Vitamin C (mg)', 90], 
    ['Vitamin D (IU)', 600], 
    ['Vitamin E (IU)', 15], 
    ['Vitamin K (ug)', 120], 
    ['Thiamin (mg)', 1.2], 
    ['Riboflavin (mg)', 1.3], 
    ['Niacin (mg)', 16], 
    ['Pantothenic Acid (mg)', 5]
    ]


# Commodity, Unit, 1939 price (cents), Calories (kcal), Protein (g),
# Calcium (g), Iron (mg), Vitamin A (KIU), Vitamin B1 (mg), Vitamin B2 (mg),
# Niacin (mg), Vitamin C (mg)
