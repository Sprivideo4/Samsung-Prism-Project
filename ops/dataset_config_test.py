import os

ROOT_DATASET = '/content/drive/My Drive/samsung'  


def return_CVAE(modality):
    filename_categories = 5
    if modality == 'RGB':
        root_data = '/content/images_test'
        filename_imglist_test = ROOT_DATASET+'/labels/test_videofolder.txt'
        prefix = 'img_{:05d}.jpg'
    else:
        raise NotImplementedError('no such modality:' + modality)
    return filename_categories, filename_imglist_test, root_data, prefix

def return_dataset(dataset, modality):
    dict_single = {'CVAE': return_CVAE }
    if dataset in dict_single:
        file_categories, file_imglist_test, root_data, prefix = dict_single[dataset](modality)
    else:
        raise ValueError('Unknown dataset '+dataset)

    file_imglist_test = os.path.join(ROOT_DATASET, file_imglist_test)
    if isinstance(file_categories, str):
        file_categories = os.path.join(ROOT_DATASET, file_categories)
        with open(file_categories) as f:
            lines = f.readlines()
        categories = [item.rstrip() for item in lines]
    else:  # number of categories
        categories = [None] * file_categories
    n_class = len(categories)
    print('{}: {} classes'.format(dataset, n_class))
    return n_class, file_imglist_test, root_data, prefix
