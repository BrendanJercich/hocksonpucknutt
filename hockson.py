# import requests as rq
from bs4 import BeautifulSoup as bs
from math import floor, ceil
import re, os

letters = [chr(x) for x in range(ord('A'), ord('Z')+1)]
first_names = [];
first_name_first_pieces = [];
first_name_last_pieces = [];
last_names = [];
last_name_first_pieces = [];
last_name_last_pieces = [];

strip_non_alpha = re.compile('[^a-zA-Z ]')
collapse_whitespace = re.compile(r'(\s+)')

for letter in letters:
	# I did this too many times and cloudflare got mad at me
	# headers = {
	# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
	# 	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
	# 	'Accept-Language': 'en-US,en;q=0.5',
	# 	'DNT': '1',
	# 	'Connection': 'keep-alive',
	# 	'Upgrade-Insecure-Requests': '1',
	# 	'Sec-Fetch-Dest': 'document',
	# 	'Sec-Fetch-Mode': 'navigate',
	# 	'Sec-Fetch-Site': 'none',
	# 	'Sec-Fetch-User': '?1',
	# }
	# page_url = "https://www.hockeydb.com/ihdb/players/player_ind_{}.html".format(letter)
	# page = rq.get(page_url, headers=headers)
	# soup = bs(page.text, 'html.parser')

	# So then I just went through and saved all 26 files locally as A.html, B.html, etc
	with open("scrape/{}.html".format(letter)) as fp:
	    soup = bs(fp, 'html.parser')
	
	# First get the name from each table row and split that name by spaces
	for row in soup.find_all('table', class_='sortable')[0].tbody.find_all('tr'):
		    first_column_list = collapse_whitespace.sub(' ', strip_non_alpha.sub(' ', row.find_all('a')[0].contents[0])).split()
		    last_names.append(first_column_list[-1])
		    # Middle names and nicknames, but not initials, go into the "first name" list.
		    for sliced_name in first_column_list[:-1]:
		    	if (len(sliced_name)) > 1:
		    		first_names.append(sliced_name)

	# Then break each name in each list apart
	for the_name in first_names:
		if (len(the_name) > 4):
			name_ceil = ceil(len(the_name) / 2)
			name_floor = -1 * name_ceil
			first_name_first_pieces.append(the_name[0:name_ceil].upper())
			first_name_last_pieces.append(the_name[name_floor:].upper())
		else:
			first_name_last_pieces.append(the_name.upper())
			first_name_first_pieces.append(the_name.upper())
			
	for the_name in last_names:
		if (len(the_name) > 4):
			name_ceil = ceil(len(the_name) / 2)
			name_floor = -1 * name_ceil
			last_name_first_pieces.append(the_name[0:name_ceil].upper())
			last_name_last_pieces.append(the_name[name_floor:].upper())
		else:
			last_name_first_pieces.append(the_name.upper())
			last_name_last_pieces.append(the_name.upper())


# Now we have huge lists of name chunks.
# Convert them to sets to remove duplicates, then convert them back.
first_name_first_pieces = list(set(first_name_first_pieces))
first_name_last_pieces = list(set(first_name_last_pieces))
last_name_first_pieces = list(set(last_name_first_pieces))
last_name_last_pieces = list(set(last_name_last_pieces))
first_name_first_pieces.sort()
first_name_last_pieces.sort()
last_name_first_pieces.sort()
last_name_last_pieces.sort()

# Write them out to files.
with open('first_name_first_pieces.txt', 'w') as f:
    for line in list(first_name_first_pieces):
        f.write(f"{line}\n")
with open('first_name_last_pieces.txt', 'w') as f:
    for line in list(first_name_last_pieces):
        f.write(f"{line}\n")
with open('last_name_first_pieces.txt', 'w') as f:
    for line in list(last_name_first_pieces):
        f.write(f"{line}\n")
with open('last_name_last_pieces.txt', 'w') as f:
    for line in list(last_name_last_pieces):
        f.write(f"{line}\n")
		