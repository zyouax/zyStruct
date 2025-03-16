# zyStruct

## 📌 Project Overview
**ZyStruct** is a powerful and lightweight tool that automatically generates a structured documentation file (`zyReadyAll.md`) for your project. It scans the project directory, excludes specified files and folders, and formats the structure in a readable manner. This tool helps developers maintain clear documentation of their project's architecture.

### 🤖 AI-Friendly Development
ZyStruct is especially useful when working with AI-based development assistants. AI models often forget parts of code or lose context when handling large projects. By generating a complete and structured project overview, ZyStruct ensures that AI tools can better understand your project, helping to debug errors, improve code consistency, and enhance collaboration.

## 🚀 Features
- Generates a well-structured project overview with file content.
- Automatically excludes files and directories listed in `zyNote.md`.
- Creates a hierarchical representation using a clean visual format.
- Reads and includes file contents in the documentation.
- Simple and lightweight with no external dependencies.
- Improves AI-assisted development by maintaining project context.

## 🛠 Installation
To install **ZyStruct**, run:

```bash
pip install .
```
[Fixing "externally-managed-environment"](/doc/fixing-externally-managed-environment.md)

## 📌 Usage
Once installed, you can run the tool with:

```bash
zystruct
```
Alternatively, execute the script manually:

```bash
python src/main.py
```

## 📝 Example `zyNote.md`

```zyNote.md
build/
node_modules/
.temp/
debug.log
.env
src/main.py
```

- For directories, add a trailing `/` (e.g., `build/`).

- For specific files, use their full path relative to the project root (e.g., `src/main.py`).

- For hidden files or directories, prefix them with a `.` (e.g., `.temp/`).

## 📝 Current Project Structure 

```structure.md
# Project structure

├── zyStruc/
│   ├── zyNote.md
│   ├── LICENSE
│   ├── README.md
│   ├── requirements.txt
│   ├── setup.py
├── src/
│   ├── utils.py
│   ├── main.py
│   ├── config.py
├── doc/
│   ├── fixing-externally-managed-environment.md
```

## 📝 Current example of `zyNote.md`

```zyNote.md
.git
LICENSE
README.md
doc/
```

## 📝 Example output `zyReadyAll.md`

<details>
  <summary>Expandir</summary>
 <tbody>

```zyReadyAll.md
# Project architecture

├── zyStruc/
│   ├── zyNote.md
│   ├── requirements.txt
│   ├── setup.py
├── src/
│   ├── utils.py
│   ├── main.py
│   ├── config.py
├── doc/

```

`zyNote.md` :

```
.git
zyReadyAll.md
main.py
```

`requirements.txt` :

```

```

`setup.py` :

```
from setuptools import setup, find_packages

setup(
    name="zystruct",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={
        "console_scripts": [
            "zystruct=main:main"
        ],
    },
)

```

`src/utils.py` :

```
import os

def load_exclusions(file):
    exclusions = set()
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            exclusions = {line.strip() for line in f if line.strip()}
    return exclusions

def list_files(directory, excluded_paths):
    files = []
    structure = []
    for root, dirs, filenames in os.walk(directory, topdown=True):
        rel_root = os.path.relpath(root, directory)
        if any(rel_root == excl or rel_root.startswith(excl + os.sep) for excl in excluded_paths):
            dirs.clear()
            continue

        indent_level = rel_root.count(os.sep)
        indent = "│   " * indent_level + "├── "
        structure.append(f"{indent}{os.path.basename(root)}/")

        for filename in filenames:
            relpath = os.path.relpath(os.path.join(root, filename), directory)
            if any(relpath == excl or relpath.startswith(excl + os.sep) for excl in excluded_paths):
                continue
            files.append(relpath)
            file_indent = "│   " * (indent_level + 1) + "├── "
            structure.append(f"{file_indent}{filename}")

    return files, structure

def write_structure_to_file(files, structure, output_file):
    with open(output_file, "w", encoding="utf-8") as out:
        out.write("# Project architecture\n\n")
        out.write("\n".join(structure) + "\n\n")
        for file in files:
            out.write(f"`{file}` :\n\n")
            try:
                with open(file, "r", encoding="utf-8") as f:
                    content = f.read()
                    out.write("```\n" + content + "\n```\n\n")
            except Exception as e:
                out.write(f"Reading error : {e}\n\n")

```

`src/main.py` :

```
import os
from src.utils import load_exclusions, list_files, write_structure_to_file
from src.config import OUTPUT_FILE, EXCLUDE_FILE

def main():
    project_root = os.getcwd()  # Utilise le dossier courant comme racine
    excluded_paths = load_exclusions(EXCLUDE_FILE)
    files, structure = list_files(project_root, excluded_paths)
    write_structure_to_file(files, structure, OUTPUT_FILE)
    print(f"File {OUTPUT_FILE} generated successfully.")

if __name__ == "__main__":
    main()

```

`src/config.py` :

```
OUTPUT_FILE = "zyReadyAll.md"
EXCLUDE_FILE = "zyNote.md"
```

</tbody>
</details>

## Supporters

[![Stargazers repo roster for @zyouax/zyStruct](https://reporoster.com/stars/dark/zyouax/zyStruct)](https://github.com/zyouax/zyStruct/stargazers)
[![Forkers repo roster for @zyouax/zyStruct](https://reporoster.com/forks/dark/zyouax/zyStruct)](https://github.com/zyouax/zyStruct/network/members)
[![Watchers repo roster for @zyouax/zyStruct](https://reporoster.com/forks/dark/zyouax/zyStruct)](https://github.com/zyouax/zyStruct/watchers)

## 📜 License

zyouax is made [Contributor](https://github.com/zyouax/zyStruct/graphs/contributors). See the **License** file for more details.