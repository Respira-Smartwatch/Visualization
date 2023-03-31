# Author: Max Roesler
# Author: Joseph Bellahcen

import argparse
import json
import sys

import matplotlib.pyplot as plt
import numpy as np


def plot_json(_args):
    # Open JSON file
    path = _args.path
    data = json.load(open(path, "r"))

    # Define data collection phases
    phases = ["baseline", "expiration1", "rest1", "expiration2", "rest2", "video", "rest3", "recitation", "rest4"]
    tonic = []

    # Plot each phase with a label and a terminating vertical line
    for i in phases:
        for j in data[i]["gsr_tonic"]:
            tonic.append(j)

        # Label the phase in the middle of its plot
        stress_rating = data[i]["stress_rating"]
        label = f"{i}\n{stress_rating}"
        plt.text(x=len(tonic) - 1, y=0, s=label, ha="right", size="small")

        # Place a red line at the end of the phase
        plt.axvline(x=len(tonic) - 1, color="red", linestyle="--")

    # Normalize and plot
    tonic /= np.linalg.norm(tonic)
    plt.plot(tonic)

    plt.title("GSR Test Data")
    plt.ylabel("Skin Conductance Response")
    plt.xlabel("Time (number of samples)")
    plt.show()


if __name__ == "__main__":
    # Set up application
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(required=True)

    # JSON Plot
    parser_foo = subparsers.add_parser("json")
    parser_foo.add_argument("path", type=str)
    parser_foo.set_defaults(func=plot_json)

    # Call appropriate function
    args = parser.parse_args(sys.argv[1:])
    args.func(args)
