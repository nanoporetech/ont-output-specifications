Fastq Output
============

**Format Version:** {{spec_value("fastq", "file.version")}}

[Fastq](https://en.wikipedia.org/wiki/FASTQ_format) is a text-based format for storing both a biological sequence (usually nucleotide sequence) and its corresponding quality scores.

Paths
-----

The following path patterns are used by place reads:


File           | Path Pattern
-------------- | ------------
**Fastq File** | ``{{spec_value("experiment_layout", "protocol_spec.contents.fastq.path")}}``

See the [Patterns](../patterns.md) documentation for more information on file patterns.

Read Batching
-------------

The following batching options are used by default:


Option       | Value
------------ | -----
**Duration** | ``{{spec_value("experiment_layout", "protocol_spec.contents.fastq.batching.duration")}}``

For more information on batching see [Batching](../batching.md).


Header Patterns
---------------

Additional header patterns are available for fastq files on top of the normal [Patterns](../patterns.md).

{{ make_table_from_mapping("Name", "Value", spec_value("experiment_layout", "protocol_spec.contents.fastq.available_patterns")) }}

Required Header Attributes
--------------------------

::: fastq_spec_docs header
