import markdown
import sys

if len(sys.argv) != 3:
    print("Usage: python markdown_to_html.py input_file.md output_file.html")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r") as f:
    markdown_text = f.read()

html = markdown.markdown(markdown_text)

with open(output_file, "w") as f:
    f.write(html)

print("Conversion complete.")
