import os
import numpy as np
import shutil
	
def train_test_directory_split(classes, source_dir='images', target_dir='images_separated'):

	for current_class in classes:
		for sub_dir in ('train', 'validation', 'test'):
			path = '{}/{}_data/{}'.format(target_dir,sub_dir, current_class)
			
			if not os.path.exists(path):
				os.makedirs(path)

		source_path = '{}/{}'.format(source_dir, current_class)

		file_names_currentCls = os.listdir(source_path)
		np.random.shuffle(file_names_currentCls)

		train_file_names, validation_file_names, test_file_names = np.split(np.array(file_names_currentCls),
	                                                          [int(len(file_names_currentCls)*0.6), int(len(file_names_currentCls)*0.8)])

		train_file_names      = [source_path + '/' + file_name for file_name in train_file_names.tolist()]
		validation_file_names = [source_path + '/' + file_name for file_name in validation_file_names.tolist()]
		test_file_names       = [source_path + '/' + file_name for file_name in test_file_names.tolist()]
		
		print('\n=====================================')
		print('Total images in class {} is {}'.format(current_class, len(file_names_currentCls)))
		print('\t{} copied to ../training/{}'.format(len(train_file_names),current_class))
		print('\t{} copied to ../validation/{}'.format(len(validation_file_names),current_class))
		print('\t{} copied to ../testing/{}'.format(len(test_file_names),current_class))

		for file_name in train_file_names:
		    shutil.copy(file_name, '{}/train_data/{}'.format(target_dir, current_class))

		for file_name in validation_file_names:
		    shutil.copy(file_name, '{}/validation_data/{}'.format(target_dir, current_class))

		for file_name in test_file_names:
		    shutil.copy(file_name, '{}/test_data/{}'.format(target_dir, current_class))