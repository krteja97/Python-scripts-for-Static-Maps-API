import ssl;
import urllib.request,urllib.parse,urllib.error;
import json;

api_key = 'Bt------------------------uY';
serviceurl = 'https://maps.googleapis.com/maps/api/staticmap?';

#ssl ..This is for HTTPS
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#create dictionary
params = dict();
center = input("Enter Location-- ");
zoom = input("enter the zoom level required-- ");
size = input("enter the wdith and height -- ");
maptype = input("roadmap, satellite, hybrid, and terrain -- ");
format1 = input("png jpg png32-- ");

params["key"] = api_key;
params["center"] = center;
params["zoom"] = zoom;
params["size"] = size;
params["maptype"] = maptype;
params["format"] = format1;

url = serviceurl + urllib.parse.urlencode(params);
print(url);
