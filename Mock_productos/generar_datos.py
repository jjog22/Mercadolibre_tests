import json
import random
from datetime import datetime, timedelta

def generar_datos_completos():
    """Genera todos los datos necesarios para el sistema de productos"""
    
    # Datos base para generar contenido realista
    marcas_celulares = ["Samsung", "iPhone", "Xiaomi", "Motorola", "Huawei"]
    marcas_monitores = ["LG", "Samsung", "ASUS", "Dell", "HP"]
    
    # Generar vendedores
    vendedores = [
        {
            "id": 1,
            "nombre": "Samsung Colombia Oficial",
            "tipo": "Oficial",
            "calificacion": 4.9,
            "ventas_totales": 15420,
            "seguidores": 2850,
            "mercado_lider": True,
            "nivel_vendedor": "Platinum",
            "productos_ids": [1, 2, 3, 6, 11, 12],  # Productos que vende Samsung
            "medios_pago": {
                "tarjetas_credito": ["Visa", "Mastercard", "American Express", "Diners"],
                "tarjetas_debito": ["Visa Débito", "Mastercard Débito"],
                "efectivo": ["Efecty", "Baloto", "Paga Todo"],
                "otros": ["PSE", "Bancolombia", "Nequi"]
            },
            "tiempo_entrega_dias": "1-3",
            "envio_gratis": True
        },
        {
            "id": 2,
            "nombre": "TecnoPlaza Colombia",
            "tipo": "Tienda",
            "calificacion": 4.7,
            "ventas_totales": 8930,
            "seguidores": 1200,
            "mercado_lider": True,
            "nivel_vendedor": "Gold",
            "productos_ids": [4, 5, 7, 8, 9, 10, 13, 14, 15],
            "medios_pago": {
                "tarjetas_credito": ["Visa", "Mastercard"],
                "tarjetas_debito": ["Visa Débito", "Mastercard Débito"],
                "efectivo": ["Efecty"],
                "otros": ["PSE"]
            },
            "tiempo_entrega_dias": "2-5",
            "envio_gratis": True
        },
        {
            "id": 3,
            "nombre": "ElectroMax Store",
            "tipo": "Tienda",
            "calificacion": 4.5,
            "ventas_totales": 3420,
            "seguidores": 580,
            "mercado_lider": False,
            "nivel_vendedor": "Silver",
            "productos_ids": [5, 8, 10, 13, 15],
            "medios_pago": {
                "tarjetas_credito": ["Visa", "Mastercard"],
                "tarjetas_debito": ["Visa Débito"],
                "efectivo": ["Efecty"],
                "otros": ["PSE"]
            },
            "tiempo_entrega_dias": "3-7",
            "envio_gratis": False
        }
    ]
    
    # Generar celulares (10 productos)
    celulares = []
    celular_id = 1
    
    celulares_data = [
        {
            "marca": "Samsung", "modelo": "Galaxy S24 Ultra", "almacenamiento": "256GB", "ram": "12GB",
            "pantalla": "6.8", "camara": "200MP", "bateria": "5000mAh", "precio_base": 4500000, "vendedor_id": 1
        },
        {
            "marca": "Samsung", "modelo": "Galaxy A54", "almacenamiento": "128GB", "ram": "8GB",
            "pantalla": "6.4", "camara": "50MP", "bateria": "5000mAh", "precio_base": 1200000, "vendedor_id": 1
        },
        {
            "marca": "iPhone", "modelo": "15 Pro Max", "almacenamiento": "256GB", "ram": "8GB",
            "pantalla": "6.7", "camara": "48MP", "bateria": "4441mAh", "precio_base": 5800000, "vendedor_id": 2
        },
        {
            "marca": "Xiaomi", "modelo": "Redmi Note 13 Pro", "almacenamiento": "256GB", "ram": "8GB",
            "pantalla": "6.67", "camara": "200MP", "bateria": "5100mAh", "precio_base": 950000, "vendedor_id": 2
        },
        {
            "marca": "Motorola", "modelo": "Edge 40 Neo", "almacenamiento": "256GB", "ram": "12GB",
            "pantalla": "6.55", "camara": "50MP", "bateria": "5000mAh", "precio_base": 1400000, "vendedor_id": 2
        },
        {
            "marca": "Samsung", "modelo": "Galaxy Z Flip5", "almacenamiento": "512GB", "ram": "8GB",
            "pantalla": "6.7", "camara": "12MP", "bateria": "3700mAh", "precio_base": 3800000, "vendedor_id": 1
        },
        {
            "marca": "Xiaomi", "modelo": "POCO X5 Pro", "almacenamiento": "256GB", "ram": "8GB",
            "pantalla": "6.67", "camara": "108MP", "bateria": "5000mAh", "precio_base": 850000, "vendedor_id": 2
        },
        {
            "marca": "Huawei", "modelo": "P60 Pro", "almacenamiento": "256GB", "ram": "8GB",
            "pantalla": "6.67", "camara": "48MP", "bateria": "4815mAh", "precio_base": 2200000, "vendedor_id": 2
        },
        {
            "marca": "Motorola", "modelo": "G73 5G", "almacenamiento": "256GB", "ram": "8GB",
            "pantalla": "6.5", "camara": "50MP", "bateria": "5000mAh", "precio_base": 780000, "vendedor_id": 3
        },
        {
            "marca": "iPhone", "modelo": "14", "almacenamiento": "128GB", "ram": "6GB",
            "pantalla": "6.1", "camara": "48MP", "bateria": "3279mAh", "precio_base": 3200000, "vendedor_id": 2
        }
    ]
    
    for data in celulares_data:
        descuento = random.randint(0, 40)
        precio_actual = int(data["precio_base"] * (1 - descuento/100))
        vendidos = random.randint(50, 2000)
        disponibles = random.randint(5, 150)
        
        celular = {
            "id": celular_id,
            "titulo": f"{data['marca']} {data['modelo']} {data['almacenamiento']} {data['ram']} RAM",
            "categoria": "Celulares y Smartphones",
            "subcategoria": "Smartphones",
            "marca": data["marca"],
            "modelo": data["modelo"],
            "condicion": "Nuevo",
            "precio_original": data["precio_base"],
            "precio_actual": precio_actual,
            "descuento_porcentaje": descuento if descuento > 0 else None,
            "vendidos": vendidos,
            "unidades_disponibles": disponibles,
            "calificacion": round(random.uniform(4.2, 5.0), 1),
            "numero_resenas": random.randint(50, 800),
            "vendedor_id": data["vendedor_id"],
            "cuotas": {
                "cantidad": random.choice([3, 6, 12, 24]),
                "valor_cuota": precio_actual // random.choice([3, 6, 12, 24]),
                "interes": random.choice([0, 2.5, 5.0])
            },
            "caracteristicas": {
                "Pantalla": f"{data['pantalla']}\" pulgadas",
                "Almacenamiento": data["almacenamiento"],
                "Memoria RAM": data["ram"],
                "Cámara principal": data["camara"],
                "Batería": data["bateria"],
                "Sistema operativo": "Android 14" if data["marca"] != "iPhone" else "iOS 17",
                "Procesador": f"Snapdragon 8 Gen 2" if data["marca"] != "iPhone" else "A17 Pro",
                "Red móvil": "5G",
                "Resistencia al agua": "IP68",
                "Carga inalámbrica": "Sí" if precio_actual > 1000000 else "No"
            },
            "descripcion": [
                f"Experimenta la potencia del {data['marca']} {data['modelo']} con {data['ram']} de RAM",
                f"Pantalla de {data['pantalla']}\" para una experiencia visual inmersiva",
                f"Cámara de {data['camara']} para capturar momentos únicos con calidad profesional",
                f"Batería de {data['bateria']} para un día completo de uso intensivo",
                f"Almacenamiento de {data['almacenamiento']} para todas tus aplicaciones y archivos",
                "Conectividad 5G para velocidades de descarga ultrarrápidas",
                "Diseño elegante y resistente con certificación IP68",
                "Procesador de última generación para un rendimiento excepcional"
            ],
            "imagenes": [
                f"https://via.placeholder.com/400x300/FF6B6B/FFFFFF?text={data['marca']}+{data['modelo']}",
                f"https://via.placeholder.com/400x300/4ECDC4/FFFFFF?text=Vista+Trasera",
                f"https://via.placeholder.com/400x300/45B7D1/FFFFFF?text=Pantalla",
                f"https://via.placeholder.com/400x300/96CEB4/FFFFFF?text=Accesorios"
            ],
            "tiempo_entrega": random.choice(["1-2 días", "2-3 días", "3-5 días"]),
            "envio_gratis": random.choice([True, False]),
            "mas_vendido": vendidos > 500,
            "posicion_categoria": random.randint(1, 20) if vendidos > 300 else None
        }
        
        celulares.append(celular)
        celular_id += 1
    
    # Generar monitores (5 productos)
    monitores = []
    monitor_id = 11  # Continuar numeración después de celulares
    
    monitores_data = [
        {
            "marca": "LG", "modelo": "24MK430H-B", "tamano": "24", "resolucion": "Full HD",
            "frecuencia": "75Hz", "panel": "IPS", "precio_base": 450000, "vendedor_id": 1
        },
        {
            "marca": "Samsung", "modelo": "Odyssey G7", "tamano": "27", "resolucion": "QHD",
            "frecuencia": "240Hz", "panel": "VA", "precio_base": 1200000, "vendedor_id": 1
        },
        {
            "marca": "ASUS", "modelo": "VP249HE", "tamano": "24", "resolucion": "Full HD",
            "frecuencia": "75Hz", "panel": "IPS", "precio_base": 380000, "vendedor_id": 2
        },
        {
            "marca": "Dell", "modelo": "S2721DS", "tamano": "27", "resolucion": "QHD",
            "frecuencia": "75Hz", "panel": "IPS", "precio_base": 850000, "vendedor_id": 2
        },
        {
            "marca": "HP", "modelo": "24mh", "tamano": "24", "resolucion": "Full HD",
            "frecuencia": "75Hz", "panel": "IPS", "precio_base": 420000, "vendedor_id": 3
        }
    ]
    
    for data in monitores_data:
        descuento = random.randint(0, 35)
        precio_actual = int(data["precio_base"] * (1 - descuento/100))
        vendidos = random.randint(100, 1500)
        disponibles = random.randint(10, 80)
        
        monitor = {
            "id": monitor_id,
            "titulo": f"Monitor {data['marca']} {data['tamano']}\" {data['resolucion']} {data['frecuencia']} {data['panel']}",
            "categoria": "Computación",
            "subcategoria": "Monitores",
            "marca": data["marca"],
            "modelo": data["modelo"],
            "condicion": "Nuevo",
            "precio_original": data["precio_base"],
            "precio_actual": precio_actual,
            "descuento_porcentaje": descuento if descuento > 0 else None,
            "vendidos": vendidos,
            "unidades_disponibles": disponibles,
            "calificacion": round(random.uniform(4.0, 4.9), 1),
            "numero_resenas": random.randint(80, 600),
            "vendedor_id": data["vendedor_id"],
            "cuotas": {
                "cantidad": random.choice([3, 6, 12]),
                "valor_cuota": precio_actual // random.choice([3, 6, 12]),
                "interes": random.choice([0, 2.5])
            },
            "caracteristicas": {
                "Tamaño de pantalla": f"{data['tamano']} pulgadas",
                "Resolución": data["resolucion"] + " (1920x1080)" if data["resolucion"] == "Full HD" else "QHD (2560x1440)",
                "Frecuencia de actualización": data["frecuencia"],
                "Tipo de panel": data["panel"],
                "Conectividad": "HDMI, VGA, DisplayPort" if precio_actual > 600000 else "HDMI, VGA",
                "Montaje VESA": "100x100mm",
                "Ajuste de altura": "Sí" if precio_actual > 700000 else "No",
                "Ángulo de inclinación": "-5° a +20°",
                "Brillo": "250 cd/m²",
                "Contraste": "1000:1"
            },
            "descripcion": [
                f"Monitor {data['marca']} de {data['tamano']}\" con resolución {data['resolucion']} para una experiencia visual excepcional",
                f"Frecuencia de actualización de {data['frecuencia']} ideal para gaming y trabajo profesional",
                f"Panel {data['panel']} que garantiza colores precisos y ángulos de visión amplios",
                "Conectividad múltiple con puertos HDMI y VGA para máxima compatibilidad",
                "Montaje VESA compatible para instalación en pared o brazo articulado",
                "Diseño ergonómico con ajustes de inclinación para mayor comodidad",
                "Tecnología de reducción de parpadeo para sesiones largas sin fatiga visual",
                "Ideal para trabajo, gaming, entretenimiento y diseño gráfico"
            ],
            "imagenes": [
                f"https://via.placeholder.com/400x300/FF6B6B/FFFFFF?text=Monitor+{data['marca']}+{data['tamano']}",
                f"https://via.placeholder.com/400x300/4ECDC4/FFFFFF?text=Vista+Lateral",
                f"https://via.placeholder.com/400x300/45B7D1/FFFFFF?text=Conectores",
                f"https://via.placeholder.com/400x300/96CEB4/FFFFFF?text=Base"
            ],
            "tiempo_entrega": random.choice(["1-3 días", "2-4 días", "3-6 días"]),
            "envio_gratis": random.choice([True, False]),
            "mas_vendido": vendidos > 400,
            "posicion_categoria": random.randint(1, 15) if vendidos > 200 else None
        }
        
        monitores.append(monitor)
        monitor_id += 1
    
    # Combinar todos los productos
    productos = celulares + monitores
    
    # Crear estructura de datos final
    datos_completos = {
        "vendedores": vendedores,
        "productos": productos,
        "categorias": {
            "Celulares y Smartphones": {
                "subcategorias": ["Smartphones", "Accesorios para Celulares"]
            },
            "Computación": {
                "subcategorias": ["Monitores", "Accesorios para Computadoras"]
            }
        }
    }
    
    return datos_completos

def guardar_datos_json():
    """Genera y guarda los datos en archivos JSON separados"""
    
    datos = generar_datos_completos()
    
    # Guardar productos
    with open('productos.json', 'w', encoding='utf-8') as f:
        json.dump(datos['productos'], f, ensure_ascii=False, indent=2)
    
    # Guardar vendedores
    with open('vendedores.json', 'w', encoding='utf-8') as f:
        json.dump(datos['vendedores'], f, ensure_ascii=False, indent=2)
    
    # Guardar categorías
    with open('categorias.json', 'w', encoding='utf-8') as f:
        json.dump(datos['categorias'], f, ensure_ascii=False, indent=2)
    
    # Guardar todo junto
    with open('datos_completos.json', 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
    
    print("Archivos JSON generados exitosamente:")
    print("   - productos.json (15 productos)")
    print("   - vendedores.json (3 vendedores)")
    print("   - categorias.json")
    print("   - datos_completos.json (todo junto)")
    
    # Mostrar estadísticas
    print(f"\nEstadísticas:")
    print(f"   - Celulares: {len([p for p in datos['productos'] if p['categoria'] == 'Celulares y Smartphones'])}")
    print(f"   - Monitores: {len([p for p in datos['productos'] if p['categoria'] == 'Computación'])}")
    print(f"   - Vendedores: {len(datos['vendedores'])}")

if __name__ == "__main__":
    guardar_datos_json()