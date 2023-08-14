from pytrends.request import TrendReq
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date

# for styling
sns.set_style("darkgrid")

# initialize a new Google Trends Request Object
kw_list = ["Diablo IV", "Blizzard", "games"]

pytrends = TrendReq(hl='en-US', tz=360)

# pytrends.build_payload(keywords,timeframe='today 12-m')
pytrends.build_payload(kw_list,timeframe=f'2023-06-01 {date.today()}')
trend_data = pytrends.interest_over_time()
series = trend_data[kw_list]
plt.plot(series)
plt.show()

series
