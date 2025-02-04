Batching
========

Output from ONT products can be batched in various ways, depending on the software used to generate the files.

MinKNOW Configuration
---------------------

### UI

The UI for MinKNOW allows configuring the batching for bam and fastq based on "Time elapsed" and "Read count".

### Default values

The `default_writer.toml` file in ``<minknow_install_dir>/conf/package/shared/default_writer.toml``
contains default batching parameters, and allows additional control on top of what the UI provides.

#### File format configuration locations

In the ``default_writer.toml`` config file batching for pod5 and fast5 can be controlled:

File Type | Config Location
--------- | ---------------
Pod5      | ``[writer_configuration.read_pod5]``
Fast5     | ``[writer_configuration.read_fast5]``


#### Batching Examples

The following examples can be used to replace existing batching options for a file format, to change how a file type is batched.

##### Batch based on read count

```
batch_duration = "0s"               # Time based batching disabled
batch_count = 4000                  # How many reads in each file
```

##### Batch into hourly files, or 500 million bases, whichever comes first

```
batch_duration = "3600s"            # Time based batch duration
bases_per_batch = 500_000_000       # Batch based on estimated base output
```

##### Batch into hourly files

```
batch_duration = "3600s"            # Time based batch duration
no_output_based_batching = {}       # Disable output based batching
```

##### Batch into 1 giga base files

```
bases_per_batch = 1_000_000_000     # Batch based on estimated base output
```
