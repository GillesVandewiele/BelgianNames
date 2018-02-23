from bs4 import BeautifulSoup
import requests

with open('rijksarchief_given_names.txt', 'w+') as gn_ofp, open('rijksarchief_family_names.txt', 'w+') as fn_ofp:
	unique_given_names = set()
	unique_family_names = set()
	for i in range(627831):
		try:
			print('Parsing page {}/627831...'.format(i))
			url = "https://search.arch.be/nl/zoeken-naar-personen/zoekresultaat/q/persoon_achternaam_t_0/*/q/zoekwijze/s/start/{}?M=0&V=0&O=0&persoon_0_periode_geen=0".format(i*50)
			html_doc = requests.get(url).text

			soup = BeautifulSoup(html_doc, 'html.parser')

			given_names = soup.find_all('td')[5::7]
			for given_name in given_names:
				text = given_name.get_text().lower()
				if text not in unique_given_names:
					gn_ofp.write(text+'\n')
					unique_given_names.add(text)

			family_names = soup.find_all('td')[4::7]
			for family_name in family_names:
				text = family_name.get_text().lower()
				if text not in unique_family_names:
					fn_ofp.write(text+'\n')
					unique_family_names.add(text)

			print('Currently we have {} given names and {} family names...'.format(len(unique_given_names), len(unique_family_names)))
		except:
			print('Something went wrong with parsing page {}...'.format(i))
