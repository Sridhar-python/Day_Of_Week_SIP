import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import yfinance as yf

# --- Data Download ---
start = '2010-01-01'
end = '2024-10-17'
stock = '^NSEI'
df = yf.download(stock, start, end, auto_adjust=True)

df['Day_of_Week'] = df.index.day_name()
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day_counts = df.groupby('Day_of_Week').size().reindex(day_order)
lowest_day = day_counts.idxmin()

# --- Plotting ---
plt.figure(figsize=(10, 6))
day_counts.plot(kind='barh', color=sns.color_palette('Dark2'))
plt.gca().spines[['top', 'right']].set_visible(False)

plt.title('Frequency of Stock Data for ^NSEI by Day of the Week')
plt.xlabel('Frequency (Trading Days)')
plt.ylabel('Day of the Week')

# Highlight the lowest day

y_pos = day_counts.index.get_loc(lowest_day) 
plt.annotate(f'Lowest: {lowest_day}',
             xy=(day_counts.min(), y_pos),
             xytext=(day_counts.min() + 20, y_pos - 0.1), 
             arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
             fontsize=12,
             ha='left',
             va='center')

plt.tight_layout()
plt.show()

print(f"The day of the week in the low range is: {lowest_day}")