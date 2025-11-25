import argparse

# %% [markdown]
# # Análisis de Logs en JSON  
# ### Uso de listas, diccionarios y sets en Python
# En este ejercicio trabajaremos con un archivo JSON que contiene registros (logs) reales de un sistema web.  
# El objetivo es practicar estructuras de datos en Python usando **listas**, **diccionarios**, **sets**, **comprehensions**, etc.
# 

# %% [markdown]
# ## Dataset: logs.json
# 
# El archivo contiene una lista de registros con información sobre usuarios, acciones, IPs y estados de respuesta.
# 
# Cada registro es un diccionario:
# 
# ```json
# {
#     "user": "ana",
#     "action": "login",
#     "ip": "192.168.1.10",
#     "status": 200,
#     "timestamp": "2025-01-14T10:23:11"
# }
# 

# %%
import json

with open('logs.json', 'r') as file:
    logs = json.load(file)

for key, value in logs[0].items():
    print(f"{key} key type: {type(key)} - value: {value} value type: {type(value)}")

# %% [markdown]
# # Ejercicios
# 
# Debes resolver los siguientes ejercicios.  
# Puedes usar **listas**, **sets** o **diccionarios**

# %% [markdown]
# ### **Ejercicio 1 — Contar acciones realizadas en los logs**
# Crea una función que cuente cuántas veces aparece cada acción dentro de la lista de logs.
# 
# - **Function name:** `count_actions`
# - **Entrada:** lista de diccionarios (`list[dict]`)
# - **Salida:** diccionario con acción → número de ocurrencias (`dict[str, int]`)

# %%
def count_actions(logs: list[dict]) -> dict[str, int]:
    """
    Cuenta cuántas veces aparece cada valor único de la clave 'action' 
    dentro de la lista de logs.

    Args:
        logs: Lista de diccionarios.

    Returns:
        Un diccionario donde la clave es la acción (str) y el valor es la 
        cantidad de veces que ocurrió (int).

    """

    action_counts = {}

    for log in logs:
        action = log['action']

        if action in action_counts:
            action_counts[action] += 1
        else:
            action_counts[action] = 1

    return action_counts

# %% [markdown]
# ### **Ejercicio 2 — Obtener lista de usuarios únicos**
# Crea una función que devuelva un conjunto con todos los usuarios distintos presentes en los logs.
# 
# - **Function name:** `get_unique_users`
# - **Entrada:** lista de diccionarios (`list[dict]`)
# - **Salida:** conjunto de strings (`set[str]`)

# %%
def get_unique_users(logs: list[dict]) -> set[str]:
    """
    Obtiene todos los valores de la clave 'user' y los almacena en un conjunto 
    para devolver solo los usuarios distintos.

    Args:
        logs: Lista de diccionarios.

    Returns:
        Un conjunto (set) de strings con todos los nombres de usuario únicos.
    """

    unique_users = set()

    for log in logs:
        user = log['user']

        unique_users.add(user)

    return unique_users

# %% [markdown]
# ### **Ejercicio 3 — Detectar qué usuarios han tenido errores (`status == 4XX`).**
# Crea una función que devuelva 
# 
# - **Function name:** `filter_by_status`
# - **Entrada:**  
#   - lista de diccionarios (`list[dict]`)  
# - **Salida:** conjunto de strings (`set[str]`)

# %%
def filter_by_status(logs: list[dict]) -> set[str]:
    """
    Devuelve un conjunto con los nombres de usuario que tienen 
    al menos un error 4XX.

    Args:
        logs: Lista de diccionarios.

    Returns:
        Un conjunto (set) de strings con los usuarios que tuvieron errores.
    """
    error_users = set()

    for log in logs:
        user = log['user']

        if 400 <= log['status'] <= 499:
            error_users.add(user)

    return error_users


# %% [markdown]
# ### **Ejercicio 4 — Obtener IPs únicas de los logs**
# Crea una función que extraiga todas las direcciones IP de los logs, sin repetir ninguna.
# 
# - **Function name:** `get_unique_ips`
# - **Entrada:** lista de diccionarios (`list[dict]`)
# - **Salida:** conjunto de strings (`set[str]`)

# %%
def get_unique_ips(logs: list[dict]) -> set[str]:
    """
    Obtiene todas las direcciones IP únicas de la lista de logs.

    Args:
        logs: Lista de diccionarios.

    Returns:
        Un conjunto (set) de strings con todas las direcciones IP únicas.
    """

    unique_ips = set()

    for log in logs:
        ip = log['ip']

        unique_ips.add(ip)

    return unique_ips

# %% [markdown]
# ### **Ejercicio 5 — Encontrar el usuario con más acciones registradas**
# Crea una función que determine qué usuario aparece más veces en los logs.
# 
# - **Function name:** `most_frequent_user`
# - **Entrada:** lista de diccionarios (`list[dict]`)
# - **Salida:** string con nombre del usuario (`str`)

# %%
def most_frequent_user(logs: list[dict]) -> str:
    """
    Determina qué usuario tiene el mayor número de logs en la lista.

    Args:
        logs: Lista de diccionarios.

    Returns:
        Un string con el nombre del usuario más frecuente.
    """

    user_counts = {}

    for log in logs:
        user = log['user']

        if user in user_counts:
            user_counts[user] += 1
        else:
            user_counts[user] = 1

    return max(user_counts, key=user_counts.get)



# %% [markdown]
# ### Ejercicio Final — `run_selected_exercise`
# 
# **Descripción:**  
# Crea una función llamada **`run_selected_exercise`** que reciba dos entradas:
# 
# 1. **`json_path`** (str):  
#    Un *path absoluto* hacia un archivo JSON local.  
#    Este JSON contiene una **lista de diccionarios** que simulan logs del sistema.
# 
# 2. **`exercise_number`** (int):  
#    Puede ser **1, 2, 3, 4 o 5**.  
#    Este número indica qué ejercicio anterior debe ejecutarse.
# 
# La función debe:
# 
# - Leer el archivo JSON desde `json_path`.
# - Cargar la lista de diccionarios de logs.
# - En función del número recibido:
#   - Llamar internamente a la función correspondiente al ejercicio **1**, **2**, **3**, **4** o **5**.
# - Recibir el resultado del ejercicio elegido.
# - **Imprimir** ese resultado por pantalla usando `print`.
# 
# **Entradas:**
# - `json_path` (str) — ruta absoluta a un archivo JSON.
# - `exercise_number` (int) — número de ejercicio a ejecutar (1, 2, 3, 4 o 5).
# 
# **Salida:**
# - Ninguna salida de retorno.  
# - La función **imprime** por pantalla el resultado del ejercicio seleccionado.
# 
# **Nombre de la función:**  
# `run_selected_exercise`
# 

# %%
def run_selected_exercise(json_path: str, exercise_number: int):
    """
     Función que dirige la ejecución de los ejercicios de logs.
    
    1. Lee el archivo JSON de logs desde la ruta proporcionada (json_path).
    2. Carga el contenido como una lista de diccionarios.
    3. En función del exercise_number (1-5), llama a la función de lógica correspondiente.
    4. Imprime el resultado de la función seleccionada por pantalla.

    Args:
        json_path (str): Ruta al archivo JSON que contiene los logs.
        exercise_number (int): El número del ejercicio a ejecutar (1: Acciones, 2: Usuarios Únicos, 3: Usuarios con Error, 4: IPs Únicas, 5: Usuario Más Frecuente).
        
    Returns:
        Ninguno. La función imprime el resultado directamente.
    """

    with open(json_path, 'r', encoding='utf-8') as file:
        logs = json.load(file)
        
    result = None
    
    if exercise_number == 1:
        print("\n Ejecutando Ejercicio 1: Conteo de Acciones")
        result = count_actions(logs)
    
    elif exercise_number == 2:
        print("\n Ejecutando Ejercicio 2: Usuarios Únicos")
        result = get_unique_users(logs)
    
    elif exercise_number == 3:
        print("\n Ejecutando Ejercicio 3: Usuarios con Error 4XX")
        result = filter_by_status(logs)
    
    elif exercise_number == 4:
        print("\n Ejecutando Ejercicio 4: IPs Únicas")
        result = get_unique_ips(logs)
        
    elif exercise_number == 5:
        print("\n Ejecutando Ejercicio 5: Usuario Más Frecuente")
        result = most_frequent_user(logs)
    
    else:
        print(f"\nERROR: Número de ejercicio no válido: {exercise_number}. Debe ser 1, 2, 3, 4 o 5.")
        return

    print("\n[RESULTADO DEL EJERCICIO]")
    print(result)

def main():

    parser = argparse.ArgumentParser(description="Dirige la ejecución de los ejercicios de logs.")
    parser.add_argument("--jsonpath", type=str, help="Ruta al archivo JSON de logs.")
    parser.add_argument( "--exercisenumber",
        type=int,
        choices=[1,2,3,4,5],
        help="Número del ejercicio a ejecutar (1, 2, 3, 4 o 5)"
    )

    args = parser.parse_args()




    run_selected_exercise(args.jsonpath, args.exercisenumber)


if __name__ == "__main__":
    main()
