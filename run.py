from pynmeagps import NMEAReader
import geojson
from geojson import LineString, Feature

file_path = input("Provide path to NMEA file: ")

file_name = file_path.split("\\")[-1].split(".")[0]

with open(file_path) as f:
    lines = f.readlines()

cords = []
date = ""

for line in lines:
    if line.startswith("$GPRMC"):
        parsed_line = NMEAReader.parse(f'{line}\r\n')
        date = parsed_line.date
        cords.append((parsed_line.lon, parsed_line.lat))

linestring = LineString(cords)

feature = Feature(geometry=linestring, properties={"country": "Italy", "date": str(date)})

dump = geojson.dumps(feature, sort_keys=True)

with open(f"geojson_output/{file_name}.geojson", "w") as g:
    g.writelines(dump)
