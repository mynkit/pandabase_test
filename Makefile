run:
	docker-compose build --no-cache
	docker-compose up -d

stop:
	docker-compose down

init:
	docker-compose down
	docker-compose build --no-cache
	docker-compose up -d
