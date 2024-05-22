c.ServerProxy.servers = {
    'flask': {
        'command': ['python', 'proxy-flask-app.py'],
        'timeout': 30,
        'launcher_entry': {
            'enabled': True,
            'title': 'Flask App',
        },
    }
}
