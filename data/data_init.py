from data_utils import *

def data_processing():
    process_func_map = {
        'P12': process_p12data,
        'P19': process_p19data,
        'MIMICIII': process_mimiciii,
    }
    for data_name in ['P12', 'P19', 'MIMICIII']:
        data_path = './data/rawdata/'+data_name
        os.makedirs(os.path.dirname("./data/processed_data/"+data_name+"/"), exist_ok=True)
        processed_data = process_func_map[data_name](data_path)
        print('parsed data:', len(processed_data))


if __name__ == '__main__':
    data_processing()
    print('done')
