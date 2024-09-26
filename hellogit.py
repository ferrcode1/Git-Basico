print("New Hello git!")  # New Hello git!")
# 01:27 Hello git!

""" 
    COMANDO PARA CONFIGURAR EL ENTORNO DE TRABAJO
    git config --global user.name "Your Name"
    git config --global user.email "Your Email"
    
"""

""" 
    COMANDO PARA CREAR UN REPOSITORIO
    git init
"""

""" 
    COMANDO PARA VER EL ESTADO DEL REPOSITORIO
    git status
"""

""" 
    COMANDO PARA AGREGAR UN ARCHIVO AL AREA DE STAGING
    git add .

"""

""" 
    COMANDO PARA CREAR UN COMMIT CON UN MENSAJE
    git commit -m "commit message"
"""

"""  
    COMANDO PARA DESHACER UN COMMIT Y CONSERVAR LOS CAMBIOS EN EL AREA DE STAGING
    git reset --soft HEAD~1
"""

""" 
    COMANDO PARA VER LOS COMMIT
    git log
"""

""" 
    COMANDO PARA VER LOS COMMIT FORMATEADOS
    git log --graph
    alias: git format
"""

""" 
    COMANDO PARA VER LOS COMMIT FORMATEADOS
    git log --pretty=oneline
"""

""" 
    COMANDO PARA REMOVER UN ARCHIVO DEL AREA DE STAGING
    git reset
"""

""" 
    COMANDO PARA REMOVERSE DE RAMA DE TRABAJO
    git checkout "hash del commit o rama al que queremos ir" 
"""

""" 
    COMANDO PARA ELIMINAR O DESHACER RAMAS DE TRABAJO
    git resest --hard "hash del commit o rama al que queremos ir (Se perdera todo el historial de commits realizado despues de este commit)"
    
    Para recuperar el historial de commits:
    git reset --hard "hash del commit o rama al que queremos ir"
"""

""" 
    COMANDO PARA LISTAR TODO EL HISTORIAL DE COMMITS
    git reflog
"""

"""
    COMANDO PARA CREAR TAGS
    git tag -a "tag name" -m "tag message"
"""

""" 
    COMANDO PARA CREAR UNA RAMA DE TRABAJO
    git branch "nombre de la rama"
"""

""" 
    COMANDO PARA VER LAS RAMAS DE TRABAJO
    git branch
"""

""" 
    COMANDO PARA MOVERSE DE RAMA DE TRABAJO
    git switch "nombre de la rama" 
"""

