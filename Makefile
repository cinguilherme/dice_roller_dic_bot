build:
	docker build . -t dice-roller-gcc:latest

run:
	docker run dice-roller:latest

run_local:
	python3 bot_example.py