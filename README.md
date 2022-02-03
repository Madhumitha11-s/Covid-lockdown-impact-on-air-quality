# Covid-lockdown-impact-on-air-quality
Analysis on Satellite and ground-based measurements


Open a virtual environment and run the following terminal command `pip install -r requirements.txt`<br />



Open pmplot.py and change the path to `path = r"C:\Users\**\Plot_Py\PM25\V5GL02.HybridPM25c_0p10.Asia.202009-202009.nc"`,
and `sf = shp.Reader(r"C:\Users\**\Plot_Py\MMRDA\MMRDA_Manual.shp")` to your current working directory.

To obtain the plot for MMR region run: `python pmplot.py`<br />

Output:
For entire dataset:
![V5GL02 HybridPM25 Asia 202001-202012](https://user-images.githubusercontent.com/79834018/152342049-dfb9ecc3-83a8-4609-ab1f-4f37f9c65515.png)

For subset over MMR region:
![PM25 Asia 201701-201712](https://user-images.githubusercontent.com/79834018/152342108-c25e6566-56de-4b7f-bcf0-95dd33725128.png)
