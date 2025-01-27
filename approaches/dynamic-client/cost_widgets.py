"""Utilities for estimating storage costs of pyramids."""

import numpy as np
import panel as pn


def calculate_level_size(*, level, pixels_per_tile, extra_dimension_length, data_dtype):
    """
    Calculate the uncompressed size for a given zoom level in GB.

    Parameters
    ----------
    level : int
        Zoom level.
    pixels_per_tile : int
        Scale of each tile (commonly 128, 256, or 512).
    extra_dimension_length : int
        Length of the non-spatial dimension.
    data_dtype : np.dtype
        Numpy dtype, expected to contain an .itemsize property.

    Returns
    -------
    int
        Uncompressed size of the given zoom level in GB.
    """
    data_size = (
        (pixels_per_tile * 2**level) ** 2
        * extra_dimension_length
        * data_dtype.itemsize
        * 1e-9
    )
    spatial_coords_size = (pixels_per_tile * 2**level * 2) * data_dtype.itemsize * 1e-9
    extra_coords_size = extra_dimension_length * data_dtype.itemsize * 1e-9
    return data_size + spatial_coords_size + extra_coords_size


def calculate_pyramid_cost(
    *,
    number_of_zoom_levels,
    pixels_per_tile,
    extra_dimension_length,
    data_dtype,
    data_compression_ratio,
    price_per_GB,
):
    """
    Calculated the expected cost of storing the overviews.

    Parameters
    ----------
    number_of_zoom_levels : int
        Number of zoom levels for the specific dataset.
    pixels_per_tile : int
        Scale of each tile (commonly 128, 256, or 512).
    extra_dimension_length : int
        Length of the non-spatial dimension.
    data_dtype : np.dtype
        Numpy dtype, expected to contain an .itemsize property.
    data_compression_ratio : float
        Expected ratio between compressed and uncompressed data.
    price_per_GB : float
        Expected storage cost per GB.

    Returns
    -------
    float
        Expected cost of storing the overviews in $.
    """
    data_dtype = np.dtype(data_dtype)
    pyramid_size = 0
    for level in range(number_of_zoom_levels):
        pyramid_level_size = calculate_level_size(
            level=level,
            pixels_per_tile=pixels_per_tile,
            extra_dimension_length=extra_dimension_length,
            data_dtype=data_dtype,
        )
        pyramid_size += pyramid_level_size
    pyramid_cost = pyramid_size / data_compression_ratio * price_per_GB
    return f"Pyramid cost: ${pyramid_cost:.2f}/month"


# Define widgets for panel app
extra_dim_widget = pn.widgets.IntSlider(
    name="Time dimension length", start=365, end=18250, step=9125, value=365
)
pixels_widget = pn.widgets.DiscreteSlider(
    name="Pixels per tile", options=[128, 256, 512], value=128
)
zoom_level_widget = pn.widgets.IntSlider(
    name="Number of zoom levels", start=1, end=4, step=1, value=2
)
compression_widget = pn.widgets.IntSlider(
    name="Data compression ratio", start=5, end=9, step=2, value=7
)
dtype_widget = pn.widgets.Select(
    name="Data type", options=["float16", "float32", "float64"], value="float32"
)
price_widget = pn.widgets.FloatSlider(
    name="Average storage pricing ($ per GB per month)",
    start=0.02,
    end=0.025,
    step=0.005,
    value=0.02,
)
