import kopf
import kubernetes
import os
import logging
import requests
import json


@kopf.on.create('poc.zinkworks.com', 'v1', 'TelecoNetwork')
def sample_msg(body, **kwargs):
    logging.info(f"spec : {body}")
    # we need to use retrun and add as below to display them on kubectl get
    return {'text': 'hello world'}


#@kopf.on.create('poc.zinkworks.com', 'v1', 'TelecoNetwork')
#def get_cell(**kwargs):
    # response = requests.get('http://108.141.128.219:8080/data/v1/radio/cell/list')
    # # response.json()
    # if response.status_code == 200:
    #     return {'request': 'Successful'}
    # else:
    #     return {'request': 'Failed'}


#@kopf.on.create('poc.zinkworks.com', 'v1', 'TelecoNetwork')
#def create_pod():
#    pass


@kopf.on.create('poc.zinkworks.com', 'v1', 'TelecoNetwork')
def post_call(body, meta, spec, status, **kwargs):
    headers = {"content-type": "application/json"}
    payload = json.dumps({ "name": "Apple AirPods", "data": {"color": "white", "generation": "3rd", "price": 135}})
    request_url = "https://api.restful-api.dev/objects"
    r = requests.post(request_url, data=payload, headers=headers)
    logging.info(f"From post call getting content : {r.content}")
    global r_id
    r_id = r.json()['id']
    if r.status_code == 200:
        return {'request': 'Successful'}
    else:
        return {'request': 'Failed'}
    # return {'id': r_id}


@kopf.on.update('poc.zinkworks.com', 'v1', 'TelecoNetwork')
def put_call(**kwargs):
    post_call(**kwargs)
    # logging.info("id to update", r_id)
    headers = {"content-type": "application/json"}
    payload = json.dumps({"name": "Apple AirPods", "data": {"color": "blue", "generation": "3rd", "price": 120}})
    request_url = "https://api.restful-api.dev/objects/" + r_id
    r = requests.put(request_url, data=payload, headers=headers)
    logging.info(f"From put call getting content : {r.content}")
    if r.status_code == 200:
        return {'request': 'Put Call Success'}
    else:
        return {'request': 'Put Call Fail'}



# @kopf.on.create('poc.zinkworks.com', 'v1', 'TelecoNetwork')
# def get_api_call():
#     request_url = "https://api.restful-api.dev/objects"
#     rget = requests.get(request_url)
#     print(rget.json())


#@kopf.on.update('poc.zinkworks.com', 'v1', 'TelecoNetwork')
# def patch_call():
#     r_id = post_call()
#     headers = {"content-type": "application/json"}
#     payload = json.dumps({ "name": "Mac", "data": {"color": "blue", "generation": "4th", "price": 1200}})
#     request_url = "https://api.restful-api.dev/objects/" + r_id
#     r = requests.patch(request_url, data=payload, headers=headers)
#
#     logging.info("from patch", r.content)
#     if r.status_code == 200:
#         return {'request': 'Successful'}
#     else:
#         return {'request': 'Failed'}



# @kopf.on.delete('poc.zinkworks.com', 'v1', 'TelecoNetwork')
# def delete_call():
#     post_call()
#     headers = {"content-type": "application/json"}
#     request_url = "https://api.restful-api.dev/objects/" + r_id
#     r = requests.delete(request_url, headers=headers)
#     logging.info("from delete", r.content)
#     if r.status_code == 200:
#         return {'request': 'Successful'}
#     else:
#         return {'request': 'Failed'}