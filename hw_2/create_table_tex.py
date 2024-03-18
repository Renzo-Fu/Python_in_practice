from latex_table_generator import generate_complete_latex_document, generate_latex_image
import os

# Пример данных для таблицы
data = [
    ["Header 1", "Header 2", "Header 3"],
    ["Row 1 Col 1", "Row 1 Col 2", "Row 1 Col 3"],
    ["Row 2 Col 1", "Row 2 Col 2", "Row 2 Col 3"]
]

# Генерируем LaTeX код для таблицы и основы документа
latex_document = generate_complete_latex_document(
    data, introduction_text="Here's an example table:")

# Генерируем LaTeX код для изображения
# Относительный путь к изображению относительно места компиляции .tex файла
image_path = "C:/Users/renz_/Python_course/hw_2/artifacts/OIP.jpg"
image_code = generate_latex_image(
    image_path, caption="Пример изображения", label="fig:exampleImage")

# Вставляем код изображения перед концом документа
latex_document_with_image = latex_document.replace(
    "\\end{document}", image_code + "\n\\end{document}")

# Определение пути к папке artifacts внутри hw_2
artifacts_path = os.path.join(os.getcwd(), "hw_2", "artifacts")

# Убедитесь, что папка artifacts существует; если нет, то создайте ее
if not os.path.exists(artifacts_path):
    os.makedirs(artifacts_path)

# Определение пути к файлу внутри папки artifacts
# Изменил имя файла на example_document.tex для ясности
file_path = os.path.join(artifacts_path, "example_document.tex")


# Сохраняем полный LaTeX код в файл, включая изображение, с указанием кодировки utf-8
with open(file_path, "w", encoding="utf-8") as file:
    file.write(latex_document_with_image)


print(f"LaTeX код сохранен в файле {file_path}")
