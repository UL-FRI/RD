import json

def update(mentors_data, date_prefix=''):
    with open('../data/doctoral_mentors.json', 'w', encoding='utf-8') as fout:
        json.dump(mentors_data, fout, indent=2, sort_keys=True, ensure_ascii=False)
    if date_prefix:
        with open(f'../data/updates/{date_prefix}_doctoral_mentors.json', 'w', encoding='utf-8') as fout:
            json.dump(mentors_data, fout, indent=2, sort_keys=True, ensure_ascii=False)

def get():
    with open('../data/doctoral_mentors.json', 'rt', encoding='utf-8') as fin:
        mentors_data = json.load(fin)
    return mentors_data

def create_files(mentors_data):
    for rid, rec in mentors_data.items():
        firstname = rec['firstname']
        lastname = rec['lastname']
        # write mentor file
        text = f"""
---
title: {exp_id}
linkTitle: {exp_id}
type: "page"
type: "doctoral-mentor"
fi: "{exp_id}"
---
"""
        f = open("../content/doctoral-mentors/%s.md" % (exp_id), "wt")
        f.write(code)
        f.close()
