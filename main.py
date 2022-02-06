import json # deals with data pulled from api
import turtle # displays the graphics
import time
import urllib.request # deals with data pulled from api
import webbrowser # opens txt file into full application


url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open('in_space.txt', 'w')
file.write('There are ' + str(result['number']) + ' astronauts in space at the moment: \n\n')
people = result['people']
for p in people:
    file.write(p['name']+ '' + '\n')
file.close()
webbrowser.open('in_space.txt')

# Next is the world map and ISS icon
# need to implement Shenzhou 13 and track it together with the ISS /separate above astronauts by craft

screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)
#screen.setworldcoordinates(-200,-100,200,100)

#remove close,minimaze,maximaze buttons:
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)

screen.bgpic('physical-world-map.gif')
screen.register_shape('iss_icon.gif')
iss = turtle.Turtle()
iss.shape('iss_icon.gif')
iss.setheading(45)
iss.penup()

while True:

    # Load the current status of the ISS in real-time
    url = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    #Extract location
    location = result['iss_position']
    lat = location['latitude']
    lon = location['longitude']

    # Output long and lat to the terminal
    lat = float(lat)
    lon = float(lon)
    print('\nLatitude: ' + str(lat))
    print('\nLongitude: ' + str(lon))

    # Update the ISS location on the map
    iss.goto(lon, lat)

    # Refresh every 5 seconds
    time.sleep(5)


