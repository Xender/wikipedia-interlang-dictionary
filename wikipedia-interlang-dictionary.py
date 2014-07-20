#!/usr/bin/env python3

# wikipedia-interlang-dictionary.py - translate words by following Wikipedia interlang links.
# Copyright (C) 2014  Aleksander Nitecki
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import requests
import sys

src_lang = 'en'
dst_lang = 'pl'

response = requests.get(
	'https://'+src_lang+'.wikipedia.org/w/api.php',
	params={
		'format' : 'json',
		'action' : 'query',
		'prop'   : 'langlinks',
		'lllang' : dst_lang,
		'titles' : sys.argv[1],
	})

response.raise_for_status()

print( *(result['langlinks'][0]['*'] for result in response.json()['query']['pages'].values()) )
