import numpy as np
random_array=np.random.uniform(100, 500, size=(30, 5)).round(2)
print(random_array)
average_prices=random_array.mean(axis=0).round(2)
print(average_prices)
max_stock=random_array.max()
max_day, max_company=np.unravel_index(np.argmax(random_array), random_array.shape)
print(f"The stock price was maximum on{max_day}\n It was of the company {max_company}")
min_stock=random_array.min()
normalization=((random_array-min_stock)/(max_stock-min_stock)).round(2)
print(normalization)
risky_investment=np.any(random_array<200, axis=1)
print(risky_investment)