import sys, getopt
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import resample

#
#  ======== usage ========
#
def usage():
    # Define the usage arguments for the user
    print("usage: " + sys.argv[0] + " [--help] [--samplerate=resamplerate] [--dirname=filename]")
    print("\n--help prints this usage information")
    print("--samplerate specifies the sample rate to resample the data")
    print("--filename specifies the name of the file to work with (must end with ecg.txt)")
    
def txt_to_csv(filename):
    # Convert a txt file to csv format
    return(pd.read_csv(filename, sep='\s+', names=['UNIX', 'Ch1', 'Ch2', 'Ch3'], index_col=False))

def savefile(df, filename):
    # Change the filename ending from .txt to .csv
    # Save the new csv file to the current directory
    df.to_csv(filename[:-4] + ".csv", sep=" ", index=False)

def upsample(df, new_freq):
    # Upsample the data from 200 to 300 via interpolation
    # Resampling factor is defined as new freq / original freq
    resampling_factor = new_freq / 200
    upsampled_df = pd.DataFrame()
    
    # Resample each channel in the dataframe
    for col in df.columns:
        print(col)
        new_length = int(len(df[col])*resampling_factor)
        upsampled_df[col] = resample(df[col], new_length)

    return(upsampled_df)

def seconds_passed(col, sample_rate):
    time_differences = [i/sample_rate for i in col.index]
    return time_differences

def ecg_plots(df, sample_rate):
    ts = seconds_passed(df['Ch1'], sample_rate)

    plt.figure()
    plt.plot(ts, df['Ch1'])
    plt.title('Upsampled ECG Data for Channel 1')
    plt.xlabel('Time Passed (seconds)')
    plt.ylabel('Voltage (µV)')
    plt.show()

def main():
    # Example input: python upsample_ecgdata.py --samplerate=300 --filename="WIF Data/17a/ecg.txt" --plot=True

    long_options = ["help", "samplerate=", "filename=", "plot="]

    helpflag = False
    plot = False
    resamplerate = ""
    filename = ""

    try:
        # Parsing argument
        options, remainder = getopt.getopt(sys.argv[1:], "", long_options)

        # Checking each argument
        for opt, arg in options:
            if opt in ("-h", "--help"):
                helpflag = True

            elif opt in ("--samplerate"):
                resamplerate = int(arg)

            elif opt in ("--filename"):
                filename = arg
                if not filename.endswith('.txt'):
                    usage()
                    quit()
            
            elif opt in ("--plot"):
                plot = True

    except getopt.error as err:
        print(sys.argv[0] + ": " + str(err))
        usage()
        quit()

    if (resamplerate == "" or filename == ""):
        print("got here")
        usage()
        quit()

    # Resample the data
    ecg_data = txt_to_csv(filename)
    ecg_data = upsample(ecg_data, resamplerate)

    # Save the resampled file as a csv in the current directory
    savefile(ecg_data, filename)

    # Plot the data
    if plot:
        ecg_plots(ecg_data, resamplerate)

if __name__ == '__main__':
    main()