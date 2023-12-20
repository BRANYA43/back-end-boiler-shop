MANAGER_PATH = "src/manage.py"

startapp:
	python $(MANAGER_PATH) startapp $(name)
	mv ./$(name) src/$(name)
	rm src/$(name)/tests.py
	mkdir src/$(name)/tests/
	touch src/$(name)/tests/__init__.py \
  		  src/$(name)/serializers.py \
  		  src/$(name)/urls.py

make_migrations:
	python $(MANAGER_PATH) makemigrations $(app)

migrate:
	python $(MANAGER_PATH) migrate $(app)

run_tests:
	python $(MANAGER_PATH) test $(app)
