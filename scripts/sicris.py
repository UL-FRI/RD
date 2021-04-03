import json

def update(sicris_data, date_prefix=''):
    with open('../data/sicris.json', 'w', encoding='utf-8') as fout:
        json.dump(sicris_data, fout, indent=2, sort_keys=True, ensure_ascii=False)
    if date_prefix:
        with open(f'../data/updates/{date_prefix}_sicris.json', 'w', encoding='utf-8') as fout:
            json.dump(sicris_data, fout, indent=2, sort_keys=True, ensure_ascii=False)

def get():
    with open('../data/sicris.json', 'rt', encoding='utf-8') as fin:
        sicris_data = json.load(fin)
    return sicris_data
