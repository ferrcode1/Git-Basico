# Comandos Básicos de Git

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
