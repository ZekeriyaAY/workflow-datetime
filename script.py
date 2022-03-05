import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--format', type=str, required=True, help='Date format')
parser.add_argument('--tag', type=str, required=True, help='Tag name')
parser.add_argument('--path', type=str, required=True,
                    help='Markdown file path')

args = parser.parse_args()

now = datetime.now()
now = now.strftime(args.format)  # https://strftime.org/

with open(args.path, 'r') as md_file:
    data = md_file.read()

start_index = data.find(f'<!-- {args.tag}:START -->')
end_index = data.find(f'<!-- {args.tag}:END -->')

if start_index == -1 or end_index == -1:
    raise Exception(
        "The tag variable in the Markdown file and the tag variable in the workflow file are not the same.")

start_index += len(f'<!-- {args.tag}:START -->')
new_data = data[:start_index] + '\n' + now + '\n' + data[end_index:]

with open(args.path, 'w') as md_file:
    md_file.write(new_data)
