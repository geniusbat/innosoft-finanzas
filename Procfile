% prepara el repositorio para su despliegue. 
release: sh -c 'cd innosoftFinanzas && python manage.py migrate --noinput'
% especifica el comando para lanzar Innosoft
web: sh -c 'cd innosoftFinanzas && gunicorn innosoftFinanzas.wsgi --log-file -'