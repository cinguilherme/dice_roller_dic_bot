build:
	docker build . -t dice-roller-gcc:latest

run:
	docker-compose run dice_roller

test:
	docker-compose run tests