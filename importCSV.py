import bpy
import csv
import numpy
import mathutils


# Set Parameters
# Filepath to CSV
filepath = "Replace_with_filepath_to_CSV"

# Name of Blender Object
obj_name = "CSV_to_Points"

# Initialize an empty dictionary to store attributes
attributes = {}

#Create empty list for vertex data
data = []
verts = []

# Read CSV File

with open(filepath, mode='r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    # Dynamically create dictionary keys based on CSV headers
    for header in reader.fieldnames:
        attributes[header] = []

    # Populate the dictionary
    for row in reader:
        data.append(row)
        for key in attributes.keys():
            try:
                # Assuming all values are to be converted to float, adjust if necessary
                value = float(row[key]) if row[key] else 0.0
                attributes[key].append(float(value))
            except KeyError:
                print(f"KeyError: Column '{key}' not found in CSV headers.")

# Append placeholder values for vertex position
for row in data:
    verts.append(mathutils.Vector((float(0), float(0), float(0))))
    
#Create Mesh

mesh_data = bpy.data.meshes.new(obj_name + '_data')
obj = bpy.data.objects.new(obj_name, mesh_data)
bpy.context.scene.collection.objects.link(obj)
mesh_data.from_pydata(verts, [], [])

# Create attributes and populate with data

for key in attributes.keys():
    key_name = key
    print(key_name)
    val = numpy.array(attributes[key])
    obj.data.attributes.new(name=key_name+'_val', type='FLOAT', domain='POINT')
    obj.data.attributes[key_name+'_val'].data.foreach_set('value',val)
