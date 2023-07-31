# Performance Methodology

## Datasets

Reproducibility is important to the integrity of this project and its reported results. That is why we selected a publicly available dataset and attempt to make the steps as fully documented and reproducible as possible. We used the [NASA Earth Exchange Global Daily Downscaled Projections (NEX-GDDP-CMIP6)](https://aws.amazon.com/marketplace/pp/prodview-k6adk576fiwmm#overview) AWS public dataset for this project.

There are 2 datasets listed on AWS: 1 is an archive of NetCDF files from about 35 different climate models, each supplying historical and predicted values for up to 9 environment variables, daily, from 1950 to 2100. To minimize preprocessing, test datasets were generated for the first 2 years of historical data, for 1 model and for 1 variable. These variables or dataset could easily be modified or swapped, but we expect the relative performance using different datasets to be the same. 

In addition to the NetCDF data, there is an archives of COGs generated from that NetCDF data to support visualization via dynamic tiling using COGs.  COGs are only available for 2 models, so for inter comparison of the tiling approach between COGs and Zarr, one of those models (`GISS-E2-1-G`) is used to generate Zarr stores.

At this time, a different model is used for the direct client approach (`ACCESS-CM2`), but we will demonstrate how there is no meaningful difference in the performance of tiling across these models.

Benchmarks for the tiling approach were run on the [VEDA JupyterHub](https://nasa-veda.2i2c.cloud/). The VEDA documentation details how to request access: https://nasa-impact.github.io/veda-docs/services/jupyterhub.html. Because we don't want to make the database or S3 bucket with datasets fully public, you must be logged into the VEDA JupyterHub to run those benchmarks.

## Performance Testing Methodology

### code profiling

### e2e testing
