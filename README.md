# Mapping Geospatial Data with Geometry Nodes in Blender
This repo contains the resources needed to follow along with the tutorial posted to my website [here](https://peteratwoodprojects.wordpress.com). This tutorial covers importing CSV data into Blender and using the Geometry Nodes tools to visualize and animate it. 
## Tutorial.blend
This is the .blend file containing the end result of the tutorial.
## EarthquakeDataRaw.csv
The initial dataset used in the tutorial. This contains the location, depth and magnitude of every earthquake with a magnitude greater than 4.5 since 2019 ([Source](https://earthquake.usgs.gov/earthquakes/map/?extent=1.66969,-134.29688&extent=62.95522,-55.63477)).
## EarthquakeDataClean.csv
The dataset formatted for import into Blender, modified from the original dataset in the following ways:
* All unneeded fields are removed
* The date field has been converted to a frame value
## Recipes.blend
This blend file a series of node groups and materials that offer some interesting ways to experiment with geometry nodes. I'll be updating this with more resources over time. To add these to your own Blender project, first download the .blend file. Then, in your own project, click File > Append, and navigate to either the materials or groups folder to import them into your project. Once a node group has been imported, you can add it to any node tree from the add menu. 
