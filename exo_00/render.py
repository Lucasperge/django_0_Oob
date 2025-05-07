import sys
import os
import re

# Vérifier si le fichier settings.py est disponible
try:
    import settings
except ImportError:
    print("Erreur : le fichier settings.py est manquant ou invalide.")
    sys.exit(1)

# Vérification du nombre d’arguments dans la ligne de commande
if len(sys.argv) != 2:
    print("Usage : python3 render.py fichier.template")
    sys.exit(1)

# Le nom du fichier .template passé en argument
template_file = sys.argv[1]

# Vérification de l'extension .template
if not template_file.endswith(".template"):
    print("Erreur : le fichier doit avoir une extension .template")
    sys.exit(1)

# Vérification si le fichier existe
if not os.path.isfile(template_file):
    print("Erreur : le fichier spécifié n’existe pas")
    sys.exit(1)

# Lecture du fichier .template
with open(template_file, "r") as f:
    content = f.read()

# Fonction qui remplace les {nom} par la valeur correspondante dans settings.py
def replacer(match):
    key = match.group(1)  # On récupère le mot entre { et }
    if hasattr(settings, key):  # Si le mot existe dans settings.py
        return str(getattr(settings, key))  # Remplace par la valeur
    else:
        print(f"Erreur : variable '{key}' non trouvée dans settings.py")
        sys.exit(1)

# Remplacer toutes les occurrences de {nom} dans le contenu
rendered = re.sub(r"\{(\w+)\}", replacer, content)

# Créer le nom du fichier de sortie (.html)
output_file = template_file.replace(".template", ".html")

# Écrire le résultat dans un fichier .html
with open(output_file, "w") as f:
    f.write(rendered)

print(f"Fichier {output_file} créé avec succès !")
