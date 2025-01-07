.. raw:: html

    <style> .red {color:red} </style>

.. role:: red

MinKNOW
=======

MinKNOW supports outputting reads as either raw or basecalled data. The following sections describe the different formats and how to use them.

Raw Output Formats
------------------

===================================  =========  =======  ==========
Format                               Supported  Default  Deprecated
===================================  =========  =======  ==========
:doc:`Pod5<../read_formats/pod5>`    ✓          ✓        ✗
:doc:`Fast5<../read_formats/fast5>`  ✓          ✗        :red:`✓`
===================================  =========  =======  ==========


Basecalled Output Formats
-------------------------


===================================  =========  =======  ==========
Format                               Supported  Default  Deprecated
===================================  =========  =======  ==========
:doc:`Bam<../read_formats/bam>`      ✓          ✗        ✗
:doc:`Fastq<../read_formats/fastq>`  ✓          ✓        ✗
===================================  =========  =======  ==========

Other data formats
------------------

These formats are output by MinKNOW by default, and are not configurable.

=============================================  =========
Format                                         Supported
=============================================  =========
:doc:`../protocol_formats/sequencing_summary`  ✓
:doc:`../protocol_formats/final_summary`       ✓
=============================================  =========
