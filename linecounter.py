file = "project.py"

with open(file, "r", encoding="utf-8") as file:
    line_count = sum(
        1 for line in file if line.strip() and not line.strip().startswith("#")
    )

print(f"Total non-blank lines: {line_count}")
