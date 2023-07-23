# Проект novella-electric (Django) 💡

Этот проект представляет собой веб-приложение novella-electric, написанное на Django.

## Минимальный запуск приложения 🚀

Перед запуском приложения убедитесь, что у вас установлен Python и pip.

### Настройка окружения ⚙️

- Для запуска приложения, выполните следующие команды в терминале (команды предназначены для Linux-систем, узнайте способы создания виртуального окружения на вашей системе):

```bash
virtualenv venv
source venv/bin/activate
git clone git@github.com:star-small/waveUp.git
cd waveUp
pip install -r requirements.txt
```

Примечание: В этом проекте отсутствует файл settings.py. Вы можете скопировать пример файла settings_example.py и внести необходимые изменения для развертывания в вашей системе:

```bash
cp core/core/settings_example.py core/core/settings.py
rm core/core/settings_example.py
```

### Запуск 🚀
    
```bash
cd core/
python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb
python3 manage.py runserver
```

После выполнения команды выше, веб-приложение будет запущено на порту 8000 локального хоста. Просто перейдите по ссылке localhost:8000, чтобы увидеть приложение.

### Создание суперпользователя 👤

Вы можете создать суперпользователя с помощью следующей команды:

```bash
python3 manage.py createsuperuser
```

После создания суперпользователя, вы сможете администрировать базу данных, перейдя по адресу localhost:8000/admin.

### Загрузка CSV 📄

Чтобы загрузить товары из CSV файла, переместите ваш файл в директорию waveUp/core/files/ под именем file.csv.

После загрузки файла, вам может потребоваться загрузить фотографии. Для этого создайте папку:

```bash
# В папке waveUp/core, рядом с файлом manage.py
mkdir media/product_image/
# местоположение каталога может разниться в зависимости от настройки setting.py
```
Загрузите фотографии товаров в каталог media/product_image/, названия файлов в этой директории и в файле CSV должны быть одинаковы.

## Развёртывание

[Руководство по развёртыванию Django с использованием Postgres, Nginx и Gunicorn на Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04#step-10-configure-nginx-to-proxy-pass-to-gunicorn)
