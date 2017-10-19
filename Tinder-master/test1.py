import json
import features
import config
import urllib.request
import os, os.path
import requests
import tinder_api as api
import sys
api.get_auth_token(config.fb_access_token,config.fb_user_id);
recommend = api.get_recommendations()['results'];
#print(api.headers);
#print(recommend);
file_object  = open("subject_id.txt", "a+")
file_object1 = open("right.txt","a+")
imagePath = 'tt\matches'
imagePath1 = "E:/tinder/Tinder-master/tt/non"
processed_numPhotos = len([f for f in os.listdir(imagePath) if os.path.isfile(os.path.join(imagePath, f))])
processed_numPhotos1 = len([f for f in os.listdir(imagePath1) if os.path.isfile(os.path.join(imagePath1, f))])

for subject in recommend:
		
		# Get the subject ID
		sid = subject['_id']
		file_object.write(sid + "\n")
		print(subject['bio'])
		age = features.calculate_age(subject['birth_date'])
		print(age)
		var = input("Press in y for yes, and n for no")
		if var == "y":
				file_object1.write(sid+"\n")
		
				# Gets a list of pictures of the subject
				pictures = subject['photos']

		# Iterate through and save the pictures of the subject
				for picIndex in range(len(pictures)):

			# Get the URL for the largest cropped photo
					processed_picURL = str(pictures[picIndex]['processedFiles'][0]['url'])

					# Get the photo and save
					urllib.request.urlretrieve(processed_picURL, imagePath + '/' + sid + '_' + str(processed_numPhotos) + '.jpg')
					processed_numPhotos += 1
		else:
					
		
		
	
							pictures = subject['photos']
						
		# Iterate through and save the pictures of the subject
							for picIndex in range(len(pictures)):

			# Get the URL for the largest cropped photo
									processed_picURL = str(pictures[picIndex]['processedFiles'][0]['url'])

			# Get the photo and save
									urllib.request.urlretrieve(processed_picURL, imagePath1 + '/' + sid + '_' + str(processed_numPhotos1) + '.jpg')
									processed_numPhotos1 += 1

	

