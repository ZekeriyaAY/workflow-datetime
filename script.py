import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--format', type=str, required=True, help='Date format')
parser.add_argument('--section', type=str, required=True, help='Section name')
parser.add_argument('--path', type=str, required=True,
                    help='Markdown file path')

args = parser.parse_args()

now = datetime.now()
now = now.strftime(args.format)  # https://strftime.org/

with open(args.path, 'r') as md_file:
    data = md_file.read()

start_index = data.find(f'<!-- {args.section}:START -->')
end_index = data.find(f'<!-- {args.section}:END -->')

if start_index == -1 or end_index == -1:
    raise Exception(
        "The section variable in the Markdown file and the section variable in the workflow file are not the same.")

start_index += len(f'<!-- {args.section}:START -->')
new_data = data[:start_index] + '\n' + now + '\n' + data[end_index:]

with open(args.path, 'w') as md_file:
    md_file.write(new_data)
