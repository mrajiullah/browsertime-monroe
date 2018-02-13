import json
import sys

file=sys.argv[1]
with open(file) as data_file:
	har_stats = json.load(data_file)

	if har_stats["IMSIMCCMNC"]==24001:
		Ops="Telia (SE)"
	if har_stats["IMSIMCCMNC"]==24201:
		Ops="Telenor (NO)"
	if har_stats["IMSIMCCMNC"]==24008:
		Ops="Telenor (SE)"
	if har_stats["IMSIMCCMNC"]==24002:
		Ops="Tre (SE)"
	if har_stats["IMSIMCCMNC"]==22201:
		Ops="TIM (IT)"
	if har_stats["IMSIMCCMNC"]==21404:
		Ops="Yoigo (ES)"
	
	if har_stats["IMSIMCCMNC"]==22210:
		Ops="Vodafone (IT)"
	if har_stats["IMSIMCCMNC"]==24202:
		Ops="Telia (NO)"
		
	if har_stats["IMSIMCCMNC"]==24214:
		Ops="ICE (NO)"
	if har_stats["IMSIMCCMNC"]==22288:
		Ops="Wind (IT)"
	if har_stats["IMSIMCCMNC"]==21403:
		Ops="Orange (ES)"
	
	if har_stats["IMSIMCCMNC"]==24001:
		Country="SE"
	if har_stats["IMSIMCCMNC"]==24201:
		Country="NO"
	if har_stats["IMSIMCCMNC"]==24008:
		Country="SE"
	if har_stats["IMSIMCCMNC"]==24002:
		Country="SE"
	if har_stats["IMSIMCCMNC"]==22201:
		Country="IT"
	if har_stats["IMSIMCCMNC"]==21404:
		Country="ES"
	
	if har_stats["IMSIMCCMNC"]==22210:
		Country="IT"
	if har_stats["IMSIMCCMNC"]==24202:
		Country="NO"
			
	if har_stats["IMSIMCCMNC"]==24214:
		Country="NO"
	if har_stats["IMSIMCCMNC"]==22288:
		Country="IT"
	if har_stats["IMSIMCCMNC"]==21403:
		Country="ES"

print("{},{},{},{},{},{},{},{},{}".format(har_stats["NodeId"],Ops,Country,har_stats["browser"],har_stats["Protocol"],har_stats["url"], float(har_stats["browserScripts"][0]["timings"]["pageTimings"]["pageLoadTime"])/1000,float(har_stats["browserScripts"][0]["timings"]["rumSpeedIndex"])/1000,float(har_stats["browserScripts"][0]["timings"]["firstPaint"])/1000))
