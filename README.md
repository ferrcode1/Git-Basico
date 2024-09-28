# ![Git Icon](https://img.shields.io/badge/-Git-F05032?logo=git&logoColor=white) Comandos Básicos de Git

Este archivo contiene una lista de comandos útiles para trabajar con Git, organizados por categorías.

## Configuración Inicial

Estos comandos configuran tu entorno de trabajo con Git, como el nombre de usuario y el correo electrónico.

```bash
# Configurar el nombre de usuario
git config --global user.name "Your Name"

# Configurar el correo electrónico
git config --global user.email "Your Email"


# Crear un nuevo repositorio
git init

# Ver el estado actual del repositorio
git status


# Agregar todos los archivos al área de staging
git add .

# Crear un commit con un mensaje descriptivo
git commit -m "Commit message"

# Deshacer el último commit pero conservar los cambios en el área de staging
git reset --soft HEAD~1


# Ver los commits realizados
git log

# Ver los commits en formato gráfico
git log --graph

# Ver los commits en una sola línea
git log --pretty=oneline


# Remover un archivo del área de staging
git reset


# Crear una nueva rama
git branch "nombre-de-la-rama"

# Listar todas las ramas
git branch

# Moverse a otra rama
git switch "nombre-de-la-rama"

# Eliminar una rama
git branch -d "nombre-de-la-rama"

# Hacer merge de una rama en la actual
git merge "nombre-de-la-rama"


# Cambiar a un commit específico o rama
git checkout "hash-del-commit-o-nombre-de-la-rama"

# Resetear el historial a un commit anterior (cuidado, se pierden los cambios posteriores)
git reset --hard "hash-del-commit"


# Crear un tag con un mensaje
git tag -a "nombre-del-tag" -m "Tag message"


# Ver el historial de commits incluyendo reset y rebase
git reflog


# Guardar el estado del trabajo de manera temporal
git stash save "Mensaje descriptivo"

# Listar los stash guardados
git stash list

# Recuperar el stash más reciente
git stash pop


# Guardar el estado del trabajo de manera temporal
git stash save "Mensaje descriptivo"

# Listar los stash guardados
git stash list

# Recuperar el stash más reciente
git stash pop


# Subir los cambios al repositorio remoto y establecer upstream
git push -u origin main

# Subir cambios de forma normal
git push origin main


# Traer los últimos cambios del repositorio remoto
git pull origin main

# Traer cambios y hacer rebase para mantener un historial limpio
git pull --rebase origin main


<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comandos Básicos de Git</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f4f7fc;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #333;
        }

        .container {
            background-color: #fff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            padding: 20px;
            max-width: 600px;
            width: 100%;
        }

        h1 {
            display: flex;
            align-items: center;
            justify-content: center;
            color: #F05032;
            font-size: 24px;
        }

        h1 img {
            width: 40px;
            margin-right: 10px;
        }

        .command-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px 15px;
            margin-bottom: 10px;
            transition: background-color 0.3s;
        }

        .command-container:hover {
            background-color: #eef4ff;
        }

        .command {
            font-family: 'Courier New', Courier, monospace;
            color: #333;
            font-size: 14px;
        }

        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 8px 12px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
            transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #45a049;
        }

        footer {
            margin-top: 20px;
            text-align: center;
            font-size: 12px;
            color: #666;
        }

    </style>
</head>
<body>

    <div class="container">
        <h1>
            <img src="https://img.shields.io/badge/-Git-F05032?logo=git&logoColor=white" alt="Git Icon">
            Comandos Básicos de Git
        </h1>

        <div class="command-container">
            <div class="command">git init</div>
            <button onclick="copyToClipboard('git init')">Copiar</button>
        </div>

        <div class="command-container">
            <div class="command">git status</div>
            <button onclick="copyToClipboard('git status')">Copiar</button>
        </div>

        <div class="command-container">
            <div class="command">git add .</div>
            <button onclick="copyToClipboard('git add .')">Copiar</button>
        </div>

        <div class="command-container">
            <div class="command">git commit -m "mensaje"</div>
            <button onclick="copyToClipboard('git commit -m \"mensaje\"')">Copiar</button>
        </div>

        <footer>
            Desarrollado con <span style="color: #e25555;">♥</span> por [Tu Nombre]
        </footer>
    </div>

    <script>
        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(() => {
                alert('Comando copiado: ' + text);
            });
        }
    </script>

</body>
</html>
