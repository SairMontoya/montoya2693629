diccionario={
    "rojo": "red",
    "azul": "blue",
    "morado": "purple",
    "blanco": "white",
    "verde": "green",
    "naranja": "orange",
    "amarillo": "yellow",
    "negro": "black",
    "rosado": "pink"
}


words = ['rojo','azul','morado','blanco','verde','naranja','amarillo','negro','rosado']

for word in words:
    if word in diccionario:
        print(word, "->", diccionario[word])
    else:
        print(word,"el color no esta")