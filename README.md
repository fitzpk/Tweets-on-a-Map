# Tweets-on-a-Map
Real-time tweets displayed on a leaflet driven digital map. 

Currently tracking: #PGATOUR Tweets.

<a href="https://fitzpk.github.io/Tweets-on-a-Map/">Click Here to Open the App</a>

Using the Tweepy Python module, tweets that contain a particular phrase are streamed, exported into a json file, and then manipulated. The json data is then pushed to Github in 10 minute intervals (subject to change as topics/phrases change), where it is made available for the Leaflet, Javascript and jQuery based web map found in the demo above.

As of April 2020, a sentiment analysis feature has been added to this application. Using a hyper-tuned logistic regression model trained on the sentiment140 dataset, the sentiment or opinion of each new tweet is now predicted and categorized as either positive or negative. Tweets categorized as positive are displayed with a blue marker, and those categorized as negative are displayed with a red marker. Thanks to <a href="https://www.amcharts.com/">amCharts</a> the results are further summarized in a simple donut chart. Mmmm donuts.

