1.crear Apps
python manage.py startapp modelo
python manage.py startapp transsaciones
python manage.py startapp login
python manage.py startapp gestion_clientes

2. Modificar el settings.py
agregar los apps en la seccion Install_app

3. migrar bd
python manage.py migrate

4. Migrar modelos para la bd
python manage.py makemigrations

5. Crear modelo en la app models

6. migrar modelos para la bd