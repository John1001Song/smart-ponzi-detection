import os

DATASET_PATH = '../dataset/'
# FOLDERS = ['ponzi_dataset/bytecode/', 'non_ponzi_dataset/bytecode/']
FOLDERS = ['ponzi_dataset/bytecode/']
evmdis_bin_path = '/Users/Jinyue/go/bin/evmdis'

def start():
    [convert_all_file(folder) for folder in FOLDERS]


def convert_all_file(folder):
    i = 0
    for filename in os.listdir(DATASET_PATH + folder):
        if not filename.endswith('.json'):
            continue
        i += 1
        print(f"{i}: {filename}")
        bcode_to_opcode(DATASET_PATH + folder + filename)


def bcode_to_opcode(path):
    # path = path.replace('Master Project', 'Master\ Project')
    print('cat ' + path + ' | ' + evmdis_bin_path + ' > ' + path.replace('bytecode', 'opcode'))
    os.popen('cat ' + path + ' | ' + evmdis_bin_path + ' > ' + path.replace('bytecode', 'opcode'))

if __name__ == '__main__':
    start()
