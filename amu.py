import shutil
import sys
import os

#==========================================================================================#
# >>>>> ПРОВЕРКА ВЕРСИИ PYTHON <<<<< #
#==========================================================================================#

# Минимальная требуемая версия Python.
PythonMinimalVersion = (3, 9)
# Проверка соответствия.
if sys.version_info < PythonMinimalVersion:
	sys.exit("Python %s.%s or later is required.\n" % PythonMinimalVersion)

#==========================================================================================#
# >>>>> ОБРАБОТКА ФАЙЛОВ <<<<< #
#==========================================================================================#

# Если передан один аргумент.
if len(sys.argv) == 2:
	# Вывод в консоль: в процессе. 
	print("In progress...")
	# Обрабатываемая директория (с заменой слэшей для совместимости с Linux).
	AppLockFolder = sys.argv[1].replace('\\', '/')
	# Получение списка папок.
	DirectoryContent = os.listdir(sys.argv[1] + "/dont_remove")
	# Список папок.
	FoldersList = list()
	# Список изображений.
	ImagesList = list()
	# Список видео.
	VideosList = list()

	# Сохранить названия папок.
	for Something in DirectoryContent:
		if os.path.isdir(AppLockFolder + "/dont_remove/" + Something):
			FoldersList.append(Something)

	# Для каждой папки.
	for Folder in FoldersList:
		# Получить список локальных изображений.
		LocalImagesList = os.listdir(AppLockFolder + "/dont_remove/" + Folder + "/.image")
		# Получить список локальных видео.
		LocalVideosList = os.listdir(AppLockFolder + "/dont_remove/" + Folder + "/.video")

		# Поместить все локальные изображения в глобальный список.
		for Image in LocalImagesList:
			ImagesList.append(AppLockFolder + "/dont_remove/" + Folder + "/.image/" + Image)

		# Поместить все локальные видео в глобальный список.
		for Video in LocalVideosList:
			VideosList.append(AppLockFolder + "/dont_remove/" + Folder + "/.video/" + Image)

	# Если найдены изображения.
	if len(ImagesList) > 0:

		# Если не существует папки для изображений, то создать её.
		if os.path.exists("Images") == False:
			os.makedirs("Images")

		# Переместить каждый файл с переименованием.
		for Image in ImagesList:
			shutil.copy(Image, "Images/" + Image.split('/')[-1] + ".jpg")

	# Если найдены видео.
	if len(VideosList) > 0:

		# Если не существует папки для изображений, то создать её.
		if os.path.exists("Videos") == False:
			os.makedirs("Videos")

		# Скопировать каждый файл с переименованием.
		for Video in VideosList:
			shutil.copy(Image, "Videos/" + Image.split('/')[-1] + ".mp4")

else:
	raise Exception("Invalid arguments count.")

# Завершение работы скрипта.
sys.exit(0)
