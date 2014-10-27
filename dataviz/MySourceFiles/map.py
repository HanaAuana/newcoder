"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON-like form, visualize in graphs, and plot as a map.

Part III: Take the data we parsed earlier and create a different format
for rendering a map. Here, we parse through each line item of the
CSV file and create a geojson object, to be collected into one geojson
file for uploading to gist.github.com.
"""

import geojson

import parse as p


def create_map(data_file):
    """Creates a GeoJSON file.

    Returns a GeoJSON file that can be rendered in a GitHub
    Gist at gist.github.com.  Just copy the output file and
    paste into a new Gist, then create either a public or
    private gist.  GitHub will automatically render the GeoJSON
    file as a map.
    """

    #Define GeoJSON type
    geo_map = {"type": "FeatureCollection"}

    #Define empty list to collect points
    item_list = []

    #Iterate over data, create GeoJSON using enumerate()
    for index, line in enumerate(data_file):

        #Skip zero coordinates
        if line['X'] == "0" or line['Y'] == "0":
            continue
        #Setup a new dictionary for each interation
        data = {}

        #Build item for GeoJSON from data fields
        data['type'] = 'Feature'
        data['id']   = index
        data['properties'] = {'title': line['Category'],
                                'description': line['Descript'],
                                'date': line['Date']}
        data['geometry'] = {'type': 'Point',
                            'coordinates': (line['X'], line['Y'])}

        #Add data dictionaries to item_list
        item_list.append(data)
    #For each point, add point to dictionary.
    for point in item_list:
        #Use setdefault and append each point to its list
        geo_map.setdefault('features', []).append(point)

    #Write GeoJSON to file
    with open('file_sf.geojson', 'w') as f:
        f.write(geojson.dumps(geo_map))

def main():
    data = p.parse(p.MY_FILE, ",")

    return create_map(data)

if __name__ == '__main__':
    main()
