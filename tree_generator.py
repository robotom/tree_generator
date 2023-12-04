#!/usr/bin/python

import os
import argparse

def generate_directory_tree(root_path, output_file, indent="", is_last=False, ignore_hidden=False):
    # Get the list of items (files and directories) in the current directory
    items = os.listdir(root_path)

    # Sort items alphabetically to match the `tree` command output
    items.sort()

    # Filter out hidden items if the ignore_hidden flag is set
    if ignore_hidden:
        items = [item for item in items if not item.startswith('.')]

    # Iterate through each item
    for i, item in enumerate(items):
        # Construct the full path to the item
        item_path = os.path.join(root_path, item)

        # Check if the item is a directory
        is_directory = os.path.isdir(item_path)

        # Determine the prefix and connector for the current item
        if i == len(items) - 1:
            prefix = "└── "
            connector = "    " if is_last else "│   "
        else:
            prefix = "├── "
            connector = "│   " if not is_last else "    "

        # Print the item with proper indentation and prefix
        output_file.write(indent + prefix + item + '\n')

        # Recursively generate the directory tree for this subdirectory
        if is_directory:
            generate_directory_tree(item_path, output_file, indent + connector, i == len(items) - 1, ignore_hidden)

if __name__ == "__main__":
    # Create a command-line argument parser
    parser = argparse.ArgumentParser(description="Generate a directory tree and save it to a text file.")
    parser.add_argument("target_directory", help="The target directory to generate the tree from.")
    parser.add_argument("output_file", help="The destination directory for the output .txt file.")
    parser.add_argument("--ignore-hidden", action="store_true", help="Ignore hidden directories (directories starting with a dot).")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Open the output file for writing
    with open(args.output_file, "w") as output_file:
        # Write the <pre> tag to start the preformatted block
        output_file.write("<pre>\n")
        
        # Generate and print the directory tree starting from the target directory
        generate_directory_tree(args.target_directory, output_file, ignore_hidden=args.ignore_hidden)

        # Write the </pre> tag to end the preformatted block
        output_file.write("</pre>\n")
