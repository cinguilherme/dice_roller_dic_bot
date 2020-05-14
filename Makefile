build:
	docker build . -t dice-roller-gcc:latest

run:
	docker-compose run dice_roller

test:
	docker-compose run tests

create-virtual-env:
	python -m venv bot_disc_venv

activate-virtual-env:
	source bot_disc_venv/bin/activate

silent-commit:
	git add . && git commit -m "silent" && git push