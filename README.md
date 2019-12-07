## Purpose
This tool is intended to extract the transit fares from Google Maps.

## Operation
1. Manually set up Google Maps (see `manualsetup.png`)
2. run `scrape.py` from the terminal, and make sure google maps is the only thing on the screen.
3. price extraction program is separate from the scraping program, for now.

### File Descriptions
* scrape.py
    * main file.
* directurlinput.py
    * input the destination and starting stations directly into the browser to avoid some gui manipulation steps.
* openmaps.py
    * this doesn't seem too necessary. It's easier just to manually prepare Google Maps, then start the program.
* fileparser.py
    * loads train station lists.
* getprices.py
    * extract the prices from images and save to a single json object.

## Train Data
This minimum viable product does not include bus routes and stops.
It does not include all the train stations.


### Major Steps
1. Open Google Chrome browser and go to Google Maps
  * Easier to do this manually
2. Enter a destination into the search input.
3. Enter a starting station
4. Screenshot the price
5. Extract the text from the image.
6. Save the text with the station info.
7. Repeat from 3.



