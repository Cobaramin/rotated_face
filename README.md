# Rotated face
This project was mostly written on Python; web services api helping rotate image based on detected face with PCN (Progressive Calibration Networks).
And this project use a part of PCN code from this [repository](https://github.com/siriusdemon/pytorch-PCN) that using this [paper](https://arxiv.org/pdf/1804.06039.pdf).

## Getting Started
### Prerequisites
  - docker ce
  - docker-compose

for linux user follow this instruction https://docs.docker.com/install/linux/docker-ce/ubuntu/
and https://docs.docker.com/compose/install/ for docker-compose

### Installation
```
$ docker-compose build
$ docker-compose up
```
### Testing
```shell
source python-tests.sh
```

### Usage
#### Curl
```shell
curl --location --request POST "{{hostname}}/fix-orientation" \
--form "file=@{{path to your file}}" --output output.jpg
```

#### Python
```python
import requests
url = '{{hostname}}/fix-orientation'
payload = {}
files = {('file': open('{{path to your file}}','rb')}
headers = {}
response = requests.request('POST', url, headers = headers, data = payload, files = files, allow_redirects=False, timeout=undefined, allow_redirects=false)
print(response.text)
```
***Note::***
- replace {{hostname}} with ```https://peaceful-everglades-90087.herokuapp.com``` or ```0.0.0.0:8000``` when working in development.
- replace {{path to your file}} with your image path eg. ```take-home-yoyo.jpg```.

#### Postman
- Follow up this link:
https://documenter.getpostman.com/view/2148815/S1LsYA7y

<div align="center">
  <img src="img01.png"><br><br>
</div>
