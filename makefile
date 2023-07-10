.PHONY: all

MIGRATION_PATH=./data/migrations
MIGRATION_CONF_PATH=./data/migrations/config.json
DB=postgres://localhost:5432/sb9000?sslmode=require

env:
	cp ./.env.sample .env

setup_server:
	cd server && pip install -r requirements.txt

venv:
	source server/venv/bin/activate

setup_bucket:
	aws --endpoint-url=http://localhost:4566 s3api create-bucket --region=us-east-1 --bucket sb9000

dev_certs:
	mkdir certs && openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 \
	-subj "/C=US/ST=State/L=City/O=Organization/CN=localhost" \
	-keyout certs/private.key -out certs/certificate.crt

up:
	docker-compose up -d

all: env setup_bucket setup_server venv dev_certs up

migration_new:
	migrate create -dir ./data/migrations -seq -ext sql $(ARG)
migration_up:
	migrate -path $(MIGRATION_PATH) -database "postgres://sb9_user:sb9_user@localhost:5432/sb9000?sslmode=disable" up
migration_down:
	migrate -path $(MIGRATION_PATH) -database "postgres://sb9_user:sb9_user@localhost:5432/sb9000?sslmode=disable" down


 