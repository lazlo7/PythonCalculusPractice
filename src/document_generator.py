from typing import Callable
from collections.abc import Generator

class DocumentGenerator():
    def __init__(self) -> None:
        self.header: str = r"""\documentclass[11pt]{report}
\usepackage[T2A]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[russian]{babel}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\oddsidemargin=-19mm
\topmargin=-30mm
\textheight 26cm
\hsize 18cm
\textwidth 20cm
\begin{document}

\pagestyle{empty}"""
        self.border: str = r"""\begin{center}
\noindent\rule{8cm}{0.4pt}
\end{center}
"""
        self.title: str = "Индивидуальное задание."
        self.description: str = ""
        self.variant_generator: Callable[[int, bool], str] = lambda variant_n, is_solution: ""
        self.variant_enumerator: Callable[[int], str] = lambda variant_n: f"Вариант ${variant_n}$"

    """
    Sets 'header' part of the document (i. e. where '\\usepackage' is defined)
    """
    def set_header(self, header: str):
        self.header = header
        return self

    """
    Sets the title of the document.
    """
    def set_title(self, title: str):
        self.title = title
        return self

    """
    Sets the description of the document.
    """
    def set_description(self, description: str):
        self.description = description
        return self

    """
    Sets the variant generator function.
    Variant generator receives a variant number, a boolean value, indicating if this is a solution, and returns a string.
    """
    def set_variant_generator(self, variant_generator: Callable[[int, bool], str]):
        self.variant_generator = variant_generator
        return self

    """
    Sets the border of the document, which divides variants from each other.
    """
    def set_border(self, border: str):
        self.border = border
        return self

    def set_variant_enumerator(self, variant_enumerator: Callable[[int], str]):
        self.variant_enumerator = variant_enumerator
        return self

    def generate(self, variant_count: int, is_solution: bool) -> Generator[str]:
        def line(text: str = ""):
            yield text + "\n"

        line(self.header)
        line(r"{\bf " + self.title + "}")
        line()
        line(self.description)
        line()
        
        for variant_n in range(variant_count):
            line(self.border)
            line(self.variant_enumerator(variant_n))
            line(self.variant_generator(variant_n, is_solution))

        line()
        line(r"\end{document}")
