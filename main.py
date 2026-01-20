import os

variables = {}

msg = [
    'IC version 1.0',
    'LeleCodes Copyright (C) 2026'
]

for line in msg:
    print(line)

print()

while True:
    line = input('$ ')
    parts = line.split(' ', 1)

    if len(parts) < 2:
        print('The command needs a parameter')
        continue

    cmd, param = parts[0], parts[1]

    if cmd == 'var':
        variables[param] = None

    elif cmd == 'pis':
        print(param)

    elif cmd == 'pisf':
        if param in variables:
            print(variables[param])
        else:
            print(f'Variable "{param}" not exist')

    elif cmd in variables and param.startswith('$entry'):
        if '_' in param:
            texto = param.split('_', 1)[1]
            print(texto)

        valor = input()
        variables[cmd] = valor

    elif cmd in variables:
        variables[cmd] = param

    elif cmd == 'ntf':
        os.chdir(param)

    elif cmd == 'cfi':
        os.system(f'type nul > {param}')
    
    elif cmd == 'cfo':
        os.mkdir(param)
    
    elif cmd == 'defo':
        os.rmdir(param)
    
    elif cmd == 'defi':
        os.delete(param)

    else:
        print(f'{cmd}: not is command of IC')
