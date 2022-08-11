import json
from candidate import Candidate

def load_candidates(filename):
    """загружает данные из файла"""
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def get_all(data):
    """вывод всех кандидатов"""
    arr = []
    for item in data:
        skills_old = item['skills'].split(',')
        skills = [skill.strip().lower() for skill in skills_old]
        candidate = Candidate(item['pk'], item['name'], item['position'], item['skills'].lower(), item['picture'])
        arr.append(candidate)
    return arr

#print(get_all(load_candidates('candidates.json')))
def get_by_pk(pk, data):
    """возвращает кандидата по pk"""
    for item in data:
        if item.pk == pk:
            return item

def get_by_skill(skill_name, data):
    """возвращает кандидатов по навыку"""
    arr = []
    for item in data:
        if skill_name in item.skills:
            arr.append(item)
    return arr