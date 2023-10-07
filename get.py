import os
import requests
import csv

# download file directory
directory_path = './images'

# create directory if not exist
if not os.path.exists(directory_path):
  os.makedirs(directory_path)

# Get links from CSV file
csv_file_path = 'links.csv'
with open(csv_file_path, 'r') as file:
  reader = csv.reader(file)
  next(reader)  # Skip if title exist
  for row in reader:
    image_url = row[0]  # Get links from first row
    image_name = os.path.basename(image_url)
    image_path = os.path.join(directory_path, image_name)

    # Check image if exist in folder
    if not os.path.exists(image_path):
      try:
        response = requests.get(image_url)
        if response.status_code == 200:
          with open(image_path, 'wb') as image_file:
            image_file.write(response.content)
          print(f"Download: {image_name}")
        else:
          print(f"Failed to download: {image_name}, status code: {response.status_code}")
      except Exception as e:
        print(f"There was an error while downloading {image_name}: {str(e)}")
    else:
      print(f"The image {image_name} already exists, skip it")

print("Ready!")
