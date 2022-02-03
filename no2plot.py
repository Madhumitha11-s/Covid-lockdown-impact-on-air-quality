
import shapefile as shp  # Requires the pyshp package
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from netCDF4 import date2index

#Open No2 data and MMR shapefile
sf = shp.Reader(r"C:\Users\madhu\Documents\MTech_Project\Plot_Py\MMRDA\MMRDA_Manual.shp")
ds = xr.open_dataset(r"C:\Users\madhu\Documents\MTech_Project\Plot_Py\NO2\TROPOMI-inferred_surface_no2_asia_202002_monthly_mean.nc")

#Squeeze 2D to 1D
lat = np.squeeze(ds.LAT_CENTER)
lon = np.squeeze(ds.LON_CENTER)

#Create new da with existing ds
da = xr.DataArray(data=ds.surface_no2_ppb[:], dims=["lat", "lon"], coords=[lat,lon])


#Subset the required region
# lat_bnds, lon_bnds = [18.26005, 19.557455], [72.548323,73.702996] #MMR
lat_bnds, lon_bnds =  [6.851295, 37.514040], [67.087643, 100.726447] #India
data = da.sel(lat=slice(*lat_bnds), lon=slice(*lon_bnds))


#Ploting the data
fig = plt.figure(figsize=(8, 8))
data.plot(vmin=0, vmax=20, cmap ='turbo')


#Overriding the shape file MMR
for shape in sf.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.plot(x,y, color="black")


#Show the plot    
plt.show()


