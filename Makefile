build:
	docker build . -t dice-roller-gcc:latest

run:
	docker-compose run dice_roller

test:
	docker-compose run tests

create-virtual-env:
	python3 -m venv bot_disc_venv

activate-virtual-env:
	source bot_disc_venv/bin/activate
