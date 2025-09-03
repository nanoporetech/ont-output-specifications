POD5 Outputs
============

POD5 is Oxford Nanopore Technologies raw read format, based on [Apache Arrow](https://github.com/apache/arrow). Its specification is part of the  [repository which implements the format](https://github.com/nanoporetech/pod5-file-format). You can also find documentation for the format [here](https://pod5-file-format.readthedocs.io/).

Specification
-------------

The POD5 file format is [documented here](https://pod5-file-format.readthedocs.io/en/latest/SPECIFICATION.html).

Paths
-----

The following path patterns are used to place the data on disk.

File Path                | Path pattern
------------------------ | ------------
**POD5 Default**         | ``{{spec_value("experiment_layout", "protocol_spec.contents.pod5.path")}}``
Split by barcode Enabled | ``{{spec_value("experiment_layout", "protocol_spec.contents.pod5.path_split_by_barcode")}}``

*Note the pattern used is different when the option to split files by barcode is enabled.*

See the [Patterns](../minknow/patterns.md) documentation for more information on file patterns.

Read batching
-------------

The following batching options are used by default:


Option         | Value
-------------- | -----
**Duration**   | ``{{spec_value("experiment_layout", "protocol_spec.contents.pod5.batching.duration")}}``
**Bases**      | ``{{spec_value("experiment_layout", "protocol_spec.contents.pod5.batching.bases")}} Bases``

For more information on batching see [Batching](../minknow/batching.md).

Minimum version
---------------

The minimum version POD5 files are expected to be written is ``{{spec_value("pod5", "file.minimum_version")}}``.
