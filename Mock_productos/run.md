# MOCK DE PRODUCTOS
## Como ejecutar el proceso de app web para consulta de productos
Los archivos necesarios para ejecutar correctamente el Mock de productos son:
* simulacion_productos.html : es la pagina web que tiene codigo interno para conexión a la API de productos
* generar_datos.py : es el codigo utilizado para generar la lista de productos, vendedores y categorias con la información necesaria para darle una funcionalidad de simulador casi real de la compra de productos, sin incluir funcionalidades como comprar, carrito de compras, acceso a tienda del vendedor 
* api_productos.py : es el codigo que se utilizó con Flask para exponer los path del endpoint de productos

En un entorno limpio, se debe empezar por generar_datos que genera los 3 json files indicados, luego ejecutar api_prodcutos para subir el endpoint que permita obtener productos desde la app web, el url con esta solución es Localhost:5000

Se incluyó después de la entrega una version modificada de la api__productos en AWS usando Lambda y API gateway, el url se entrega modificado en el repo, asi no habria que generar los json files, ni usar el localhost

Url en AWS: https://6antj8ttfe.execute-api.us-east-1.amazonaws.com/Prod/api