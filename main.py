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
    print("=== PDF EXPORT ===")
    print(f"Title:  {document['title']}")
    print(f"Author: {document['author']}")
    print("-" * 40)
    for row in document["rows"]:
        print("  |  ".join(str(cell).ljust(12) for cell in row))
    print("=" * 40)
    print()


def export_excel(document):
    print("=== EXCEL EXPORT ===")
    print(f"[Sheet: {document['title']}]")
    print(f"[Author: {document['author']}]")
    print()
    for row in document["rows"]:
        print("\t".join(str(cell) for cell in row))
    print()


def export_csv(document):
    print("=== CSV EXPORT ===")
    for row in document["rows"]:
        print(",".join(f'"{cell}"' for cell in row))
    print()


#TO DO: refactor export_* functions to create files in exports folder instead of printing to console
#TO DO: remove .claude folder, .git folder, readme.md, and claude.md file 


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