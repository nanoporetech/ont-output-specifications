Fast5 Outputs
=============

!!! Warning
    This file format is deprecated.

FAST5 files are Hierarchical Data Format 5 files, with specific layout for Nanopore data. They are superseded by [Pod5](./pod5.md).

Paths
-----

The following path patterns are used to place the data on disk:

File           | Path Pattern
-------------- | ------------
**Fast5 File** | ``{{spec_value("experiment_layout", "protocol_spec.contents.fast5.path")}}``

See the [Patterns](../patterns.md) documentation for more information on file patterns.

Read Batching
-------------

The following batching options are used by default:


Option         | Value
-------------- | -----
**Read Count** | ``{{spec_value("experiment_layout", "protocol_spec.contents.fast5.batching.read_count")}}``

For more information on batching see [Batching](../batching.md).
