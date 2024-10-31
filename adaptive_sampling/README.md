# Adaptive Sampling CSV Specification

Adaptive sampling outputs two required and one optional comma separated text files:
1. `AS_timings*.csv` Per-read timings and statistics for basecalled reads
1. `AS_decisions*.csv` Per-read decisions made by adaptive sampling
1. `AS_debug*.csv` *optional* Per-read/event tracing of data throughout the script

The CSV specifications (`*.csvs`) can be validated using the csv-validator: http://digital-preservation.github.io/csv-validator/
We also provide data-dictionaries for each CSV file with information on units and descriptions. See https://ess-dive.gitbook.io/file-level-metadata-reporting-format/csv_dd for more information
