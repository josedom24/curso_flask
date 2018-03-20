# Finalización de la compra 

En esta última unidad vamos a simular el final de la compra, en este caso hemos simplificado mucho este proceso, simplemente vamos a mostrar la lista de los artículos comprados, el precio final y vamos a actualizar el stock de cada uno de los artículos.

## Realizar pedido

En la plantilla `carrito.hrml` hemos introducido un enlace al la ruta `pedido`:

	<a class="btn btn-primary" href="{{url_for('pedido')}}" role="button">Comprar</a>

En esta ruta vamos a realizar las siguientes acciones:

* Vamos a leer los datos de la cookie
* Calculamos el precio final de la compra.
* Actualizamos en cada artículo la cantidad restando los artículos que hemos comprado.
* Borramos la cookie
* Utilizando la plantilla `pedido.html` mostramos los artículos y el precio final.

{% include "../../adsense.md" %}

El código quedaría de la siguiente forma:

	@app.route('/pedido')
	@login_required
	def pedido():
		try:
			datos = json.loads(request.cookies.get(str(current_user.id)))
		except:
			datos = []
		total=0
		for articulo in datos:
			total=total+Articulos.query.get(articulo["id"]).precio_final()*articulo["cantidad"]
			Articulos.query.get(articulo["id"]).stock-=articulo["cantidad"]
			db.session.commit()
		resp = make_response(render_template("pedido.html",total=total))
		resp.set_cookie(str(current_user.id),"",expires=0)
		return resp

## Código ejemplo de esta unidad

[Código](https://github.com/josedom24/curso_flask/tree/master/ejemplos/u32)

{% include "../../adsense2.md" %}