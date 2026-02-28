import os

document = {
    "title": "Q1 Sales Report",
    "author": "Jane Smith",
    "rows": [
        ["Region", "Product", "Units Sold", "Revenue"],
        ["North",  "Widget A", 120,          "$2,400"],
        ["South",  "Widget B", 95,           "$1,900"],
        ["East",   "Widget C", 200,          "$6,000"],
        ["West",   "Widget A", 80,           "$1,600"],
    ]
}

def export_pdf(document):
    filename = f"exports/{document['title']}.txt"
    with open(filename, "w") as f:
        f.write("=== PDF EXPORT ===\n")
        f.write(f"Title:  {document['title']}\n")
        f.write(f"Author: {document['author']}\n")
        f.write("-" * 40 + "\n")
        for row in document["rows"]:
            f.write("  |  ".join(str(cell).ljust(12) for cell in row) + "\n")
        f.write("=" * 40 + "\n")
    print(f"Exported PDF to {filename}")


def export_excel(document):
    filename = f"exports/{document['title']}.tsv"
    with open(filename, "w") as f:
        f.write(f"[Sheet: {document['title']}]\n")
        f.write(f"[Author: {document['author']}]\n\n")
        for row in document["rows"]:
            f.write("\t".join(str(cell) for cell in row) + "\n")
    print(f"Exported Excel to {filename}")


def export_csv(document):
    filename = f"exports/{document['title']}.csv"
    with open(filename, "w") as f:
        for row in document["rows"]:
            f.write(",".join(f'"{cell}"' for cell in row) + "\n")
    print(f"Exported CSV to {filename}")


os.makedirs("exports", exist_ok=True)

# Change this value to test a different format: "pdf", "excel", "csv"
formats = ["pdf", "excel", "csv"]
format = input(f"Enter export format ({', '.join(formats)}): ").strip().lower()
while format not in formats:
    print(f"Invalid format: '{format}'. Please enter {', '.join(formats)}.")
    format = input(f"Enter export format ({', '.join(formats)}): ").strip().lower()

if format == "pdf":
    export_pdf(document)
elif format == "excel":
    export_excel(document)
elif format == "csv":
    export_csv(document)