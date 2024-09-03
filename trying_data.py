import music21 as m21
import os

PIANO_DATAPATH = "Dataset"

with open("single_file_dataset.txt", "r") as fp:
    count = 0
    for line in fp:
        for word in line:
            count += 1

