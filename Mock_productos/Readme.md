# Prototipo E-commerce (Mock Mercado Libre)

Este proyecto es un prototipo funcional de una página de producto, similar a Mercado Libre. Está construido con un frontend en **HTML/CSS/JS** que consume datos de una **API REST** desarrollada en **Python con Flask**. Todo el sistema está alimentado por un modelo de datos simulado en archivos **JSON**, generado con IA Generativa para un mayor realismo.

---

## Modelo de Datos: La "Base de Datos" en JSON

El corazón del proyecto es un conjunto de datos simulados. Se optó por archivos **JSON** como una solución ligera y perfecta para prototipos.

### Generación de Datos con IA Generativa (GenAI)

Para asegurar un catálogo de productos variado y con información coherente, se utilizó IA Generativa siguiendo estos pasos:

1.  **Definición de Esquemas:** Se crearon plantillas claras para `productos`, `vendedores` y `categorías`, especificando los campos necesarios (ej: `titulo`, `precio_actual`, `caracteristicas`, `vendedor_id`).
2.  **Prompts de Generación:** Se usaron prompts detallados para pedir a la IA que generara datos realistas. Por ejemplo:
    > "Genera 10 productos tipo smartphone con especificaciones técnicas comunes (RAM, almacenamiento, marca), descripciones de venta, precios en dólares y asociarlos a un vendedor."
3.  **Realismo y Coherencia:** La IA se encargó de crear títulos, descripciones y características coherentes. Los datos numéricos como precios y calificaciones fueron generados dentro de rangos lógicos para simular un mercado real.

### Estructura y Asociación de Datos

Los datos están organizados en archivos JSON interconectados:

* **`productos.json`**: Contiene un array de productos.

* **`vendedores.json`**: Contiene un array de vendedores.

* **`categorias.json`**: Un árbol de categorías que permite la clasificación y la creación de las "migas de pan" (breadcrumbs).

### Indexación de Imágenes

Para evitar el almacenamiento local, el campo `imagenes` en `productos.json` es un array de **URLs que apuntan a imágenes existentes en la web**, lo que permite que el prototipo sea visualmente rico con un costo mínimo de infraestructura.

---

## API Backend: Python + Flask

Se desarrolló una API REST simple utilizando **Python** y el micro-framework **Flask**. Su única responsabilidad es leer los archivos JSON y servir los datos al frontend de manera estructurada.

### Endpoint Principal: `GET /api/producto/{id}`

Este es el endpoint clave utilizado por la página. Su lógica es fundamental para la eficiencia del frontend, ya que con una sola llamada se obtiene toda la información necesaria:

1.  **Recibe un ID de producto** (ej: `/api/producto/1`).
2.  **Busca el Producto Principal:** Encuentra el producto con ese `id` en `productos.json`.
3.  **Busca el Vendedor Asociado:** Usa el `vendedor_id` del producto para encontrar al vendedor en `vendedores.json`.
4.  **Simula "Productos Relacionados":** Filtra `productos.json` para encontrar otros productos que compartan la misma subcategoría.
5.  **Simula "Productos del Vendedor":** Filtra `productos.json` para encontrar todos los productos con el mismo `vendedor_id`.
6.  **Empaqueta y Envía:** Combina toda esta información en **una sola respuesta JSON**.

---

## Frontend y Decisiones de Diseño

El diseño del frontend emula las mejores prácticas de plataformas de e-commerce consolidadas, enfocándose en la claridad, la confianza y la facilidad de acción.

### Estructura de Tres Columnas

La página se organiza en un layout de tres columnas para separar las funciones cognitivas del usuario:

* **Columna Izquierda (Visual):** Dedicada a las imágenes. Permite al usuario evaluar visualmente el producto de forma rápida.
* **Columna Central (Informativa):** Contiene la información descriptiva: título, calificación, características. Responde a la pregunta "¿Qué es este producto?".
* **Columna Derecha (Transaccional):** Es la zona de acción. Muestra el precio, información de envío, stock, los botones de compra y la información del vendedor para generar confianza. Responde a la pregunta "¿Cómo lo consigo y de quién?".

### Flujo de Interacción y Carga de Datos

1.  La página se carga y muestra un indicador de "Cargando...".
2.  El JavaScript extrae el `id` del producto de la URL.
3.  Se realiza una única llamada `fetch` al endpoint `/api/producto/{id}`.
4.  Al recibir la respuesta JSON, varias funciones de JavaScript (`loadProductInfo`, `loadSellerInfo`, etc.) se encargan de tomar los datos e inyectarlos en el HTML.
5.  Una vez renderizados los datos, el indicador de carga se oculta y se muestra el contenido principal de la página.

_________________________

### RETOS ENCONTRADOS

1. Encontrar una forma sencilla de tener articulos reales con información que pueda relacionarse en un ecommerce
2. Encontrar la forma de generar el codigo que se adpte al alyout esperado con muchos parametros a ser variables
3. Generar la API no fue dificil, esperaba poder probarlo y escalarlo mejor en AWS con lambda y API gateway pero el tiempo se me terminó antes de lograr lo esperado en funcionalidades.
