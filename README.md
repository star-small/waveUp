# Сайт novella-electric, написанный на Django.

## Минимальный запуск приложения 

### Настройка окружения

- Представленные комманды только для линукс, узнайте методы для создания виртульного окружения и установки пакетов для собственной системы.

```bash
virtualenv venv
source venv/bin/activate
git clone git@github.com:star-small/waveUp.git
cd waveUp
pip install -r requirements.txt
```

### Примечание 
settings.py для этого проекта отсутсвует. Скопируйте пример settings_example.py и внесите в него изменения, необходимые для развертывания в вашей системе:

```bash
cp core/core/settings_example.py core/core/settings.py
rm core/core/settings_example.py
```

### Запуск
    
```bash
cd core/
python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb
python3 manage.py runserver
```

- Данная комманда запустит веб-приложение на 8000-м порту на локальном хосте. Просто перейдите по ссылке localhost:8000, чтобы увидеть приложение.

Создание суперпользователя:

```bash
python3 manage.py createsuperuser
```

- После создания суперпользователя, вы можете администрировать базу данных, перейдя по адресу localhost:8000/admin

### Загрузка CSV.

Чтобы загрузить товары из csv файла переместите ваш файл в директорию ```waveUp/core/files/``` под именем ``` file.csv ```.

- после загрузки файла, вам может потребоваться загрузить фотографии. Для этого создайте папку:

```bash
# В папке waveUp/core, рядом с файлом manage.py
mkdir media/product_image/
# местоположение каталога может разниться в зависимости от настройки setting.py
```
- Загрузите фотографии товаров в каталог ``` media/product_image/ ```, названия файлов в этой директории и в файле сsv должны быть одинаковы.

## Развёртывание

https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04#step-10-configure-nginx-to-proxy-pass-to-gunicorn
