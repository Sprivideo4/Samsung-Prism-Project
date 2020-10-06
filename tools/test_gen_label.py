import os


dataset_path = '/content/images_test'
label_path = '/content/drive/My Drive/samsung/labels'

if __name__ == '__main__':
    with open('/content/drive/My Drive/samsung/labels/category.txt') as f:
        categories = f.readlines()
        categories = [c.strip().replace(' ', '_').replace('"', '').replace('(', '').replace(')', '').replace("'", '') for c in categories]
    assert len(set(categories)) == 5
    dict_categories = {}
    for i, category in enumerate(categories):
        dict_categories[category] = i

    print(dict_categories)
    files_input = ['CVAE_test.csv']
    files_output = ['test_videofolder.txt']
    for (filename_input, filename_output) in zip(files_input, files_output):
        count_cat = {k: 0 for k in dict_categories.keys()}
        with open(os.path.join(label_path, filename_input)) as f:
            lines = f.readlines()[1:]
        folders = []
        idx_categories = []
        categories_list = []
        for line in lines:
            line = line.rstrip()
            items = line.split(',')
            this_category = ''
            folders.append(items[0])
            if "clapping" in items[0]:
            	this_category = 'clapping'
            elif "dancing" in items[0]:
            	this_category = 'dancing'
            elif "musical" in items[0]:
            	this_category = 'musical_instruments'
            elif "singing" in items[0]:
            	this_category = 'singing'
            elif "travel" in items[0]:
            	this_category = 'travel'
            categories_list.append(this_category)
            idx_categories.append(dict_categories[this_category])
            count_cat[this_category] += 1
        print(max(count_cat.values()))
        assert len(idx_categories) == len(folders)
        missing_folders = []
        output = []
        for i in range(len(folders)):
            curFolder = folders[i]
            curIDX = idx_categories[i]
            # counting the number of frames in each video folders
            img_dir = os.path.join(dataset_path, categories_list[i], curFolder)
            print(img_dir)
            if not os.path.exists(img_dir):
                missing_folders.append(img_dir)
                # print(missing_folders)
            else:
                dir_files = os.listdir(img_dir)
                output.append('%s %d %d'%(os.path.join(categories_list[i], curFolder), len(dir_files), curIDX))
            print('%d/%d, missing %d'%(i, len(folders), len(missing_folders)))
        with open(os.path.join(label_path, filename_output),'w') as f:
            f.write('\n'.join(output))
        with open(os.path.join(label_path, 'missing_' + filename_output),'w') as f:
            f.write('\n'.join(missing_folders))

