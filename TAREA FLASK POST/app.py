from flask import Flask, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)



app = Flask (__name__)
with open ('data.json') as json_file:
  my_json = json.load(json_file)


def mensaje():
  mensaje = 'Hola desde el metodo'
  return "alert('" + mensaje + "')"


  @app.route('crear' , methods = ['GET' , 'POST'])
  def crear():
    if request.method == 'POST':
      _id = request.form['id']
      _type = request.form['type']
      _name = request.form['name']
      _image = request.form ['image']
      _thumbnail = request.form['_thumbnail']
      

      my_json['data'].append({"id":_id, "type":_type, "name":_name, "image":{"url":_image}, "_thumbnail":{"url":_thumbnail}})
      return redirect(url_for('index'))
    template = env.get_template('form.html')
    return template.render()


  @app.route('/nombre')
  def nombre():
    return 'Nickolas Peter Nolte Brol'

  @app.route('/edad')
  def edad():
    return '19 años'

  @app.route('/carnet')
  def carnet():
    return '20200561'
