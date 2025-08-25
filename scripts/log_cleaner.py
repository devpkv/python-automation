import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True, help="Path to the log file")
parser.add_argument("--output", required=True, help="Path to save the cleaned log file")
args=parser.parse_args()

def clean_log(input_path, output_path):
    with open(input_path, "r") as logFile, open(output_path, "w") as cleanFile: 
        for line in logFile:
            if "ERROR" in line:
                cleanFile.write(line)

    print(f"Cleaned log saved to {output_path}")

clean_log(args.input, args.output)