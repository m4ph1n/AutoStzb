import yaml
from pywebio.output import use_scope, put_button, put_column, put_text
from pywebio.pin import put_input, pin_on_change
from config.config import globalConfig


def set_new_data(instance):
    def set_data(val):
        instance.data['Simulator']['url'] = val
        instance.write()
    return set_data


class LoadConfig:
    def __init__(self, data, path):
        self.data = data
        self.path = path

    def write(self):
        with open(self.path, 'w') as f:
            yaml.dump(self.data, f)

    def renderConfig(self):
        with use_scope('center', clear=True):
            put_column([
                put_text('请输入模拟器地址'),
                put_input('simulator', value=self.data['Simulator']['url'])
            ])
        pin_on_change('simulator', set_new_data(self), clear=True)

    def render(self):
        with use_scope('config', clear=True):
            put_button('配置', onclick=self.renderConfig)


change_config = LoadConfig(globalConfig, globalConfig['Simulator']['path'])
