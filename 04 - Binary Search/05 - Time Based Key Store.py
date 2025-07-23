#!usr/bin/python

import math


class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        try:
            self.map[key][0].append(value)
            self.map[key][1].append(timestamp)

        except KeyError:
            self.map[key] = [[value], [timestamp]]

    def get(self, key: str, timestamp: int) -> str:

        try:
            timestamps = self.map[key][1]

        except KeyError:
            return ""

        left = 0
        right = len(timestamps) - 1
        half = math.floor((left + right) / 2)

        if timestamp < timestamps[left]:
            return ""

        while right - left > 1:

            if timestamps[left] == timestamp:
                return self.map[key][0][left]

            if timestamps[right] == timestamp:
                return self.map[key][0][right]

            if timestamps[half] == timestamp:
                return self.map[key][0][half]

            if timestamps[half] < timestamp:
                left = half

            else:
                right = half

            half = math.floor((left + right) / 2)

        if timestamps[right] <= timestamp:
            return self.map[key][0][right]

        else:
            return self.map[key][0][left]
