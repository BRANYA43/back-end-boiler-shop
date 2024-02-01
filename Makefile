MANAGER_PATH = src/manage.py
APP_PATH = src/$(name)


startapp:
	python $(MANAGER_PATH) startapp $(name)
	mv ./$(name) $(APP_PATH)
	rm $(APP_PATH)/tests.py
	mkdir $(APP_PATH)/tests/
	touch $(APP_PATH)/tests/__init__.py \
  		  $(APP_PATH)/serializers.py \
  		  $(APP_PATH)/urls.py

make_migrations:
	python $(MANAGER_PATH) makemigrations $(if $(app),$(app),src)

migrate:
	python $(MANAGER_PATH) migrate $(if $(app),$(app),src)

run_tests:
	python $(MANAGER_PATH) test $(if $(app),$(app),src)
