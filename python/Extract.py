#-------------------------------------------------------------
# Kevin Fitzgerald - 2018
# 
# Extract attributes from existing json file, perform string
# manipulation and export to geojson file 
#-------------------------------------------------------------

import json, datetime

# Create function that takes a 3 letter month and returns the calendar number
def monthTOnumber(string):
    m = {
        'jan': '01',
        'feb': '02',
        'mar': '03',
        'apr': '04',
        'may': '05',
        'jun': '06',
        'jul': '07',
        'aug': '08',
        'sep': '09',
        'oct': '10',
        'nov': '11',
        'dec': '12'
        }
    s = string.strip()[:3].lower()
    out = m[s]
    return out

# Open a file called pytweets in read mode 
with open('/Users/kf/Desktop/pytweets.json', 'r') as f:
    # Create dictionary called geo_data
    geo_data = {
        "type": "FeatureCollection",
        "features": []
    }
    # Iterate over each line in pytweets.json
    for line in f:
        
        # Set tweet to store each line as json - enabling us to call attributes
        tweet = json.loads(line)

        # Store time of tweet and partition it
        date = tweet['created_at']
        yyyy = date.split(' ')[5]
        mmm = date.split(' ')[1]
        dd = date.split(' ')[2]
        time = date.split(' ')[3]
        # Convert month name to month number
        mm = monthTOnumber(mmm)
        # Combine date variable together to match python date format
        tweettime = yyyy+'-'+mm+'-'+dd+' '+time
        # Get the date as of one week ago and trim time to match the tweets
        weekago = str(datetime.datetime.now() - datetime.timedelta(days=7))
        weekago = weekago[0:19]
        
        # Only manipulate tweets that have a place attribute AND are not more
        # than a week old
        if tweet['place'] and (tweettime > weekago):
            
            # Store tweet coordinates and convert to string for manipulation
            location = tweet['place']['bounding_box']['coordinates']
            ts = str(location)
            
            # Split coordinates and grab the 2nd coordinate (NW) - Clean XY1
            XY = ts.split(']')[1]
            XY = XY.replace('[','')
            
            # Split X and Y values of 2nd coordinate and store as float
            Y1 = float(XY.split(',')[1])
            X1 = float(XY.split(',')[2])
            
            # Split coordinates and grab the 4th coorindate (SE) - Clean XY2
            XY2 = ts.split(']')[3]
            XY2 = XY2.replace('[','')
            
            # Split X and Y values of 4th coordinate and store as float
            Y2 = float(XY2.split(',')[1])
            X2 = float(XY2.split(',')[2])
            
            # Calculate centroid of tweet polygon and round to 7 decimals
            NewX = round(((X1+X2)/2),7)
            NewY = round(((Y1+Y2)/2),7)
            
            # Convert back to string
            Centroid = str((NewY, NewX))
            
            # Replace unnecessary characters
            Centroid = Centroid.replace('(','[')
            Centroid = Centroid.replace(')',']')
            
            # Append geojson formatting text to centroid variable
            Centroid = "{''type'':''Point'', ''coordinates'':"+Centroid+'}'
            
            # Create geojson properties and geometry via tweet attributes
            geo_json_feature = {
                "type": "Feature",
                "properties": {
                    "ProfilePic": tweet['user']['profile_image_url'],
                    "Name": tweet['user']['name'],
                    "Handle": tweet['user']['screen_name'],
                    "Tweet": tweet['text'],
                    "TweetLink": tweet['id_str'],
                    "Place": tweet['place']['name'],
                    "Time": tweet['created_at']
                },
                "geometry": Centroid
            }
            # Append geojson data to features array in the geo_data dictionary
            geo_data['features'].append(geo_json_feature)
 
# Open geojson file in write mode and export json data
with open('/Users/kf/Tweets-on-a-map/geo_data.geojson', 'w') as fout:
    fout.write(json.dumps(geo_data, indent=4))

# Open geojson file in read mode and store all text in a variable
with open('/Users/kf/Tweets-on-a-map/geo_data.geojson', 'r') as fout:
  filedata = fout.read()

# Perform string manipulation on variable with geojson text
filedata = filedata.replace("''", '"')
filedata = filedata.replace('"{"type', '{"type')
filedata = filedata.replace('}",', '},')

# Finally open geojson file again in write mode and update it with
# the text from the manipulated variable
with open('/Users/kf/Tweets-on-a-map/geo_data.geojson', 'w') as fout:
  fout.write(filedata)
  fout.close()


