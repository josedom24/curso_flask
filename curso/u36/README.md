sudo docker run --name servidor_mysql -e MYSQL_DATABASE=tienda -e MYSQL_ROOT_PASSWORD=asdasd -d mysql


sudo docker run --name mytienda -p 8080:80 --link servidor_mysql:mysql -d tienda




sudo docker exec -i -t mytienda /bin/bash
root@5db96abf79b3:/var/www/html/tienda_videojuegos# python3 manage.py create_admin