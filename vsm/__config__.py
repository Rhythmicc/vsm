import os
import json
from QuickProject import user_root, user_lang, QproDefaultConsole, QproInfoString, _ask

enable_config = True
config_path = os.path.join(user_root, ".vsm_config")

questions = {
    'sudo': {
        'type': 'confirm',
        'message': 'Do you want to use sudo to install packages?' if user_lang != 'zh' else '是否使用sudo安装依赖?',
        'default': True
    },
}

def init_config():
    with open(config_path, "w") as f:
        json.dump({i: _ask(questions[i]) for i in questions}, f, indent=4, ensure_ascii=False)
    QproDefaultConsole.print(QproInfoString, f'Config file has been created at: "{config_path}"' if user_lang != 'zh' else f'配置文件已创建于: "{config_path}"')
    QproDefaultConsole.print(QproInfoString, 'You can add service to the config file. And format is like: ' if user_lang != 'zh' else '您可以在配置文件中添加服务. 格式如下: ')
    QproDefaultConsole.print(QproInfoString, '"service": {"path": "folder path", "port": 8080}')


class vsmConfig:
    def __init__(self):
        if not os.path.exists(config_path):
            init_config()
        with open(config_path, "r") as f:
            self.config = json.load(f)
    
    def select(self, key):
        if key not in self.config and key in questions:
            self.update(key, _ask(questions[key]))
        return self.config.get(key, None)
    
    def update(self, key, value):
        self.config[key] = value
        with open(config_path, "w") as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)

    def valid_port(self, port):
        for item in self.config:
            if item in ['sudo']:
                continue
            if self.config[item].get('port', -1) == port:
                return False
        return True

    def valid_service(self, service):
        return service in self.config
