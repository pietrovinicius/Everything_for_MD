"""Interface gráfica CustomTkinter — upload, progresso, preview/salvar."""

from pathlib import Path
from tkinter import filedialog
from typing import Optional

import customtkinter as ctk

from src.converter import convert_pdf_to_markdown


class EverythingForMDApp(ctk.CTk):
    """Janela principal do aplicativo."""

    def __init__(self) -> None:
        super().__init__()

        self.title("Everything for MD")
        self.geometry("800x600")
        self.minsize(600, 400)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self._selected_file: Optional[Path] = None
        self._markdown_result: str = ""

        self._build_ui()

    # ─── UI Construction ──────────────────────────────────────────────

    def _build_ui(self) -> None:
        """Monta todos os widgets da interface."""
        # Header
        self._header = ctk.CTkLabel(
            self,
            text="Everything for MD",
            font=ctk.CTkFont(size=24, weight="bold"),
        )
        self._header.pack(pady=(20, 10))

        self._subtitle = ctk.CTkLabel(
            self,
            text="Converta PDF para Markdown em um clique",
            font=ctk.CTkFont(size=14),
            text_color="gray",
        )
        self._subtitle.pack(pady=(0, 20))

        # Upload frame
        self._upload_frame = ctk.CTkFrame(self, corner_radius=12)
        self._upload_frame.pack(padx=40, pady=10, fill="x")

        self._file_label = ctk.CTkLabel(
            self._upload_frame,
            text="Nenhum arquivo selecionado",
            font=ctk.CTkFont(size=13),
        )
        self._file_label.pack(side="left", padx=20, pady=15)

        self._upload_btn = ctk.CTkButton(
            self._upload_frame,
            text="Selecionar PDF",
            command=self._on_select_file,
            width=140,
        )
        self._upload_btn.pack(side="right", padx=20, pady=15)

        # Progress bar
        self._progress = ctk.CTkProgressBar(self, width=400)
        self._progress.pack(pady=15)
        self._progress.set(0)

        # Convert button
        self._convert_btn = ctk.CTkButton(
            self,
            text="Converter para Markdown",
            command=self._on_convert,
            width=200,
            height=40,
            state="disabled",
        )
        self._convert_btn.pack(pady=10)

        # Preview area
        self._preview = ctk.CTkTextbox(self, corner_radius=8)
        self._preview.pack(padx=40, pady=(10, 5), fill="both", expand=True)

        # Save button
        self._save_btn = ctk.CTkButton(
            self,
            text="Salvar .md",
            command=self._on_save,
            width=140,
            state="disabled",
        )
        self._save_btn.pack(pady=(5, 20))

    # ─── Callbacks ────────────────────────────────────────────────────

    def _on_select_file(self) -> None:
        """Abre diálogo para selecionar PDF."""
        filepath = filedialog.askopenfilename(
            title="Selecione um arquivo PDF",
            filetypes=[("PDF files", "*.pdf")],
        )
        if filepath:
            self._selected_file = Path(filepath)
            self._file_label.configure(text=self._selected_file.name)
            self._convert_btn.configure(state="normal")
            self._progress.set(0)

    def _on_convert(self) -> None:
        """Executa conversão PDF → Markdown."""
        if not self._selected_file:
            return

        self._progress.set(0.2)
        self._convert_btn.configure(state="disabled")
        self.update()

        try:
            self._markdown_result = convert_pdf_to_markdown(self._selected_file)
            self._progress.set(1.0)

            # Mostra preview
            self._preview.delete("0.0", "end")
            self._preview.insert("0.0", self._markdown_result)
            self._save_btn.configure(state="normal")
        except Exception as e:
            self._preview.delete("0.0", "end")
            self._preview.insert("0.0", f"Erro na conversão:\n{e}")
            self._progress.set(0)
        finally:
            self._convert_btn.configure(state="normal")

    def _on_save(self) -> None:
        """Salva o Markdown gerado em arquivo."""
        if not self._markdown_result:
            return

        default_name = (
            self._selected_file.stem + ".md" if self._selected_file else "output.md"
        )
        filepath = filedialog.asksaveasfilename(
            title="Salvar Markdown",
            defaultextension=".md",
            initialfile=default_name,
            filetypes=[("Markdown files", "*.md"), ("All files", "*.*")],
        )
        if filepath:
            Path(filepath).write_text(self._markdown_result, encoding="utf-8")
