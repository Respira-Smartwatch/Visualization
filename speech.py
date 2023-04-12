import matplotlib.pyplot as plt
import json

data = json.load(open('respira_Danny_2023-04-06.json', 'r'))
phases = ['baseline', 'expiration1', 'rest1', 'expiration2', 'rest2', 'video', 'rest3', 'recitation', 'rest4']
speech = ['speech_happy', 'speech_sad', 'speech_disgust', 'speech_surprise']
output = {}
for i in phases:
	rate = data[i]['stress_rating']
	maximum = data[i]['speech_happy']
	key = 'None'
	for j in speech:
		if data[i][j] > maximum:
			key = j
			maximum = data[i][j]
	if len(maximum) == 0:
		j = ''
		maximum = ''
	output[i] = str(key + str(maximum) + ' &' + ' Stress Rating: ' + str(rate))

for i in output:
	print(i + ': ' + output[i])
