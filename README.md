# File Format Converter

A private, local alternative to online conversion tools for common file format conversions developers make.

## Current Functionality

The project currently exports a structured document to 8 formats: TXT, CSV, JSON, Markdown, HTML, SVG, RTF, and XML.

Two implementations demonstrate the difference between procedural and pattern-based code:

- **Without design patterns** — flat functions with an if/elif chain
- **With design patterns** — Strategy pattern for export behavior, Factory pattern for object creation

### Project Structure

```
main.py               Entry point — both implementations side by side
export.py             Core export functions (8 formats)
strategy_pattern.py   Abstract ExportStrategy base class, 8 concrete strategies, DocumentExporter context
factory_pattern.py    ExportFactory — creates the right strategy from a format string
exports/              Output directory for exported files
```

### How to Run

```bash
python main.py
```

Select a format when prompted. The exported file appears in the `exports/` folder.

### Supported Export Formats

| Format | Extension | Library |
|--------|-----------|---------|
| TXT | `.txt` | built-in |
| CSV | `.csv` | built-in `csv` |
| JSON | `.json` | built-in `json` |
| Markdown | `.md` | built-in |
| HTML | `.html` | built-in |
| SVG | `.svg` | built-in |
| RTF | `.rtf` | built-in |
| XML | `.xml` | built-in `xml.etree` |

### Dependencies (Current)

- Python 3.10+
- No pip installs required

---

## Future: File Format Converter

### Vision

Pivot the project into a universal file format converter that:

- Keeps data private — files never leave your machine
- Supports batch processing — convert hundreds of files at once
- Has no file size limits
- Works offline
- Produces consistent, reliable output every time

### Why This Exists

Online converters are fine for a single small file, but they fall short when:

- You're handling sensitive or proprietary data
- You need to convert files in bulk
- You're offline or behind a firewall
- The file exceeds the site's size limit
- You need consistent output formatting across runs

### Planned Conversions

| # | Conversion | Use Case |
|---|-----------|----------|
| 1 | PNG → JPG | Reduce file size for photos |
| 2 | JPG → PNG | Lossless format for editing |
| 3 | WEBP → PNG | Browser format to universal format |
| 4 | WEBP → JPG | Browser format to photo format |
| 5 | PNG → WEBP | Optimize images for web |
| 6 | JPG → WEBP | Optimize images for web |
| 7 | GIF → PNG | Extract static image from GIF |
| 8 | GIF → JPG | Extract static image from GIF |
| 9 | PNG → GIF | Simple format conversion |
| 10 | JPG → GIF | Simple format conversion |
| 11 | BMP → PNG | Legacy format to modern format |
| 12 | BMP → JPG | Legacy format to compressed format |
| 13 | PNG → BMP | Modern to legacy system compatibility |
| 14 | JPG → BMP | Modern to legacy system compatibility |

### Planned Usage

```bash
python convert.py photo.png jpg            # single file
python convert.py screenshot.webp png      # WEBP to PNG
python convert.py images/ png jpg          # batch convert folder
```

### Dependencies (Future)

```bash
pip install Pillow
```

### Design Patterns

The converter will use the same patterns already in the codebase:

- **Strategy Pattern** — one strategy per conversion direction (e.g., `PngToJpgStrategy`, `WebpToPngStrategy`)
- **Factory Pattern** — `ConversionFactory` selects the right strategy based on input and output format

The internal flow: **image in → detect format → convert → save to target format**
