import os
from libmiyoushe import lib_version, lib_name

os.system('python setup.py bdist_wheel')
# dir_list = os.listdir('dist')
# file_name = ''
# for file in dir_list:
#     if lib_version in file.split('-') and file.endswith('.whl') and file.startswith(lib_name):
#         file_name = file
#         break
# file_path = os.path.abspath(os.path.join('.', 'dist', file_name))
# os.system(f'twine upload ./dist/{file_name}')