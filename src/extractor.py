"""Extração de texto e estrutura do PDF via PyMuPDF."""

from dataclasses import dataclass, field
from pathlib import Path

import fitz  # PyMuPDF


@dataclass(frozen=True)
class PageContent:
    """Conteúdo extraído de uma página do PDF."""

    page_number: int
    text: str
    blocks: list[dict] = field(default_factory=list)


@dataclass(frozen=True)
class PDFContent:
    """Conteúdo completo extraído do PDF."""

    title: str
    pages: list[PageContent]
    total_pages: int


def extract_pdf_content(pdf_path: Path) -> PDFContent:
    """Extrai texto e estrutura de todas as páginas do PDF.

    Args:
        pdf_path: Caminho para o arquivo PDF.

    Returns:
        PDFContent com texto e blocos de cada página.
    """
    doc = fitz.open(str(pdf_path))

    pages: list[PageContent] = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text")
        blocks = page.get_text("dict")["blocks"]

        pages.append(
            PageContent(
                page_number=page_num + 1,
                text=text,
                blocks=blocks,
            )
        )

    title = doc.metadata.get("title", "") or pdf_path.stem
    total_pages = len(doc)
    doc.close()

    return PDFContent(title=title, pages=pages, total_pages=total_pages)
