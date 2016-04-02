from storage import gfs
from PIL import Image
import random, io, os

def fetch_image(gallery, image_name):
    query_results = []
    for image in gfs.find({"filename":image_name}, {"gallery":gallery}):
        query_results.append(image)
    return gfs.find_one(
        {"filename":query_results[random.randint(0, len(query_results)-1)]},
        {"gallery":gallery}
        ).read()

def fetch_image(image_name):
    query_results = []
    for image in gfs.find({"filename":image_name}):
        query_results.append(image)
    return gfs.find_one(
        {"filename":query_results[random.randint(0, len(query_results)-1)]}
    ).read()

def fetch_random():
    all_images = gfs.list()
    random_image = random.randint(0, len(all_images)-1)
    selected_image = gfs.find_one({"filename":all_images[random_image]})
    path = "./static/" + selected_image.filename
    filetype = selected_image.filename.split(".",1)[1]
    image = Image.open(io.BytesIO(selected_image.read()))
    image.save(path, filetype)
    return selected_image.filename

def store_image(gallery, image):
    gfs.put(image, filename=image.filename, gallery_name=gallery)
    return 0
