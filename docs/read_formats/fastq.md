Fastq Output
============

**Format Version:** {{spec_value("fastq", "file.version")}}

[Fastq](https://en.wikipedia.org/wiki/FASTQ_format) is a text-based format for storing both a biological sequence (usually nucleotide sequence) and its corresponding quality scores.

Paths
-----

The following path patterns are used to place the data on disk:


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

Record Structure
----------------

ONT fastq records contain a key value section after then required unique read id. This should be treated as an unordered set of values.

The approximate structure of a record is:

```
@<read-id>(\s<key>=<value>)*
ATCG...
+
QQQQ...
```

For example:

```
@bd8655fb-383c-45cc-bff3-eb1dc86533e0 key1=value1 key2=value2
ATCG
+
QQQQ
```

Attributes included in the key value section are listed below.

Required Header Attributes
--------------------------

::: fastq_spec_docs header


Header Patterns
---------------

Additional header patterns are available for fastq files on top of the normal [Patterns](../patterns.md).

{{ make_table_from_mapping("Name", "Value", spec_value("experiment_layout", "protocol_spec.contents.fastq.extra_patterns")) }}
