MinKNOW
=======

MinKNOW supports outputting reads as either raw or basecalled data. The following sections describe the different formats and how to use them.

Raw output formats
------------------

Format                              | Supported                                | Default | Generation time
----------------------------------- | ---------------------------------------- | ------- | ---------------
[POD5](../read_formats/pod5.md)     | ✓                                        | ✓       | As batch is filled, during acquisition and basecalling catchup
[.fast5](../read_formats/fast5.md)   | <span>✓</span> {{warning("Deprecated")}} | ✗       | As batch is filled, during acquisition and basecalling catchup


Basecalled output formats
-------------------------


Format                              | Supported | Default | Generation time
----------------------------------- | --------- | ------- | ---------------
[BAM](../read_formats/bam.md)       | ✓         | ✗       | As batch is filled, during acquisition and basecalling catchup
[FASTQ](../read_formats/fastq.md)   | ✓         | ✓       | As batch is filled, during acquisition and basecalling catchup

Other data formats
------------------

These formats are output by MinKNOW by default, and are not configurable.

Format                                                          | Generation time
--------------------------------------------------------------- | ---------------
[Sequencing Summary](../protocol_formats/sequencing_summary.md) | End of sequencing acquisition and basecalling catchup period.
[Sample Sheet](../protocol_formats/sample_sheet.md)             | Beginning of sequencing run.
[Output Hash File](../../protocol_formats/output_hash_file)     | Once hashed files have been written for the sequencing run.
Final Summary                                                   | Once all files have been written for the sequencing run.
Barcode Alignment Report                                        | End of sequencing acquisition and basecalling catchup period.
