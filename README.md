# README

## Introduction

This Python script, `upsample_ecgdata.py`, is designed to upsample electrocardiogram (ECG) data stored in a text file. It utilizes the Pandas library for data manipulation, Matplotlib for data visualization, and SciPy for signal processing.

## Usage

To use the script, follow these instructions:

```bash
python upsample_ecgdata.py --samplerate=resamplerate --filename=filename [--plot=True]
```

- `--samplerate`: Specifies the sample rate to which the data will be resampled.
- `--filename`: Specifies the name of the file containing the ECG data. The file must end with `.txt`.
- `--plot`: Optional flag to plot the upsampled ECG data. If included, the script will generate plots.

## Dependencies

Ensure you have the following dependencies installed:

- Python 3.x
- Pandas
- Matplotlib
- SciPy

You can install dependencies using pip:

```bash
pip install pandas matplotlib scipy
```

## Functions

The script includes several functions to process and analyze ECG data:

- `usage()`: Displays usage information for the script.
- `txt_to_csv(filename)`: Converts a text file containing ECG data to CSV format.
- `savefile(df, filename)`: Saves the DataFrame to a CSV file with the same name as the input file but with a `.csv` extension.
- `upsample(df, new_freq)`: Upsamples the ECG data to the specified sample rate using interpolation.
- `seconds_passed(col, sample_rate)`: Computes the time passed for each data point based on the sample rate.
- `ecg_plots(df, sample_rate)`: Generates plots of the upsampled ECG data.

## Example

An example usage of the script is as follows:

```bash
python upsample_ecgdata.py --samplerate=300 --filename="WIF Data/17a/ecg.txt" --plot=True
```

This command resamples the ECG data in the file `ecg.txt` located in the `WIF Data/17a/` directory to a sample rate of 300 samples per second and generates plots of the upsampled data.

## Note

- Ensure that the input file contains ECG data in a suitable format.
- The script assumes that the ECG data file has three columns: 'UNIX', 'Ch1', and 'Ch2'. Adjust the column names if necessary.
- If the `--plot` option is not specified, the script will only resample the data and save it to a CSV file without generating plots.
