from jinja2 import Template

temp1="Hola {{nombre}}"
print(Template(temp1).render(nombre="Pepe"))

