# Tweets-on-a-Map
Real-time tweets displayed on a leaflet driven digital map. 

Currently tracking: PGA TOUR events.

<a href="https://fitzpk.github.io/Tweets-on-a-Map/">Click Here to Open the App</a>

Using the Tweepy Python module, tweets that contain a particular phrase are streamed, exported into a json file, and then manipulated. The json data is then pushed to Github in 10 minute intervals (subject to change as topics/phrases change), where it is made available for the Leaflet, Javascript and jQuery based web map found in the demo above.
