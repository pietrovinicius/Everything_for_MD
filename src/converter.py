"""Orquestra pipeline PDF → Markdown."""

from pathlib import Path

from src.extractor import extract_pdf_content
from src.formatter import format_to_markdown


def convert_pdf_to_markdown(pdf_path: Path) -> str:
    """Converte um PDF em string Markdown.

    Args:
        pdf_path: Caminho para o arquivo PDF.

    Returns:
        Conteúdo em formato Markdown.

    Raises:
        FileNotFoundError: Se o PDF não existir.
        ValueError: Se o arquivo não for PDF válido.
    """
    if not pdf_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {pdf_path}")

    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError(f"Arquivo não é PDF: {pdf_path.suffix}")

    raw_content = extract_pdf_content(pdf_path)
    markdown = format_to_markdown(raw_content)
    return markdown
