POD5 Outputs
============

POD5 is Oxford Nanopore Technology's raw read format, based on [Apache Arrow](https://github.com/apache/arrow). Its specification is part of the  [repository which implements the format](https://github.com/nanoporetech/pod5-file-format). You can also find documentation for the format [here](https://pod5-file-format.readthedocs.io/).

Specification
-------------

The POD5 file format is [documented here](https://pod5-file-format.readthedocs.io/en/latest/SPECIFICATION.html).

Paths
-----

The following path patterns are used to place the data on disk:

File           | Path Pattern
-------------- | ------------
**POD5 File** | ``{{spec_value("experiment_layout", "protocol_spec.contents.pod5.path")}}``

See the [Patterns](../minknow/patterns.md) documentation for more information on file patterns.

Read Batching
-------------

The following batching options are used by default:


Option         | Value
-------------- | -----
**Duration**   | ``{{spec_value("experiment_layout", "protocol_spec.contents.pod5.batching.duration")}}``
**Bases**      | ``{{spec_value("experiment_layout", "protocol_spec.contents.pod5.batching.bases")}} Bases``

For more information on batching see [Batching](../minknow/batching.md).

Minimum Version
---------------

The minimum version POD5 files are expected to be written is ``{{spec_value("pod5", "file.minimum_version")}}``.
