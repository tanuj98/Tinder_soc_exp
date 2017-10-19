# Get the number of photos in directory
processed_numPhotos = len([f for f in os.listdir(imagePath) if os.path.isfile(os.path.join(imagePath, f))])

	# Iterate through list of subjects
for subject in subjects:
		
		# Get the subject ID
		sid = subject['_id']
		
		# Gets a list of pictures of the subject
		pictures = subject['photos']

		# Iterate through and save the pictures of the subject
		for picIndex in range(len(pictures)):

			# Get the URL for the largest cropped photo
			processed_picURL = str(pictures[picIndex]['processedFiles'][0]['url'])

			# Get the photo and save
			urllib.request.urlretrieve(processed_picURL, imagePath + '/' + sid + '_' + str(processed_numPhotos) + '.jpg')
			processed_numPhotos += 1
