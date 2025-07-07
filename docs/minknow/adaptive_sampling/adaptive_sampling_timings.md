Adaptive Sampling Timings CSV
===

**Format version:** {{spec_value("adaptive_sampling/timings_spec", "file.version")}}

This CSV file records the real-time data that the Adaptive Sampling process used in its decision making.

Paths
-----

The following path patterns are used to place the data on disk:


File           | Path pattern
-------------- | ------------
**AS Timings file** | ``{{spec_value("experiment_layout", "protocol_spec.contents.adaptive_sampling_timings.path")}}``

See the [Patterns](../../minknow/patterns.md) documentation for more information on file patterns.

Columns
-------

::: csv_spec_docs adaptive_sampling/timings_spec
