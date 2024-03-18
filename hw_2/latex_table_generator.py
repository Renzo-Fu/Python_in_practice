def generate_complete_latex_document(data, title="test", author="Renzo Flores Ugarte", date="March 2024", introduction_text=""):
    """
    Generates a complete LaTeX document with a table included in the introduction section.

    :param data: Two-dimensional list with data for the table.
    :param title: Title of the document.
    :param author: Author of the document.
    :param date: Date for the document.
    :param introduction_text: Text to include in the Introduction section.
    :return: String with the complete LaTeX document.
    """
    """
    Generates LaTeX code for a table from a two-dimensional list.

    :param data: Two-dimensional list with data for the table.
    :return: String with LaTeX code for the table.
    """
    header = data[0]  # Assuming the first row is the header
    body = data[1:]   # The rest are body rows

    # Start of the table
    latex = "\\begin{tabular}{|" + "l|" * len(header) + "}\n\\hline\n"

    # Header
    latex += " & ".join(header) + " \\\\\n\\hline\n"

    # Body
    for row in body:
        latex += " & ".join(row) + " \\\\\n\\hline\n"

    # End of the table
    latex += "\\end{tabular}\n"

    document = "\\documentclass{article}\n" \
               "\\usepackage{graphicx} % Required for inserting images\n" \
               "\\usepackage[T2A]{fontenc}\n"\
               "\\usepackage[utf8]{inputenc}\n"\
               "\\usepackage[english, russian]{babel}\n\n"\
               "\\title{" + title + "}\n" \
               "\\author{" + author + "}\n" \
               "\\date{" + date + "}\n\n" \
               "\\begin{document}\n\n" \
               "\\maketitle\n\n" \
               "\\section{Introduction}\n\n" + \
               introduction_text + "\n\n" + \
               "\\begin{center}\n" + \
               latex + "\n" \
               "\\end{center}\n\n" \
               "\\end{document}"

    return document


def generate_latex_image(image_path, caption="Figure", label="fig:image"):
    """
    Генерирует LaTeX код для вставки картинки.

    :param image_path: Путь к файлу изображения (относительный путь от .tex файла).
    :param caption: Подпись к изображению.
    :param label: Метка для ссылки на изображение.
    :return: Строка с LaTeX кодом для вставки картинки.
    """
    return f"""\\begin{{figure}}[h]
\\centering
\\includegraphics[width=0.8\\textwidth]{{{image_path}}}
\\caption{{{caption}}}
\\label{{{label}}}
\\end{{figure}}
"""
