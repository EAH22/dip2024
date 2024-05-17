import subprocess
import sys

# Path to the file to print, passed as an argument
if len(sys.argv) != 2:
    print("Usage: python3 print.py <path_to_file_to_print>")
    sys.exit(1)

file_to_print_path = sys.argv[1]

# Command to print the file
print_command = ["lp", "-d", "HP_OfficeJet_200_Mobile_Series_4F2FC0_USB", file_to_print_path]

try:
    subprocess.run(print_command, check=True)
    print(f"Successfully sent {file_to_print_path} to the printer.")
except subprocess.CalledProcessError as e:
    print(f"Failed to print {file_to_print_path}. Error: {e}")
