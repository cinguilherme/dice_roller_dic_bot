build:
	docker build . -t dice-roller-gcc:latest

run:
	docker-compose run dice_roller

test_local:
	docker-compose run tests

run_in_scale:
	docker-compose scale dice_roller=3