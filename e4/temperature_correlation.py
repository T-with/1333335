import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def distance(city, stations):
    R = 6371000
    lat1 = np.radians(city['latitude'])
    lon1 = np.radians(city['longitude'])
    lat2 = np.radians(stations['latitude'])
    lon2 = np.radians(stations['longitude'])
 
    dlat = lat2 - lat1
    dlon = lon2 - lon1
 
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    return R * c


def best_tmax(city, stations):
    dists = distance(city, stations)
    return stations['avg_tmax'].iloc[dists.argmin()]

def main():
    stations_file = sys.argv[1]
    city_file = sys.argv[2]
    output_file = sys.argv[3]
 
    stations = pd.read_json(stations_file, lines=True)
    stations['avg_tmax'] = stations['avg_tmax'] / 10
 
    city = pd.read_csv(city_file)
    city = city.dropna(subset=['area', 'population']).copy()
    city['area'] = city['area'] / 1e6
    city = city[city['area'] <= 10000]
    city['density'] = city['population'] / city['area']
 
    city['avg_tmax'] = city.apply(best_tmax, stations=stations, axis=1)
 
    plt.figure(figsize=(10, 5))
    plt.plot(city['density'], city['avg_tmax'], 'b.', alpha=0.5)
    plt.xlabel('Population Density (people/km\u00b2)')
    plt.ylabel('Avg Max Temperature (\u00b0C)')
    plt.title('Temperature vs Population Density')
    plt.savefig(output_file)

main()