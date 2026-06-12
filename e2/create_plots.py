import sys
import pandas as pd
import matplotlib.pyplot as plt

filename1 = sys.argv[1]
filename2 = sys.argv[2]

data1 = pd.read_csv(filename1, sep=' ', header=None, index_col=1,
                    names=['lang', 'page', 'views', 'bytes'])
data2 = pd.read_csv(filename2, sep=' ', header=None, index_col=1,
                    names=['lang', 'page', 'views', 'bytes'])

sorted_views = data1['views'].sort_values(ascending=False)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(sorted_views.values)
plt.title('Popularity Distribution')
plt.xlabel('Rank')
plt.ylabel('Views')

combined = pd.DataFrame({
    'hour1': data1['views'],
    'hour2': data2['views']
})
plt.subplot(1, 2, 2)
plt.plot(combined['hour1'], combined['hour2'], 'b.')
plt.title('Hourly Correlation')
plt.xlabel('Hour 1 views')
plt.ylabel('Hour 2 views')
plt.xscale('log')
plt.yscale('log')

plt.savefig('wikipedia.png')