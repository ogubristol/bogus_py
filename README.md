# bogus_py

## Overview

**Welcome to the Bristol Organic Geochemistry Unit System - Python (BOGUS Py for short).**

This is a Python package developed by the Organic Geochemistry Unit to help
process isotope ratio mass spectrometry (IRMS) data. This is done in two ways:

### Data preparation

Our IRMS instruments (particularly the IsoPrime 100) produce horrible proprietary
data files, requiring each run to be opened and the data manually extracted before
we can calculate &delta; values. With the data preparation functions in this package
one should be able to create one long `.csv` or Excel file from a folder full of
data files without any copy-pasting at all!

We currently have data preparation functions for the following instrument files:

- Delta V (`.dxf`)
- Delta XP (`.dxf`)
- IsoPrime 100 (`.raw` folders; these are particularly annoying)

Note that processing of `.dxf` files from the Delta instruments requires an extra
step, see [below](##dxf-pre-processing).

### Data analysis

Once &delta; values have been obtained, we also need to perform corrections like scale
normalisation. We also have functions for that!

## Installation

This package can be installed into a Python environment with `pip`, using
the following command:

```bash
pip install https://github.com/ogubristol/bogus_py.git
```

To submit modifications/additions, please branch and create a merge request. For help
with this, contact Nick Hall.

## DXF Pre-processing

Currently, this package cannot directly handle output files from Thermo IRMS software
(e.g. `.dxf` files).
Handily, the [isoreader](https://isoreader.isoverse.org/index.html) R package has been
developed to handle these files, and can export useful data as easy-to-read `.csv`
files, which this package can then process.

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
