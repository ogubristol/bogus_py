from dataclasses import dataclass


@dataclass(frozen=True)
class Schimm2Hvalues:
    B5 = [
        -9.1,  # C16 alkane
        -121.2,
        -52,
        -56.3,
        -177.6,
        -181.6,
        -68.2,
        -67.2,
        -29.7,
        -258.9,
        -45.9,
        -205.2,
        -36.8,
        -162.6,
        -41.5  # C30 alkane
        ]

    F8 = [
        -231.2,  # C14 methyl ester
        -231.2,
        -166.8,
        -211.0,
        -206.2,
        -214.2,
        -166.7,
        -195.5  # C20 ethyl ester
        ]
