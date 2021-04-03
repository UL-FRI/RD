import json

def update(k, v, date_prefix=''):
    with open('../data/stats.json', 'rt') as fin:
        data = json.load(fin)
    data[k] = v
    with open('../data/stats.json', 'w', encoding='utf-8') as fout:
        json.dump(data, fout, indent=2, sort_keys=True, ensure_ascii=False)
    if date_prefix:
        with open(f'../data/updates/{date_prefix}_stats.json', 'w') as fout:
            json.dump(data, fout, indent=2, sort_keys=True, ensure_ascii=False)
