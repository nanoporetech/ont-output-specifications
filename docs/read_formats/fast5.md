.fast5 Outputs
=============

!!! warning
    This file format is deprecated.

ONT .fast5 files are Hierarchical Data Format 5 files, with specific layout for Nanopore data. They are superseded by [POD5](./pod5.md).

Paths
-----

The following path patterns are used to place the data on disk:

File           | Path Pattern
-------------- | ------------
**.fast5 File** | ``{{spec_value("experiment_layout", "protocol_spec.contents.fast5.path")}}``

See the [Patterns](../minknow/patterns.md) documentation for more information on file patterns.

Read Batching
-------------

The following batching options are used by default:


Option         | Value
-------------- | -----
**Read Count** | ``{{spec_value("experiment_layout", "protocol_spec.contents.fast5.batching.read_count")}}``

For more information on batching see [Batching](../minknow/batching.md).
