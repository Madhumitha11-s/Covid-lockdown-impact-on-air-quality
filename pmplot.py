
import shapefile as shp  # Requires the pyshp package
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from netCDF4 import date2index
import os


#open shape file for MMR Region
sf = shp.Reader(r"C:\Users\madhu\Documents\MTech_Project\Plot_Py\MMRDA\MMRDA_Manual.shp")

#Open satellite nc data
path = r"C:\Users\madhu\Documents\MTech_Project\Plot_Py\NO2\TROPOMI-inferred_surface_no2_asia_202001_monthly_mean.nc"
ds = xr.open_dataset(path)


fig = plt.figure(figsize=(8,6))


#Subset the MMR region from rest of the area
lat_bnds, lon_bnds =  [18.26005, 19.557455], [72.548323,73.702996]
# lat_bnds, lon_bnds = [18.121996, 19.910110], [72.827503, 73.494505]
data = ds.sel(lat=slice(*lat_bnds), lon=slice(*lon_bnds))


# plt.style.use('seaborn-dark-palette')
data.GWRPM25.plot(vmin=15, vmax=65, cmap ='turbo')


#Override shape file over the exisiting plot
for shape in sf.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.plot(x,y, color="white")

# plt.title('Data:', str(os.path.basename(path)))

plt.show()

print("runned")
