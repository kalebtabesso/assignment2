import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='Process some inputs.')
    parser.add_argument('file_path', type=str, help='Path to the file')
    parser.add_argument('integer_value', type=int, help='An integer value')
    parser.add_argument('float_value', type=float, help='A float value')

    args = parser.parse_args()

    if os.path.isfile(args.file_path):
        print(f"File Path: {args.file_path}")
    else:
        print(f"The path {args.file_path} does not point to a valid file.")
    print(f"Integer Value: {args.integer_value}")
    print(f"Float Value: {args.float_value}")

    # Example additional functionality: multiplying integer and float values
    result = args.integer_value * args.float_value
    print(f"Multiplication of {args.integer_value} and {args.float_value} is {result}")

if __name__ == "__main__":
    main()
