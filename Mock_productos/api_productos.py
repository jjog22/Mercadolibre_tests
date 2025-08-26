from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Permite peticiones desde el frontend

class ProductAPI:
    def __init__(self):
        self.productos = []
        self.vendedores = []
        self.categorias = {}
        self.cargar_datos()
    
    def cargar_datos(self):
        """Carga los datos desde los archivos JSON"""
        try:
            # Cargar productos
            if os.path.exists('productos.json'):
                with open('productos.json', 'r', encoding='utf-8') as f:
                    self.productos = json.load(f)
            
            # Cargar vendedores
            if os.path.exists('vendedores.json'):
                with open('vendedores.json', 'r', encoding='utf-8') as f:
                    self.vendedores = json.load(f)
            
            # Cargar categorías
            if os.path.exists('categorias.json'):
                with open('categorias.json', 'r', encoding='utf-8') as f:
                    self.categorias = json.load(f)
                    
            print(f" Datos cargados: {len(self.productos)} productos, {len(self.vendedores)} vendedores")
            
        except Exception as e:
            print(f">> Error cargando datos: {e}")
    
    def obtener_producto_por_id(self, producto_id):
        """Obtiene un producto específico por ID"""
        for producto in self.productos:
            if producto['id'] == producto_id:
                return producto
        return None
    
    def obtener_vendedor_por_id(self, vendedor_id):
        """Obtiene un vendedor específico por ID"""
        for vendedor in self.vendedores:
            if vendedor['id'] == vendedor_id:
                return vendedor
        return None
    
    def obtener_productos_relacionados(self, producto_id, limite=3):
        """Obtiene productos relacionados (misma categoría/subcategoría, diferentes vendedores)"""
        producto_actual = self.obtener_producto_por_id(producto_id)
        if not producto_actual:
            return []
        
        productos_relacionados = []
        for producto in self.productos:
            # Mismo categoría y subcategoría, pero diferente producto
            if (producto['id'] != producto_id and 
                producto['categoria'] == producto_actual['categoria'] and
                producto['subcategoria'] == producto_actual['subcategoria']):
                productos_relacionados.append(producto)
        
        # Limitar y ordenar por popularidad (más vendidos primero)
        productos_relacionados.sort(key=lambda x: x['vendidos'], reverse=True)
        return productos_relacionados[:limite]
    
    def obtener_productos_vendedor(self, vendedor_id, producto_actual_id, limite=3):
        """Obtiene otros productos del mismo vendedor"""
        productos_vendedor = []
        for producto in self.productos:
            # Mismo vendedor, pero diferente producto
            if (producto['vendedor_id'] == vendedor_id and 
                producto['id'] != producto_actual_id):
                productos_vendedor.append(producto)
        
        # Limitar y ordenar por precio
        productos_vendedor.sort(key=lambda x: x['precio_actual'], reverse=True)
        return productos_vendedor[:limite]

# Inicializar la API
api = ProductAPI()

@app.route('/')
def home():
    """Endpoint de prueba"""
    return jsonify({
        "message": "API de Productos - MercadoLibre Clone",
        "productos_disponibles": len(api.productos),
        "vendedores_disponibles": len(api.vendedores),
        "endpoints": {
            "producto": "/api/producto/<id>",
            "productos": "/api/productos",
            "vendedor": "/api/vendedor/<id>",
            "buscar": "/api/buscar?q=<término>"
        }
    })

@app.route('/api/producto/<int:producto_id>')
def obtener_producto_completo(producto_id):
    """
    Endpoint principal: obtiene producto + vendedor + relacionados + productos del vendedor
    Ejemplo: /api/producto/1
    """
    producto = api.obtener_producto_por_id(producto_id)
    
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    
    # Obtener vendedor
    vendedor = api.obtener_vendedor_por_id(producto['vendedor_id'])
    
    # Obtener productos relacionados (misma categoría, diferentes vendedores)
    productos_relacionados = api.obtener_productos_relacionados(producto_id)
    
    # Obtener otros productos del mismo vendedor
    productos_vendedor = api.obtener_productos_vendedor(producto['vendedor_id'], producto_id)
    
    # Formatear datos para el frontend
    respuesta = {
        "producto": producto,
        "vendedor": vendedor,
        "productos_relacionados": productos_relacionados,
        "productos_vendedor": productos_vendedor,
        "metadata": {
            "total_productos_categoria": len([p for p in api.productos 
                                            if p['categoria'] == producto['categoria']]),
            "total_productos_vendedor": len([p for p in api.productos 
                                           if p['vendedor_id'] == producto['vendedor_id']]),
            "timestamp": "2025-01-01T00:00:00Z"
        }
    }
    
    return jsonify(respuesta)

@app.route('/api/productos')
def listar_productos():
    """
    Lista todos los productos con filtros opcionales
    Parámetros: categoria, subcategoria, vendedor_id, limite
    """
    categoria = request.args.get('categoria')
    subcategoria = request.args.get('subcategoria')
    vendedor_id = request.args.get('vendedor_id', type=int)
    limite = request.args.get('limite', default=50, type=int)
    
    productos_filtrados = api.productos.copy()
    
    # Aplicar filtros
    if categoria:
        productos_filtrados = [p for p in productos_filtrados if p['categoria'] == categoria]
    
    if subcategoria:
        productos_filtrados = [p for p in productos_filtrados if p['subcategoria'] == subcategoria]
    
    if vendedor_id:
        productos_filtrados = [p for p in productos_filtrados if p['vendedor_id'] == vendedor_id]
    
    # Limitar resultados
    productos_filtrados = productos_filtrados[:limite]
    
    return jsonify({
        "productos": productos_filtrados,
        "total": len(productos_filtrados),
        "filtros_aplicados": {
            "categoria": categoria,
            "subcategoria": subcategoria,
            "vendedor_id": vendedor_id,
            "limite": limite
        }
    })

@app.route('/api/vendedor/<int:vendedor_id>')
def obtener_vendedor(vendedor_id):
    """
    Obtiene información completa del vendedor
    """
    vendedor = api.obtener_vendedor_por_id(vendedor_id)
    
    if not vendedor:
        return jsonify({"error": "Vendedor no encontrado"}), 404
    
    # Obtener productos del vendedor
    productos_vendedor = [p for p in api.productos if p['vendedor_id'] == vendedor_id]
    
    return jsonify({
        "vendedor": vendedor,
        "productos": productos_vendedor,
        "total_productos": len(productos_vendedor)
    })

@app.route('/api/buscar')
def buscar_productos():
    """
    Busca productos por término
    Parámetro: q (término de búsqueda)
    """
    termino = request.args.get('q', '').lower()
    limite = request.args.get('limite', default=20, type=int)
    
    if not termino:
        return jsonify({"error": "Término de búsqueda requerido"}), 400
    
    productos_encontrados = []
    
    for producto in api.productos:
        # Buscar en título, marca, modelo, categoría
        campos_busqueda = [
            producto['titulo'].lower(),
            producto['marca'].lower(),
            producto['modelo'].lower(),
            producto['categoria'].lower(),
            producto['subcategoria'].lower()
        ]
        
        # Buscar en descripción
        for desc in producto['descripcion']:
            campos_busqueda.append(desc.lower())
        
        # Si el término está en algún campo, incluir producto
        if any(termino in campo for campo in campos_busqueda):
            productos_encontrados.append(producto)
    
    # Limitar resultados
    productos_encontrados = productos_encontrados[:limite]
    
    return jsonify({
        "productos": productos_encontrados,
        "total": len(productos_encontrados),
        "termino_busqueda": termino
    })

@app.route('/api/categorias')
def obtener_categorias():
    """Obtiene todas las categorías disponibles"""
    return jsonify(api.categorias)

@app.route('/api/estadisticas')
def obtener_estadisticas():
    """Obtiene estadísticas generales"""
    stats = {
        "total_productos": len(api.productos),
        "total_vendedores": len(api.vendedores),
        "productos_por_categoria": {},
        "productos_por_vendedor": {},
        "rango_precios": {
            "minimo": min([p['precio_actual'] for p in api.productos]) if api.productos else 0,
            "maximo": max([p['precio_actual'] for p in api.productos]) if api.productos else 0
        }
    }
    
    # Contar productos por categoría
    for producto in api.productos:
        categoria = producto['categoria']
        if categoria not in stats['productos_por_categoria']:
            stats['productos_por_categoria'][categoria] = 0
        stats['productos_por_categoria'][categoria] += 1
    
    # Contar productos por vendedor
    for producto in api.productos:
        vendedor_id = producto['vendedor_id']
        if vendedor_id not in stats['productos_por_vendedor']:
            stats['productos_por_vendedor'][vendedor_id] = 0
        stats['productos_por_vendedor'][vendedor_id] += 1
    
    return jsonify(stats)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint no encontrado"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == '__main__':
    # Verificar si existen los archivos JSON
    if not os.path.exists('productos.json'):
        print(" No se encuentra productos.json")
        print(" Ejecuta primero el generador de datos:")
        print("   python generar_datos.py")
        exit(1)
    
    print("========== Iniciando API de Productos... ==========")
    print("========== Endpoints disponibles: ==========")
    print("   GET  /                           - Información de la API")
    print("   GET  /api/producto/<id>          - Producto completo con relacionados")
    print("   GET  /api/productos              - Lista de productos (con filtros)")
    print("   GET  /api/vendedor/<id>          - Información del vendedor")
    print("   GET  /api/buscar?q=<término>     - Buscar productos")
    print("   GET  /api/categorias             - Todas las categorías")
    print("   GET  /api/estadisticas           - Estadísticas generales")
    print("\n Servidor ejecutándose en: http://localhost:5000")
    print("🔧 Modo debug activado para desarrollo")
    
    app.run(debug=True, host='0.0.0.0', port=5000)