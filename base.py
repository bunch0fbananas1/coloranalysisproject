import matplotlib.pyplot as plt
from pytrends.request import TrendReq
import pandas as pd


pytrends = TrendReq(hl='en-US', tz=360)
pantone_colors = ['Viva Magenta', 'Classic Blue', 'Living Coral', 'Ultra Violet', 'Greenery']
data = pd.DataFrame()

for color in pantone_colors:
    pytrends.build_payload([color], timeframe='2015-2023')
    trends = pytrends.interest_over_time()
    if not trends.empty:
        data[color] = trends[color]

# Save to CSV for future analysis
data.to_csv('pantone_trends.csv')
plt.figure(figsize=(12, 6))
for color in pantone_colors:
    plt.plot(data.index, data[color], label=color)

plt.title('Google Search Trends for Pantone Colors of the Year')
plt.xlabel('Date')
plt.ylabel('Search Interest')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
