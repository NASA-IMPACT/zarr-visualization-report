# Results + Recommendations

## Data Format

* **Data Format:** At this time, COG + pgSTAC tiling performs better than tiling Zarr or kerchunk references, at all zoom levels.
* **Kerchunk Reference Files:** The performance of tiling using a kerchunk reference can be as good or better than a zarr store. It is important to consider this is when the NetCDF files' chunks are the same as the zarr store version. 

## Zarr-specific Recommendations

* **Ensure no zarr coordinate chunking:** Ensure coordinate data is not being chunked. If coordinates are being chunked, it will result in more files being opened during xarray.open_dataset and cause significant performance degradation.
* **Smaller chunk sizes perform better:** Chunk size significantly impacts performance.
* **Fewer spatial chunks perform better:** A greater number of chunks, spatially, will impact performance especially at low zoom levels as more chunks are loaded for greater spatial coverage.
* **Pyramids improve performance for high resolution datasets:** High resolution datasets will suffer having either large chunks or many chunks, or both. To provide a good experience, zarr data can be aggregated into multiscale datasets, otherwise known as pyramids.

