Output Hash File
================

The output hash file is csv file, containing one row per output minknow file. It is intended to confirm integrity of the written output data.

Paths
-----

The following path patterns are used to place the data on disk:

File           | Path Pattern
-------------- | ------------
**Output Hash File** | ``{{spec_value("experiment_layout", "protocol_spec.contents.output_hash_file.path")}}``

See the [Patterns](../minknow/patterns.md) documentation for more information on file patterns.

Columns
-------

::: csv_spec_docs output_hash_file
