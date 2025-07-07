Adaptive Sampling Decisions CSV
===

**Format version:** {{spec_value("adaptive_sampling/decisions_spec", "file.version")}}

This CSV file records the decisions &mdash; whether a read was sequenced completely or unblocked &mdash; made by the live Adaptive Sampling process.
There may be duplicated read IDs in this file due to the asynchronous implementation of the script.

Paths
-----

The following path patterns are used to place the data on disk:


File           | Path pattern
-------------- | ------------
**AS Decisions file** | ``{{spec_value("experiment_layout", "protocol_spec.contents.adaptive_sampling_decisions.path")}}``

See the [Patterns](../../minknow/patterns.md) documentation for more information on file patterns.

Columns
-------

::: csv_spec_docs adaptive_sampling/decisions_spec
