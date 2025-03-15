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
        out.write("# Architecture du projet\n\n")
        out.write("\n".join(structure) + "\n\n")
        for file in files:
            out.write(f"`{file}` :\n\n")
            try:
                with open(file, "r", encoding="utf-8") as f:
                    content = f.read()
                    out.write("```\n" + content + "\n```\n\n")
            except Exception as e:
                out.write(f"Erreur de lecture : {e}\n\n")
