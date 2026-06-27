"""Formatação do conteúdo extraído em Markdown."""

from src.extractor import PDFContent


def format_to_markdown(content: PDFContent) -> str:
    """Converte PDFContent em string Markdown.

    Args:
        content: Conteúdo extraído do PDF.

    Returns:
        String formatada em Markdown.
    """
    lines: list[str] = []

    # Título do documento
    lines.append(f"# {content.title}")
    lines.append("")

    for page in content.pages:
        if content.total_pages > 1:
            lines.append(f"---")
            lines.append(f"")
            lines.append(f"*Página {page.page_number}/{content.total_pages}*")
            lines.append("")

        # Processa texto da página
        page_text = page.text.strip()
        if page_text:
            lines.append(page_text)
            lines.append("")

    return "\n".join(lines)
