# Divided at the Edge - Measuring Performance and the Digital Divide of Cloud Edge Data Centers

See RIPEAtlasGraphs.ipynb for steps to generate graphs in the paper from the RIPE Atlas measurement results, DigitalDivideGraphs.ipynb for steps to generate graphs related to the cloud digital divide, and StarlinkGraphs.ipynb for graphs related to our LEO satellite analysis.

# Data

## Ripe Atlas

Necessary data is downloaded using the RIPE Atlas API from the jupyter notebook, no additional downloads are necessary.

## Digital Divide

- Gridded population of the world from [SEDAC](https://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-count-rev11) year 2020 at 15 arc-minute resolution. Download the file `gpw_v4_population_count_rev11_2020_15_min.tif` and place it in the `data` folder.
- [ESRI Updated Demographics](https://doc.arcgis.com/en/esri-demographics/latest/regional-data/updated-demographics.htm) downloading using [ArcGIS Online](https://www.arcgis.com/index.html). The census tract level is used, files should be placed in `data/ACS_Median_Household_Income_Variables_-_Boundaries/Tract_2.csv` and `data/ACS_Population_Variables_-_Boundaries/Tract_2.csv`
- GADM Administrative level 2 for the world, downloaded [here](https://www.gadm.org/data.html). The file should be placed in `data/gadm_410-levels.gpkg`.
- Annual VNL v2.1 for 2020 from [here](https://eogdata.mines.edu/nighttime_light/annual/v21/). This should be placed in `data/VNL_v21_npp_2020_global_vcmslcfg_c202205302300.median_masked.dat.tif`.

## Satellite

Results of the LEO satellite simulations can be downloaded from https://drive.google.com/file/d/1z8WjIIT0T20dIgsStQxCBc1bEgvcj65z/view This should be placed in the data/starlink_simulator directory
