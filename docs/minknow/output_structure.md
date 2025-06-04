Output Structure
================

MinKNOW organises all artifacts produced during a sequencing protocol under a single base output directory
chosen when the run is started.

Data pooling         | Base output path pattern | Example
-------------------- | ------------------------ | ----------------------
Disabled *(default)* | ``{{spec_value("experiment_layout", "protocol_spec.root.no_pooling.pattern")}}``          | ``{{spec_value("experiment_layout", "protocol_spec.root.no_pooling.example")}}``
Enabled              | ``{{spec_value("experiment_layout", "protocol_spec.root.pooling.pattern")}}`` | ``{{spec_value("experiment_layout", "protocol_spec.root.pooling.example")}}``

*The content in curly braces is replaced at sequencing run start with the value from [patterns](../patterns).*

##  Read output

Inside the base output directory MinKNOW creates format‑specific sub‑directories:


Format                             | Sub‑directories
---------------------------------- | -------------
[POD5](../../read_formats/pod5/)   | ``pod5/`` & ``pod5_skip``
[FASTQ](../../read_formats/fastq/) | ``fastq_pass/`` & ``fastq_fail/``
[BAM](../../read_formats/bam/)     | ``bam_pass/`` & ``bam_fail/``
[.fast5](../../read_formats/pod5/) *(deprecated)* | ``fast5_pass/``, ``fast5_fail/`` & ``fast5_skip/``

See more about specific [format support](../support).

## Report & summary output

Additional sequencing artifacts are written directly to the base protocol path:

Type | Path
---- | -----
HTML Report | ``{{spec_value("experiment_layout", "protocol_spec.contents.html_report.path")}}``
[Sequencing Summary](../../protocol_formats/sequencing_summary) | ``{{spec_value("experiment_layout", "protocol_spec.contents.sequencing_summary.path")}}``
[Output Hash File](../../protocol_formats/output_hash_file) | ``{{spec_value("experiment_layout", "protocol_spec.contents.output_hash_file.path")}}``
[Sample Sheet](../../protocol_formats/sample_sheet) | ``{{spec_value("experiment_layout", "protocol_spec.contents.sample_sheet.path")}}``
Final Summary | ``{{spec_value("experiment_layout", "protocol_spec.contents.final_summary.path")}}``
Barcode Alignment Report | ``{{spec_value("experiment_layout", "protocol_spec.contents.barcode_alignment_report.path")}}``

## Example directory tree

This example describes an sequencing run with pooling disabled, and POD5, FASTQ and BAM turned on, which has finished sequencing:

```
/data/Sample_Group/Sample/20250603_1201_3E_PAA12345_e05460c6/
├── pod5/
│   ├── PAA12345_fd97ea7b_0f1d7e9e_57.pod5
│   └── …
├── fastq_pass/
│   ├── PAA12345_pass_dca6f6d1_d11637af_0.fastq.gz
│   └── …
├── fastq_fail/
│   └── …
├── bam_pass/
│   ├── PAA12345_pass_dca6f6d1_d11637af_0.bam
│   └── PAA12345_pass_dca6f6d1_d11637af_0.bam.bai
└── bam_fail/
|   └── …
├── sequencing_summary_PAA12345_fd97ea7b_0f1d7e9e.txt
├── output_hash_PAA12345_fd97ea7b_0f1d7e9e.csv
├── sample_sheet_PAA12345_fd97ea7b_0f1d7e9e.csv
├── final_summary_PAA12345_fd97ea7b_0f1d7e9e.txt
└── barcode_alignment_PAA12345_fd97ea7b_0f1d7e9e.tsv
```
