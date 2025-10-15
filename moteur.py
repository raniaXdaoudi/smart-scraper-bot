def analyser_requete(input_utilisateur):
	input_utilisateur = input_utilisateur.lower()
	instructions = []

	mots_cles = {
		"titre": {
			"label": "titre",
			"balises": [{"tag": "h1", "attr": None}, {"tag": "h2", "attr": None}, {"tag": "h3", "attr": None}]
		},
		"titres": {
			"label": "titre",
			"balises": [{"tag": "h1", "attr": None}, {"tag": "h2", "attr": None}, {"tag": "h3", "attr": None}]
		},
		"paragraphe": {
			"label": "texte",
			"balises": [{"tag": "p", "attr": None}]
		},
		"résumé": {
			"label": "résumé",
			"balises": [{"tag": "p", "attr": None}]
		},
		"lien": {
			"label": "lien",
			"balises": [{"tag": "a", "attr": "href"}]
		},
		"liens": {
			"label": "lien",
			"balises": [{"tag": "a", "attr": "href"}]
		},
		"hyperlien": {
			"label": "lien",
			"balises": [{"tag": "a", "attr": "href"}]
		}
	}

	for mot in mots_cles:
		if mot in input_utilisateur:
			label = mots_cles[mot]["label"]
			for b in mots_cles[mot]["balises"]:
				instructions.append({
					"tag": b["tag"],
					"attr": b["attr"],
					"label": label
				})

	return instructions
