import os
from ConvertFactory import ConvertFactory
from ConvertStrategy import FileConverter

EXT_ALIASES = {"jpeg": "jpg"}

def get_input_files():
    os.makedirs("input", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    files = [f for f in os.listdir("input") if os.path.isfile(os.path.join("input", f))]
    if not files:
        print("No files found in input/ folder.")
    return files

def get_available_conversions(files):
    extensions = set()
    for f in files:
        ext = os.path.splitext(f)[1].lower().lstrip(".")
        ext = EXT_ALIASES.get(ext, ext)
        if ext:
            extensions.add(ext)

    conversions = []
    for ext in sorted(extensions):
        targets = ConvertFactory.get_targets(ext)
        for target in targets:
            conversions.append((ext, target))

    if not conversions:
        print("No supported conversions available for the files in input/.")
    return conversions

def prompt_conversion_choice(conversions):
    print("\nAvailable conversions:")
    for i, (source, target) in enumerate(conversions, 1):
        print(f"  {i}. {source} -> {target}")

    choice = input("\nSelect a conversion (enter number): ").strip()
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(conversions):
        print(f"Invalid choice. Please enter a number between 1 and {len(conversions)}.")
        choice = input("Select a conversion (enter number): ").strip()

    return conversions[int(choice) - 1]

def convert_files(files, source_ext, target_ext):
    strategy = ConvertFactory.create(source_ext, target_ext)
    converter = FileConverter(strategy)

    for f in files:
        ext = os.path.splitext(f)[1].lower().lstrip(".")
        ext = EXT_ALIASES.get(ext, ext)
        if ext == source_ext:
            converter.convert(os.path.join("input", f))

def main():
    files = get_input_files()
    if not files:
        return

    conversions = get_available_conversions(files)
    if not conversions:
        return

    source_ext, target_ext = prompt_conversion_choice(conversions)
    convert_files(files, source_ext, target_ext)

if __name__ == "__main__":
    #TODO: refactor main_convert() into separate functions, and call those functions from main()
    #TODO: create unit test(s) to verify factory pattern output based on input format
    #TODO: remove excess files and folders (ex: claude.md, .vscode, .git, .gitignore, etc.)
    #TODO: provide sample input files for testing
    #TODO: refactor README.md to include instructions for: running tests & running the program with sample input files
    main()
