#!/usr/bin/env python

import os
import yaml

menu = {
    'references': [],
    'manual': []
}

# References
for ref in [i for i in os.listdir('references') if i.endswith('.md')]:
    name = ref.replace('.md', '')
    with open(os.path.join('references', ref), 'r') as f:
        data = f.read()
        # Keep only the yaml header
        delimiter = data.index('---\n', 2)
        data = data[:delimiter]
        content = yaml.safe_load(data)

    menu['references'].append({
        'title': content.get('title'),
        'name': name
    })

# Manual
for man in [i for i in os.listdir('manual') if i.endswith('.md')]:
    name = man.replace('.md', '')
    menu['manual'].append({
        'title': name,
        'name': name
    })

with open('_data/menu.yml', 'w') as a:
    a.write(yaml.safe_dump(menu, explicit_start=True, default_flow_style=False))