MinKNOW
=======

MinKNOW supports outputting reads as either raw or basecalled data. The following sections describe the different formats and how to use them.

Raw Output Formats
------------------

Format                              | Supported                                | Default | Generation time
----------------------------------- | ---------------------------------------- | ------- | ---------------
[Pod5](../read_formats/pod5.md)     | ✓                                        | ✓       | As batch is filled, during acquisition and basecalling catchup
[Fast5](../read_formats/fast5.md)   | <span>✓</span> {{warning("Deprecated")}} | ✗       | As batch is filled, during acquisition and basecalling catchup


Basecalled Output Formats
-------------------------


Format                              | Supported | Default | Generation time
----------------------------------- | --------- | ------- | ---------------
[Bam](../read_formats/bam.md)       | ✓         | ✗       | As batch is filled, during acquisition and basecalling catchup
[Fastq](../read_formats/fastq.md)   | ✓         | ✓       | As batch is filled, during acquisition and basecalling catchup

Other data formats
------------------

These formats are output by MinKNOW by default, and are not configurable.

Format                                                          | Generation time
--------------------------------------------------------------- | ---------------
[Sequencing Summary](../protocol_formats/sequencing_summary.md) | End of sequencing acquisition and basecalling catchup period
[Final Summary](../protocol_formats/final_summary.md)           | End of sequencing acquisition and basecalling catchup period
