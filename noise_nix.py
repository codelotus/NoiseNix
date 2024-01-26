from pydub import AudioSegment
import argparse
import os

def delete_file(file_path):
    """
    Utility for cleaning up the workspace

    Parameters:
    - file_path (string): the location of the file to delete
    """
    try:
        # Check if the file exists before attempting to delete
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully.")
        else:
            print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {str(e)}")


def remove_echo_and_perform_gain(input_file, output_file):
    """
    The actual processing of of the audio file.  Of note is hte use of hte arnnoise models
    Available models include:
        * beguiling-drafter-2018-08-30/bd.rnnn
        * conjoined-burgers-2018-08-28/cb.rnnn
        * leavened-quisling-2018-08-31/lq.rnnn
        * marathon-prescription-2018-08-29/mp.rnnn
        * somnolent-hogwash-2018-09-01/sh.rnnn
    
    Parameters:
    - input_file (string): fiile to process
    - output_file (string): resulting processed file
    aecho=0.1:0.88:6:0.5 lowpass=f=3000,highpass=f=100,\
    """
    try:
        # Load the audio file
        audio = AudioSegment.from_file(input_file)

        audio.export(output_file,
                           format="mp3",
                           bitrate="192k",
                           parameters=[
                               "-af", "arnndn=m='rnnoise-models/somnolent-hogwash-2018-09-01/sh.rnnn',\
                                aecho=0.01:0.25:2:0.5 lowpass=f=3000,highpass=f=200,\
                                volume=10"
                               ],
                           cover="christ_reformed.png")
        print(f"Processing successful. Output saved to {output_file}")
    except Exception as e:
        print(f"Exception: {str(e)}")


def main():
    """
    Main function... where the magic happens
    """

    parser = argparse.ArgumentParser(description='Script for removing noise from a spoken audio file')

    # Add positional argument
    parser.add_argument('input_file', type=str, help='Path to audio file to process.')

    # Add optional argument
    parser.add_argument('--output', '-o', type=str, default='result.mp3', help='Path to the resulting processed file. Default is result.mp3.')

    # Parse the command-line arguments
    args = parser.parse_args()

    if os.path.exists(args.output):
        delete_file(args.output)
    remove_echo_and_perform_gain(args.input_file, args.output)


# Check if the script is run directly
if __name__ == "__main__":
    main()
