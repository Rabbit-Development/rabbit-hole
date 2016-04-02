from flask import request, abort, make_response, send_file, render_template, url_for
from storage.filestorage import fetch_image, fetch_random, store_image
from image_service import controller
import json, datetime, io

@controller.route("/")
def hello():
	return make_response("Hello there!")


@controller.route("/i/", methods=['GET'])
def down_the_rabbit_hole():
	print('Going down the rabbit hole to get something random...')
	return "<img src=" + url_for('static', filename=fetch_random()) +  ">"

@controller.route("/i/<gallery_id>/<image_id>", methods=['GET'])
def retrieve_galler_image(gallery_id, image_id):
	print('Looking for something specific in the rabbit hole...')
	return io.BytesIO(fetch_image(gallery_id, image_id))

@controller.route("/i/<image_id>", methods=['GET'])
def retrieve_image(image_id):
	print('Looking for something semi-specific in the rabbit hole...')
	return send_file(io.BytesIO(fetch_image(image_id)))

@controller.route("/u/", methods=['POST', 'GET'])
def store_image_in_storage():
	print('Someone is approaching the rabbit hole...')
	if request.method == 'POST':
		print('Throwing something down the rabbit hole...')
		file = request.files['image']
		gallery = request.form['gallery']
		if store_image(gallery, file) != 0:
			abort(500)
			print('Ehm... It dissappeared...')
	return '''
	<!doctype html>
    <title>Upload new Image</title>
    <h1>Upload new Image</h1>
    <form action="" method=post enctype=multipart/form-data>
		<label>Gallery</label><input type=text name=gallery>
		<br>
		<label>Image</label><input type=file name=image>
		<input type=submit value=Upload>
    </form>
	'''
