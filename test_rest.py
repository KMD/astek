import requests
import json


def test_client_get_200():
	r = requests.get('http://127.0.0.1:5000/client/')
	assert r.status_code == 200
	
def test_client_get():
	r = requests.get('http://127.0.0.1:5000/client/')
	assert isinstance(r.json(), list)
	
def test_client_get_200_id():
	r = requests.get('http://127.0.0.1:5000/client/1')
	assert r.status_code == 200

	
def test_client_create():
	params = {'name':'Adam', 'ip-address':'127.0.0.1'}
	r = requests.post('http://127.0.0.1:5000/client/', params=params)
	assert r.json()['result'] == 'success'
	
def test_client_put_200():
	r = requests.put('http://127.0.0.1:5000/client/')
	assert r.status_code == 200

def test_client_delete_200_id():
	r = requests.delete('http://127.0.0.1:5000/client/1')
	assert r.status_code == 200
	
def test_dataset_get_200():
	r = requests.get('http://127.0.0.1:5000/dataset/')
	assert r.status_code == 200
	
def test_dataset_get_200_id():
	r = requests.get('http://127.0.0.1:5000/dataset/1')
	assert r.status_code == 200

def test_dataset_post_200():
	r = requests.post('http://127.0.0.1:5000/dataset/')
	assert r.status_code == 200
	
def test_dataset_put_200():
	r = requests.put('http://127.0.0.1:5000/dataset/')
	assert r.status_code == 200

def test_dataset_delete_200_id():
	r = requests.delete('http://127.0.0.1:5000/dataset/1')
	assert r.status_code == 200
