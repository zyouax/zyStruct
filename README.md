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

## Supporters

[![Stargazers repo roster for @zyouax/zyStruct](https://reporoster.com/stars/dark/zyouax/zyStruct)](https://github.com/zyouax/zyStruct/stargazers)
[![Forkers repo roster for @zyouax/zyStruct](https://reporoster.com/forks/dark/zyouax/zyStruct)](https://github.com/zyouax/zyStruct/network/members)
[![Watchers repo roster for @zyouax/zyStruct](https://reporoster.com/forks/dark/zyouax/zyStruct)](https://github.com/zyouax/zyStruct/watchers)

## 📜 License

zyouax is made [Contributor](https://github.com/zyouax/zyStruct/graphs/contributors). See the **License** file for more details.