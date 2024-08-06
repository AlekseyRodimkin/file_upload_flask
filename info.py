# https://docs-python.ru/packages/veb-frejmvork-flask-python/zagruzka-fajlov-server-flask/

# import os
# from flask import Flask, flash, request, redirect, url_for
# # объясняется ниже
# from werkzeug.utils import secure_filename
# from flask import send_from_directory
#
# basedir = os.path.abspath(os.path.dirname(__file__))
#
# # папка для сохранения загруженных файлов
# UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
# # расширения файлов, которые разрешено загружать
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
#
# # создаем экземпляр приложения
# app = Flask(__name__)
# # конфигурируем
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# """
# Максимальный размер файла
# Превышение = RequestEntityTooLarge
# """
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000  # 16mb
#
#
# def allowed_file(filename):
#     """ Функция проверки расширения файла """
#     return '.' in filename and \
#         filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#
#
# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # проверим, передается ли в запросе файл
#         if 'file' not in request.files:
#             # После перенаправления на страницу загрузки
#             # покажем сообщение пользователю
#             flash('Не могу прочитать файл')
#             return redirect(request.url)
#         file = request.files['file']
#         # Если файл не выбран, то браузер может
#         # отправить пустой файл без имени.
#         if file.filename == '':
#             flash('Нет выбранного файла')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             # безопасное извлечение оригинального имени файла
#             filename = secure_filename(file.filename)
#             # сохраняем файл
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             # если все прошло успешно, то перенаправляем
#             # на функцию-представление `download_file`
#             # для скачивания файла
#             return redirect(url_for('download_file', name=filename))
#     return '''
#     <!doctype html>
#     <title>Загрузить новый файл</title>
#     <h1>Загрузить новый файл</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     </html>
#     '''
#
#
# @app.route('/uploads/<name>')
# def download_file(name):
#     return send_from_directory(app.config["UPLOAD_FOLDER"], name)
#
#
# # ----------------------------------------------------------------
#
#
# from flask_uploads import UploadSet, configure_uploads, IMAGES
# from flask import render_template, flash, redirect, url_for, request
#
# # ##################Расширение для загрузки файлов Flask-Uploads.###########################
# # Приведенные ниже настройки применяются для одного набора загрузок,
# # замените FILES на имя набора (например, UPLOADED_PHOTOS_DEST):
#
# # UPLOADED_FILES_DEST: параметр указывает на каталог, в котором будут сохранены загруженные файлы.
# # UPLOADED_FILES_URL: если есть сервер, настроенный для обслуживания файлов в этом наборе, то это URL-адрес, с которого загруженные файла набора будут общедоступны. В конце добавьте косую черту /.
# # UPLOADED_FILES_ALLOW: параметр, разрешающий указанные расширения файлов.
# # UPLOADED_FILES_DENY: параметр, запрещающий расширения файлов.
#
#
# # Чтобы сэкономить время на настройку, можно указать две настройки,
# # которые будут применяться как настройки по умолчанию.
#
# # UPLOADS_DEFAULT_DEST: параметр указывает место назначения набора загрузки,
# # если оно не объявлено иным образом.
# # Например, если установить значение /var/uploads,
# # то набор с именем photos будет хранить свои загрузки в /var/uploads/photos.
#
# # UPLOADS_DEFAULT_URL: это базовый URL-адрес настроенного сервера,
# # для обслуживания файлов из UPLOADS_DEFAULT_DEST.
# # Продолжая приведенный выше пример,
# # если директория /var/uploads доступна по адресу http://example.ru/uploads,
# # то URL-адреса для набор с именем photos будут начинаться с
# # http://example.ru/uploads/photos. Включите завершающую косую черту.
#
# # Так же можно установить MAX_CONTENT_LENGTH, чтобы ограничить размер загружаемых файлов.
#
# # Если нет настроенного сервера для обслуживания файлов,
# # то и не нужно устанавливать какие-либо параметры *_URL.
# # В этом случае, загруженные файлы будут обслуживаться фреймворком Flask.
# # НО если у вас большой трафик загрузки,
# # то для обслуживания файлов лучше использовать более быстрый и производительный сервер,
# # такой как Nginx или Lighttpd.
#
# UPLOADED_PHOTOS_DEST: os.path.join(basedir, 'uploads')
#
# # Наборы загрузок UploadSet.
# # "Набор загрузок" - это единый набор файлов какой-категории. Его необходимо объявить в коде:
#
# photos = UploadSet('photos', IMAGES)
#
#
# # После этого можно использовать метод .store(), для сохранения загруженного файла в
# # определенную директорию, после чего извлечь путь до файла и URL-адрес для доступа к нему.
# # Например:
#
#
# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST' and 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         rec = Photo(filename=filename, user=g.user.id)
#         rec.store()
#         flash("Фотография сохранена.")
#         return redirect(url_for('show', id=rec.id))
#     return render_template('upload.html')
#
#
# @app.route('/photo/<id>')
# def show(id):
#     photo = Photo.load(id)
#     if photo is None:
#         abort(404)
#     url = photos.url(photo.filename)
#     return render_template('show.html', url=url, photo=photo)
#
#
# # Если в конфигурации указано "расположение загрузок по умолчанию" UPLOADS_DEFAULT_DEST и например,
# # ваше приложение имеет каталог экземпляра приложения,
# # при этом загрузки должны сохраняться в папке upload каталога экземпляра приложения,
# # то можно быстро перенастроить папку для загрузки,
# # передав аргумент default_dest конструктору UploadSet. Например:
#
# # media = UploadSet('media', default_dest=lambda app: app.instance_path)
#
#
# # Конфигурация расширения Flask-Uploads.
# # Конфигурация набора загрузки хранится в приложении.
# # Таким образом, можно использовать наборы загрузки сразу в нескольких приложениях.
# # Используйте функцию configure_uploads(), чтобы загрузить конфигурацию для разных наборов загрузок.
# # Функция configure_uploads() передает приложению и все наборы загрузок.
# # Вызов configure_uploads более одного раза безопасен.
#
# from flask_uploads import UploadSet, configure_uploads, IMAGES
#
# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)
# # Если приложение имеет фабрику приложений, то это,
# # именно то место где нужно настраивать расширение Flask-Uploads.
#
# # По умолчанию Flask не накладывает никаких ограничений на размер загружаемых данных.
# # Чтобы защитить приложение, можно использовать patch_request_class().
# # Если вызывать patch_request_class() со вторым параметром None,
# # то для ограничения максимального размера загружаемого файла будет
# # использоваться параметр конфигурации MAX_CONTENT_LENGTH.
#
# from flask_uploads import patch_request_class
#
# patch_request_class(app, None)
# # Класс patch_request_class() также второй параметр может быть числом,
# # которое установить абсолютный предел,
# # но он существует только по причинам обратной совместимости и
# # не рекомендуется для использования. Кроме того, это не обязательно для Flask 0.6 или выше.
#
# # Форма загрузки файлов.
# # Чтобы действительно загрузить файлы, необходимо правильно настроить форму.
# # Форма, которая загружает файлы, должна иметь свой метод, установленный в POST,
# # и свой тип enctype, установленный в multipart/form-data.
# # Если метод формы настроен на GET, то загрузка вообще не будет работать,
# # а если не установить enctype, то будет передано только имя файла.
# #
# # Само поле должно быть <input type=file>.
# #
# # <form method=POST enctype=multipart/form-data action="{{ url_for('upload') }}">
# #     ...
# #     <input type=file name=photo>
# #     ...
# # </form>
