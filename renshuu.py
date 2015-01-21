#!/usr/bin/env python

import sys
from workflow import Workflow, web


SEARCH_URL = 'https://www.renshuu.org/index.php'

'''
#!/bin/sh
curl 'https://www.renshuu.org/index.php?page=grammar/search&pg=0&output=dictionary&search=1&bcat_id=&gstring='"$*" |\
 tr ' ' "\n" | grep href
'''

def main(wf):
    params = {
        'page': 'grammar/search',
        'pg': 0,
        'output': 'dictionary',
        'search': 1,
        'gstring': sys.argv[1]
    }
    r = web.get(SEARCH_URL, params)
    r.raise_for_status()
    for line in r.json()['stext_grammar'].strip().split():
        if 'href' not in line:
            continue
        _, url, _ = line.split("'")
        wf.add_item(url, url)
    wf.send_feedback()

if __name__ == '__main__':
    sys.exit(Workflow().run(main))
