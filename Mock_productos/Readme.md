Prototipo E-commerce (Mock Mercado Libre)
Este proyecto es un prototipo funcional de una página de producto, similar a Mercado Libre. Está construido con un frontend en HTML/CSS/JS que consume datos de una API REST desarrollada en Python con Flask. Todo el sistema está alimentado por un modelo de datos simulado en archivos JSON, generado con IA Generativa para un mayor realismo.

🧠 Modelo de Datos: La "Base de Datos" en JSON
El corazón del proyecto es un conjunto de datos simulados. Se optó por archivos JSON como una solución ligera y perfecta para prototipos.

Generación de Datos con IA Generativa (GenAI)
Para asegurar un catálogo de productos variado y con información coherente, se utilizó IA Generativa siguiendo estos pasos:

Definición de Esquemas: Se crearon plantillas claras para productos, vendedores y categorías, especificando los campos necesarios (ej: titulo, precio_actual, caracteristicas, vendedor_id).

Prompts de Generación: Se usaron prompts detallados para pedir a la IA que generara datos realistas. Por ejemplo:

"Genera 10 productos tipo smartphone con especificaciones técnicas comunes (RAM, almacenamiento, marca), descripciones de venta, precios en dólares y asociarlos a un vendedor."

Realismo y Coherencia: La IA se encargó de crear títulos, descripciones y características coherentes. Los datos numéricos como precios y calificaciones fueron generados dentro de rangos lógicos para simular un mercado real.

Estructura y Asociación de Datos
Los datos están organizados en archivos JSON interconectados:

productos.json: Contiene un array de productos.

Claves principales: id, titulo, precio_actual, imagenes (un array de URLs), caracteristicas, vendedor_id y categoria_id.

vendedores.json: Contiene un array de vendedores.

Claves principales: id, nombre, y datos acumulados como ventas_totales y calificacion para simular un historial.

categorias.json: Un árbol de categorías que permite la clasificación y la creación de las "migas de pan" (breadcrumbs).

Indexación de Imágenes
Para evitar el almacenamiento local, el campo imagenes en productos.json es un array de URLs que apuntan a imágenes existentes en la web, lo que permite que el prototipo sea visualmente rico con un costo mínimo de infraestructura.

⚙️ API Backend: Python + Flask
Se desarrolló una API REST simple utilizando Python y el micro-framework Flask. Su única responsabilidad es leer los archivos JSON y servir los datos al frontend de manera estructurada.

Endpoint Principal: GET /api/producto/{id}
Este es el endpoint clave utilizado por la página. Su lógica es fundamental para la eficiencia del frontend, ya que con una sola llamada se obtiene toda la información necesaria:

Recibe un ID de producto (ej: /api/producto/1).

Busca el Producto Principal: Encuentra el producto con ese id en productos.json.

Busca el Vendedor Asociado: Usa el vendedor_id del producto para encontrar al vendedor en vendedores.json.

Simula "Productos Relacionados": Filtra productos.json para encontrar otros productos que compartan la misma subcategoría.

Simula "Productos del Vendedor": Filtra productos.json para encontrar todos los productos con el mismo vendedor_id.

Empaqueta y Envía: Combina toda esta información en una sola respuesta JSON.

🎨 Frontend y Decisiones de Diseño
El diseño del frontend emula las mejores prácticas de plataformas de e-commerce consolidadas, enfocándose en la claridad, la confianza y la facilidad de acción.

Estructura de Tres Columnas
La página se organiza en un layout de tres columnas para separar las funciones cognitivas del usuario:

Columna Izquierda (Visual): Dedicada a las imágenes. Permite al usuario evaluar visualmente el producto de forma rápida.

Columna Central (Informativa): Contiene la información descriptiva: título, calificación, características. Responde a la pregunta "¿Qué es este producto?".

Columna Derecha (Transaccional): Es la zona de acción. Muestra el precio, información de envío, stock, los botones de compra y la información del vendedor para generar confianza. Responde a la pregunta "¿Cómo lo consigo y de quién?".

Flujo de Interacción y Carga de Datos
La página se carga y muestra un indicador de "Cargando...".

El JavaScript extrae el id del producto de la URL.

Se realiza una única llamada fetch al endpoint /api/producto/{id}.

Al recibir la respuesta JSON, varias funciones de JavaScript (loadProductInfo, loadSellerInfo, etc.) se encargan de tomar los datos e inyectarlos en el HTML.

Una vez renderizados los datos, el indicador de carga se oculta y se muestra el contenido principal de la página.

Simulación de Confianza y Urgencia
Elementos como la calificación del vendedor, el número de ventas (+5mil ventas), el badge de "MÁS VENDIDO" y el stock disponible están diseñados para:

Generar Confianza: Un vendedor con buena reputación es más fiable.

Crear Prueba Social: Si muchos lo han comprado, debe ser un buen producto.

Indicar Escasez: Un número limitado de unidades puede incentivar la compra.
RETOS ENCONTRADOS
1. Encontrar una forma sencilla de tener articulos reales con información que pueda relacionarse en un ecommerce
2. Encontrar la forma de generar el codigo que se adpte al alyout esperado con muchos parametros a ser variables
3. Generar la API no fue dificil, esperaba poder probarlo y escalarlo mejor en AWS con lambda y API gateway pero el tiempo se me terminó antes de lograr lo esperado en funcionalidades.
