Sample Sheet
============

Sample sheets are used in multiple ways inside MinKNOW, either as a way to configure a sequencing run, or as a document of the configuration of the sequencing run.


Output Columns
--------------

The following fields document fields MinKNOW will write at the end of a sequencing run.

::: csv_spec_docs sample_sheet


Input Columns
-------------

When passing a sample sheet into MinKNOW, different rules apply to the columns - not all are required.

Column                     | Notes
-------------------------- | ------
``flow_cell_id``           | **Optional** if ``position_id`` is specified and the flow cell has ``flow_cell_id`` on the EEPROM. Used to identify which position to apply values to.
``position_id``            | **Optional** if ``flow_cell_id`` is specified. Used to identify which position to apply values to.
``sample_id``              | **Optional.** An individual position can only have one sample_id assigned to it when starting a run.
``experiment_id``          | Each row in the sample sheet must contain an experiment_id.
``flow_cell_product_code`` | **Required** if the product code is not available on the EEPROM. Used to find the correct protocol to start.
``kit``                    | **Required** Kit is used to find a protocol to start.

### Notes

If ``position_id`` and ``flow_cell_id`` are both defined, the ``flow_cell_id`` will be validated against the EEPROM value. The ``flow_cell_id`` will be set against the ``user_specified_flow_cell_id`` when starting a protocol.

All rows must contain the same ``experiment_id`` value, therefore, the sample sheet will only have a single ``experiment_id`` defined overall but the entries on each row are validated.

If expansions kits are additionally defined they should be space separated, e.g., ``SQK-LSK109 EXP-NBD104 EXP-NBD114`` or ``OND-SQK-LP0096S``. The sample sheet must contain exactly one sequencing kit, but can contain 0, 1, or many, expansion kits. The sequencing kit must be specified before any expansion kits.
