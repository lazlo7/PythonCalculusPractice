from typing import Callable
from collections.abc import Generator

class DocumentGenerator:
    DEFAULT_HEADER: str = r"""\documentclass[11pt]{report}
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

    DEFAULT_BORDER: str = r"""\begin{center}
\noindent\rule{8cm}{0.4pt}
\end{center}"""

    def __init__(self, 
                 variant_generator: Callable[[int], tuple[str, str]], 
                 description: str,
                 header: str = DEFAULT_HEADER, 
                 border: str = DEFAULT_BORDER,
                 title: str = "Индивидуальное задание.",
                 variant_enumerator: Callable[[int], str] = lambda variant_n: f"Вариант ${variant_n}$"):
        self.variant_generator = variant_generator
        self.description = description
        self.header = header
        self.border = border
        self.title = title
        self.variant_enumerator = variant_enumerator

    def generate(self, variant_count: int) -> Generator[tuple[str, str]]:
        def line(task: str = "", solution: str = None) -> tuple[str, str]:
            if solution is None:
                solution = task
            return task + "\n", solution + "\n"

        yield line(self.header)
        yield line(r"{\bf " + self.title + "}")
        yield line()
        yield line(self.description)
        yield line()
        
        for variant_n in range(variant_count):
            yield line(self.border)
            yield line(self.variant_enumerator(variant_n))
            yield line(*self.variant_generator(variant_n))

        yield line()
        yield line(r"\end{document}")

