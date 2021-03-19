from matplotlib import pyplot as plt
import csv
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("inp")
args = parser.parse_args()

with open(args.inp) as f:
    reader = csv.reader(f)
    data = list(reader)

side_sizes = [row[0] for row in data[1:]]
series_labels = zip(data[0][1:], ['g', 'b', 'r', 'k', 'y'])
data = [[float(el) for el in row[1:]] for row in data[1:]]
data = np.array(data)

plt.figure()
for i, label in enumerate(series_labels):
    plt.plot(side_sizes, data[:, i], f'{label[1]}-', label=label[0])
plt.legend(loc="upper left")
plt.title("Running time VS Field side size for different number of processes")
plt.xlabel("Field side size")
plt.ylabel("Running time")
plt.show()
