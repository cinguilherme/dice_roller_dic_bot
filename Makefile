build:
	docker build . -t dice-roller-gcc:latest

run:
	docker-compose run dice_roller

test_local:
	docker-compose run tests