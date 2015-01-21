#!/usr/bin/env python

import sys
from workflow import Workflow, web, ICON_WARNING


SEARCH_URL = 'https://www.renshuu.org/index.php'


def main(wf):
    count = 0
    try:
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
            count += 1
            wf.add_item(url, arg=url, valid=True)
    except (AttributeError, ValueError):
        wf.add_item('Loading')
    if not count:
        wf.add_item('No items', icon=ICON_WARNING)
    wf.send_feedback()

if __name__ == '__main__':
    sys.exit(Workflow().run(main))
