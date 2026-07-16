# bogus_py

## Overview

**Welcome to the repository of Bristol Organic Geochemistry Unit Software for Python (BOGUS Py for short).**

This is a Python package developed by the Organic Geochemistry Unit here in
Bristol to help process data, including from isotope ratio mass spectrometry
(IRMS) instruments.

## Installation

This package can be installed into a Python environment with `pip`, using
the following command:

```bash
pip install git+https://github.com/ogubristol/bogus_py.git
```

To submit modifications/additions, please branch and create a merge request. For help
with this, contact Nick Hall.

## GC-FID

This package allows users to read proprietary GC-FID data into `.csv` files
without the need to manually export each run, speeding up the creation of
chromatograms for publication.

## IRMS

### Data preparation

IRMS instruments (particularly the IsoPrime 100) produce challenging proprietary
data files, requiring each run's data to be manually extracted before we can
calculate &delta; values. With the data preparation functions in this package
one should be able to create one long `.csv` or Excel file from a folder full of
data files without any copy-pasting at all!

We currently have data preparation functions for the following instruments:

- Delta V (`.dxf`)
- Delta XP (`.dxf`)
- IsoPrime 100 (`.raw` folders; these are particularly annoying)

Note that processing of `.dxf` files from the Delta instruments requires an extra
step, see [below](#dxf-pre-processing).

### Data analysis

This package also contains resources for IRMS data processing tasks, including

- Locating the relevant isotopic reference material runs for a given sample
- Linear regression of isotopic reference material data
- Normalisation of delta values to reference material data

### DXF Pre-processing

Currently, this package cannot directly handle output files from Thermo IRMS
software (i.e. `.dxf` files). Handily, the
[isoreader](https://isoreader.isoverse.org/index.html) R package has been
developed to handle these files, and can export useful data as easy-to-read
`.csv` files, which this package can then process.

For a directory (folder) containing `.dxf` files, we can create single
`.csv` file containing every run's data as follows:

```R
library(isoreader)

DIR <- "path/to/directory/data"
OUTFILE <- "path/to/directory/all_run_data.csv"

OUTFILE <- paste(DIR, OUTFILE, sep = "")

dxf_files <- list.files(path=DIR, pattern="*.dxf", full.names=TRUE, recursive=FALSE)
file_data <- iso_read_continuous_flow(dxf_files)
output_data <- file_data |> iso_get_vendor_data_table(
    include_file_info=c(file_datetime, starts_with("Identifier"))
    )

write.table(output_data, OUTFILE, sep=",", row.names=FALSE)
```

Where the `.csv` contains the "vendor data" (the per-peak isotope ratio data that you'd
ordinarily copy and paste into an Excel sheet) for each run as well as some extra
information like the date/time the run was started.

This `.csv` is now ready to be processed in Python with this package.
