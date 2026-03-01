import export
from abc import ABC, abstractmethod

# --- Abstract Strategy ---

class ExportStrategy(ABC):
    @abstractmethod
    def export(self, document):
        pass


# --- Concrete Strategies ---
class TxtStrategy(ExportStrategy):
    def export(self, document):
        export.export_txt(document)

class CsvStrategy(ExportStrategy):
    def export(self, document):
        export.export_csv(document)

class JsonStrategy(ExportStrategy):
    def export(self, document):
        export.export_json(document)

class MarkdownStrategy(ExportStrategy):
    def export(self, document):
        export.export_markdown(document)

class HtmlStrategy(ExportStrategy):
    def export(self, document):
        export.export_html(document)

class SvgStrategy(ExportStrategy):
    def export(self, document):
        export.export_svg(document)

class RtfStrategy(ExportStrategy):
    def export(self, document):
        export.export_rtf(document)

class XmlStrategy(ExportStrategy):
    def export(self, document):
        export.export_xml(document)

# --- Context ---
class DocumentExporter:
    def __init__(self, strategy: ExportStrategy):
        self.strategy = strategy

    def export(self, document):
        self.strategy.export(document)