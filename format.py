import fastai2
from fastai2.vision.all import *
from fastai2.vision.widgets import *
from fastai2.basics import *

import csv

image_path = Path("whole sky images")
images = get_image_files(image_path)
csv_name = "properties.csv" 
stats = {
	"Clear sky" : 0,
	"Partial cloud" : 0,
	"Overcast sky" : 0
}

with open(csv_name, 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['sky_type'] != '':
			stats[row['sky_type']] += 1

print(stats)