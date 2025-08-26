# Modelo de ML supervisado de clasificación
### El modelo es de ML para buscar predecir la condicion de productos "new" o "used"
### Se creó un notebook para hacer todas las etapas de modelamiento como mejores practicas para el tipo de datos y cantidad de columnas/registros

  -	Definición del problema / necesidad
	•	Entender el objetivo de negocio o científico.
	•	Traducirlo a un problema de predicción/clasificación/regresión, etc.
	-	Recolección y comprensión de datos
	•	Obtener datos relevantes.
	•	Analizar calidad, estructura y representatividad.
  -	Preprocesamiento de datos
	•	Limpieza (valores nulos, duplicados, outliers).
	•	Transformación (normalización, codificación de variables categóricas).
	•	División en entrenamiento, validación y prueba.
	-	Selección de características (Feature Engineering)
	•	Creación, transformación y selección de variables relevantes.
  -	Selección del modelo
	•	Elegir algoritmos candidatos (árboles, regresión, redes neuronales, etc.) en función del problema y los datos.
	-	Entrenamiento
	•	Ajustar parámetros del modelo usando los datos de entrenamiento.
  -	Validación y optimización
	•	Ajustar hiperparámetros (ej. grid search, random search, Bayesian optimization).
	•	Validar con datos separados (validación cruzada).
	-	Evaluación
	•	Medir desempeño en el conjunto de prueba con métricas apropiadas (ej. accuracy, precision, recall, RMSE, AUC, etc.).
  -	Implementación / Predicción
	•	Desplegar el modelo entrenado y optimizado para que realice predicciones en datos nuevos.
	•	Monitorear desempeño en producción (drift de datos, degradación del modelo).
