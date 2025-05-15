
from flask import render_template,current_app as app

@app.route('/designs/A-Frame')
def aframe():
    return render_template('designs/A-frame.html') 

@app.route('/designs/Prefabricated-Luxury-house')
def Prefabricated():
    return render_template('designs/prefabricated-Luxury.html') 

@app.route('/designs/Wooden-House')
def wooden_house():
    return render_template('designs/wooden-house.html') 

@app.route('/designs/Wooden-Resort')
def wooden_resort():
    return render_template('designs/wooden-resort.html') 

@app.route('/designs/A-Frame-Cottages')
def aframecottages():
    return render_template('designs/a-frame-cottages.html') 

@app.route('/designs/Portable-House')
def portable_house():
    return render_template('designs/portable-house.html') 

@app.route('/designs/Prefabricated-Wooden-house')
def Prefab_wooden():
    return render_template('designs/prefab-wooden-house.html') 

@app.route('/designs/Modular-Cottage')
def modular():
    return render_template('designs/modular-cottage.html') 

@app.route('/designs/Prefabricated-house')
def Prefab_house():
    return render_template('designs/prefab-house.html') 

@app.route('/designs/Portable-Cabin')
def portable_cabin():
    return render_template('designs/portable-cabin.html') 

@app.route('/designs/Office-Cabin')
def office_cabin():
    return render_template('designs/office-cabin.html') 

@app.route('/designs/Double-Storey-Houses')
def double_storey():
    return render_template('designs/double-storey.html') 
