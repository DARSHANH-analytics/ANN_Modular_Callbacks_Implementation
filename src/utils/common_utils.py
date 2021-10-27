import yaml
import time
import os

def read_config(config_path):
    print(f'config_path --> {config_path}')
    with open(config_path) as config_file:
        content = yaml.safe_load(config_file)
    return content

def get_log_path(log_dir = 'logs/fit'):
    unique_filename = time.strftime('log_%Y-%m-%d-%H-%M-%S')
    log_path = os.path.join(log_dir,unique_filename)
    print(f'Savings logs at :{log_path}')
    return log_path