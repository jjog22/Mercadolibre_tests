# Modelo de ML supervisado de clasificación
### El modelo es de ML para buscar predecir la condicion de productos "new" o "used"
### Se creó un notebook para hacer todas las etapas de modelamiento como mejores practicas para el tipo de datos y cantidad de columnas/registros
	
##	Definición del problema / necesidad
1.	Entender el objetivo de negocio o científico.
2.	Traducirlo a un problema de predicción/clasificación/regresión, etc.
	
##	Recolección y comprensión de datos
1.	Obtener datos relevantes.
2. 	Analizar calidad, estructura y representatividad.
	
##	Preprocesamiento de datos
1.	Limpieza (valores nulos, duplicados, outliers).
2.	Transformación (normalización, codificación de variables categóricas).
3.	División en entrenamiento, validación y prueba.
	
##	Selección de características (Feature Engineering)
1. 	Analisis de variables, importancia y selección por relevancia estadística según el contenido (numérico, categórico)	
2.	Creación, transformación y selección de variables relevantes.
	
##	Selección del modelo
*	Elegir algoritmos candidatos (árboles, regresión, redes neuronales, etc.) en función del problema y los datos.
	
## 	Entrenamiento
*	Ajustar parámetros del modelo usando los datos de entrenamiento.
	
##	Validación y optimización
1.	Ajustar hiperparámetros (ej. grid search, random search, Bayesian optimization).
2.	Validar con datos separados (validación cruzada).
	
##	Evaluación
*	Medir desempeño en el conjunto de prueba con métricas apropiadas (ej. accuracy, precision, recall, RMSE, AUC, etc.).
	
##	Implementación / Predicción
1.	Desplegar el modelo entrenado y optimizado para que realice predicciones en datos nuevos.
2.	Monitorear desempeño en producción (drift de datos, degradación del modelo).
	
