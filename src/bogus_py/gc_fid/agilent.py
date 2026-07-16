import pandas as pd
import rainbow as rb
from datetime import datetime as dt

def create_chrom_df(data_directory: str):
    parsed_directory = rb.read(data_directory)
    chromatography_file = parsed_directory.get_file("FID1A.ch")

    file_info = chromatography_file.metadata
    unit = file_info["unit"]

    chrom_df = pd.DataFrame({"retention_time_min": chromatography_file.xlabels,
                             f"response_{unit}": chromatography_file.data[:, 0]})

    chrom_df.loc[:, "sample_id"] = file_info["notebook"]
    chrom_df.loc[:, "sample_starttime"] = dt.strptime(file_info["date"], r"%d-%b-%y, %H:%M:%S")
    chrom_df.loc[:, "sample_method"] = file_info["method"]

    return chrom_df