#importar render para ver las views
from django.shortcuts import render 
#librerias a usar para la parte grafica de los datos
import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns
#librerias a usar para entrenamiento del dataset y calcular mejor los datos
from sklearn.model_selection import train_test_split #libreria para entrenamiento del dataset
from sklearn.linear_model import LogisticRegression #libreria para pruebas de regresion Linear
from sklearn.metrics import accuracy_score #libreria para tener datos lo mas certeros posibles

def home(request):#ruta de la vista home
    return render(request, 'home.html')

def prediccion(request):#ruta de la vista prediccion
    return render(request, 'predict.html')

def contacto(request):#ruta de la vista contacto
    return render(request, 'contact.html')

def resultado(request):#ruta de la vista donde se mostrara el resultado
    #cargar el dataset con pandas
    datos= pd.read_csv(r"C:\Users\carlos\diabetes.csv")
    x= datos.drop("Outcome",axis=1) #separar los datos de la columna outcome para el analisis
    y=datos["Outcome"] #encapsular los datos de outcome en un arreglo
    #variables para entrenamiento de datos las cuales se basaran las dos variables ya creadas
    #las 4 variables que crearas seran 2 para la parte de entrenamiento del modelo y dos para las pruebas
    x_train,x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)
    modelo = LogisticRegression() #entranamiento mediante regresion Logistica
    modelo.fit(x_train,y_train)#uso de las variables de entrenamiento

    #variables del formulario de predict.html
    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    #metodo para predecir mediante la informacion en cada campo
    pred = modelo.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])

    resultado1 =""
    if pred ==[1]:
        resultado1 = "Positivo"
    else:
        resultado1 = "Negativo"    

    return render(request, 'predict.html',{"resultado2":resultado1})
