import argparse

# parser = argparse.ArgumentParser(description="Process some integers.")
# parser.add_argument("integers", metavar="N", type=int, nargs="+", help="an integer for the accumulator")
# parser.add_argument("--sum", dest="accumulate", action="store_const", const=sum, default=max, help="sum the integers (default: find the max)")  
# args = parser.parse_args()
# print(args.accumulate(args.integers))   

# To run this script from the command line, use:
# python commandLine.py 1 2 3 4 --sum
# or
# python commandLine.py 1 2 3 4 


# Example 2

parser = argparse.ArgumentParser(description="Greet the user.")
parser.add_argument("--name", required=True, help="Name of the user")
parser.add_argument("--last", default="Raja", help="Name of the user")
args = parser.parse_args()
print(f"Hello, {args.name}! {args.last}")
print(type(args.name))