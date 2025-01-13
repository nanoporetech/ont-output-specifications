MinKNOW
=======

MinKNOW supports outputting reads as either raw or basecalled data. The following sections describe the different formats and how to use them.

Raw Output Formats
------------------

Format                              | Supported | Default | Deprecated
----------------------------------- | --------- | ------- | ----------
[Pod5](../read_formats/pod5.md)     | ✓         | ✓       | ✗
[Fast5](../read_formats/fast5.md)   | ✓         | ✗       | <span style="color:red">✓</span>


Basecalled Output Formats
-------------------------


Format                              | Supported | Default | Deprecated
----------------------------------- | --------- | ------- | ----------
[Bam](../read_formats/bam.md)       | ✓         | ✗      | ✗
[Fastq](../read_formats/fastq.md)   | ✓         | ✓      | ✗

Other data formats
------------------

These formats are output by MinKNOW by default, and are not configurable.

Format                                                          | Supported
--------------------------------------------------------------- | ---------
[Sequencing Summary](../protocol_formats/sequencing_summary.md) | ✓
[Final Summary](../protocol_formats/final_summary.md)           | ✓
