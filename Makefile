build:
	docker build -t fastapi-app .

run:
	docker run -d -p 8000:8000 --name fastapi-app fastapi-app

stop:
	docker stop fastapi-app || true
	docker rm fastapi-app || true

restart: stop build run

clean:
	docker rmi fastapi-app || true
