import os
from src.utils import load_exclusions, list_files, write_structure_to_file
from src.config import OUTPUT_FILE, EXCLUDE_FILE

def main():
    project_root = os.getcwd()  # Utilise le dossier courant comme racine
    excluded_paths = load_exclusions(EXCLUDE_FILE)
    files, structure = list_files(project_root, excluded_paths)
    write_structure_to_file(files, structure, OUTPUT_FILE)
    print(f"Fichier {OUTPUT_FILE} généré avec succès.")

if __name__ == "__main__":
    main()
