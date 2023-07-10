"""Calculates the bit rate."""
import numpy as np


def bit_rate(data, step_sec=0.1):
    data["time"] -= data.iloc[0]["time"]
    start = data.iloc[0]["time"]
    finish = data.iloc[-1]["time"]

    step = finish / step_sec
    finish = start + step_sec
    value = []

    for i in range(int(step)):

        # From Byte to bit - selection of the time interval between the start and the end of a single time slot
        val = np.sum(data[(data["time"] >= start) & (data["time"] < finish)]["length"] * 8)
        if not np.isnan(val):
            value.append(val / step_sec)
        start = finish
        finish = start + step_sec

    return value
