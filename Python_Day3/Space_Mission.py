import numpy as np
resources=np.random.uniform(1, 100, size=(6, 3)).round(2)
Oxygen, Water, Food,= total=np.sum(resources, axis=0)
print(f"Oxygen = {Oxygen} Water = {Water} Food = {Food}" )

max_val=np.max(resources, axis=0)
max_oxygen, max_water, max_food = max_val
max_monthly=np.max(resources)
max_month_index=np.unravel_index(np.argmax(resources), resources.shape)
print(f"Highest Consumption : Water {max_water} tons in month {max_month_index[0]+1}")

stand=np.std(resources, axis=0)
stand_oxygen, stand_water, stand_food=stand
print(f"Standard Deviation : Water {stand_oxygen}, Water {stand_water}, Food {stand_food}")