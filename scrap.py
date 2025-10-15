import moteur
import requests
import csv
from datetime import date
from bs4 import BeautifulSoup

#choix
def get_input():
	url = input("Choisissez le site a scraper : ").strip()
	requete = input("Que veux-tu extraire ? ")
	instructions = moteur.analyser_requete(requete)
	if instructions:
		print("\nCompris ! Je vais extraire :")
		deja_affiches = set()
		for instr in instructions:
			label = instr["label"]
			tag = instr["tag"]
			attr = instr["attr"]
			if label not in deja_affiches:
				deja_affiches.add(label)
				if attr:
					print(f"- {label} (balise <{tag}> avec attribut '{attr}')")
				else:
					print(f"- {label} (balise <{tag}>)")
	else:
		print("Je n'ai rien compris. Reformule ta demande.")
	return url, instructions

def get_html(url):
	if not url.startswith("http://") and not url.startswith("https://"):
		print("L'URL doit commencer par http:// ou https://")
		return None
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
					  "AppleWebKit/537.36 (KHTML, like Gecko) "
					  "Chrome/115.0 Safari/537.36"
	}
	try:
		response = requests.get(url, headers=headers, timeout=10)
		response.raise_for_status()
		soup = BeautifulSoup(response.content, "html.parser")
		return soup
	except requests.exceptions.MissingSchema:
		print("Format d’URL incorrect.")
	except requests.exceptions.HTTPError as e:
		print(f"Erreur HTTP : {e}")
	except requests.exceptions.ConnectionError:
		print("Problème de connexion. Vérifie ta connexion internet.")
	except requests.exceptions.Timeout:
		print("Le site a mis trop de temps à répondre.")
	except requests.exceptions.RequestException as e:
		print(f"Erreur réseau : {e}")
	return None

#création du fichier csv
def save_to_csv(resultats, nom_fichier):
	try:
		with open(nom_fichier, 'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(["type", "contenu"])
			for label, valeur in resultats:
				writer.writerow([label, valeur])
	except PermissionError:
		print("Impossible d’écrire le fichier.")
	except Exception as e:
		print(f"Une erreur est survenue lors de la sauvegarde : {e}")

#attribut + text save
def extract_elements(soup, instructions):
	all_results = []
	for instr in instructions:
		tag = instr["tag"]
		attr = instr["attr"]
		elements = soup.find_all(tag)
		for el in elements:
			if attr:
				valeur = el.get(attr)
			else:
				valeur = el.get_text(strip=True)
			if valeur:
				if (instr["label"], valeur) not in all_results:
					all_results.append((instr["label"], valeur))
	if all_results:
		all_results = [(label, valeur) for label, valeur in all_results if valeur.strip()]

		if all_results:
			labels = sorted(set(label for label, _ in all_results))
			today = date.today().isoformat()
			nom = "_".join(labels)
			nom_fichier = f"scraping_{nom}_{today}.csv"
			save_to_csv(all_results, nom_fichier)
		else:
			print("Les balises ont été trouvées, mais elles étaient vides. Aucun fichier n'a été créé.")
	else:
		print("Aucune donnée trouvée correspondant à votre demande.")

def main():
	url, instructions = get_input()
	soup = get_html(url)
	if soup:
		extract_elements(soup, instructions)
	else:
		print("Le scraping a échoué. Merci de réessayer avec un lien valide.")

if __name__ == "__main__":
	main()
