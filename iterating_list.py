#!/usr/bin/env python3.8

users = [
    { 'admin': True, 'active': False, 'name': 'Chelsea' },
    { 'admin': True, 'active': True, 'name': 'Paula' },
    { 'admin': True, 'active': False, 'name': 'Dean' },
    { 'admin': False, 'active': True, 'name': 'Kevin' },
    { 'admin': False, 'active': False, 'name': 'Kathy' },
    { 'admin': True, 'active': True, 'name': 'Michael' }
    ]

line = 1

for user in users:
    if user['admin'] and user['active']:
        print(f"{line}. ACTIVE - (ADMIN) {user['name']}")
        line = line + 1
    elif user['active']:
        print(f"{line}. ACTIVE - {user['name']}")
        line = line + 1
    elif user['admin']:
        print(f"{line}. (ADMIN) {user['name']}")
        line = line + 1
    else:
        print(f"{line}. {user['name']} is nothing.")
        line = line + 1
