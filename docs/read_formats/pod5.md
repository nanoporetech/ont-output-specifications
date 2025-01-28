Pod5 Outputs
============

Pod5 is the Nanopore's raw read format, based on [Apache Arrow](https://github.com/apache/arrow). Its specification is part of the  [repository which implements the format](https://github.com/nanoporetech/pod5-file-format). You can also find generated documentation for the format [here](https://pod5-file-format.readthedocs.io/).

Paths
-----

The following path patterns are used to place the data on disk:

File           | Path Pattern
-------------- | ------------
**Pod5 File** | ``{{spec_value("experiment_layout", "protocol_spec.contents.pod5.path")}}``

See the [Patterns](../patterns.md) documentation for more information on file patterns.

Read Batching
-------------

The following batching options are used by default:


Option         | Value
-------------- | -----
**Duration**   | ``{{spec_value("experiment_layout", "protocol_spec.contents.pod5.batching.duration")}}``
**Bases**      | ``{{spec_value("experiment_layout", "protocol_spec.contents.pod5.batching.bases")}} Bases``

For more information on batching see [Batching](../batching.md).

Minimum Version
---------------

The minimum version pod5 files are expected to be written is ``{{spec_value("pod5", "file.minimum_version")}}``.
