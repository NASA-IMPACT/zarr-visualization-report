# Future Areas

At this time, we plan to develop the tile server approach in the following areas:

* Implement caching at the application level with zarr metadata caching.
* Implement caching at the API level with CloudFront.
* Make consolidated metadata optional and benchmark the difference between consolidated and non-consolidated metadata.

At this time, the following areas of research and development are of interest but unplanned:

* Exacting guidelines on when to create pyramids. For example, if your dataset is  `x` chunk shape/size, and you expect `y` performance, you should or should nnot create `z` levels of pyramid.
* Understand the impact of latency and caching for layers of AWS services. We expect there may be some caching in the S3 service but have not tested or verified this.
* There is latency introduced with the API Gateway and Lambda services. It may be helpful to estimate the latency for these layers and different expected dataset configurations.
