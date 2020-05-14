build:
	docker build . -t dice-roller-gcc:latest

run:
	docker-compose run dice_roller

tests:
	docker-compose run tests

silent-commit:
	git add . && git commit -m "silent" && git push