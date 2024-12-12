all:
	@echo "#### functions implemented"
	@echo "make build-img-local ............... build image"
	@echo "make up ............................ docker compose up -d"
	@echo "make stop .......................... docker compose stop"
	@echo "make down .......................... docker compose down"
	@echo "make rm ............................ remove all exited containers and all dangling volumes"
	@echo "make du ............................ docker compose down && docker compose up -d"
	@echo "make de ............................ docker compose down && docker exec -it main_etl_mobilidade bash"
	@echo "make enter-local ................... docker exec -it main_etl_mobilidade bash"
	@echo "make bypass-enter-local ............ docker exec -it main_etl_mobilidade bash"
	@echo ""


build-img-local:
	@echo "Building local image docker..."
	@docker build -t etl_mobilidade:1.0 -f "./Dockerfile" "."

up:
	@echo "[UP]"
	@echo "docker compose up -d"
	@docker compose up -d
	@echo "wait 10 seconds and go -> http://localhost:9004/ for minio"

stop:
	@echo "[STOP]"
	@echo "docker compose stop"
	@docker compose stop

down:
	@echo "[DOWN]"
	@echo "docker compose down"
	@docker compose down  --remove-orphans

du: down up

de: down enter-local

rm: down
	@echo ""
	@echo ""
	@echo "remove all stopped containers"
	command docker ps -aqf status=exited | xargs -r docker rm
	@echo ""
	@echo ""
	@echo "remove all dangling volumes"
	@# The dangling filter matches on all volumes not referenced by any containers
	command docker volume ls -qf dangling=true | xargs -r docker volume rm
	@echo ""

enter-local: up
	@echo "Enter image local..."
	@docker exec -it main_etl_mobilidade bash

bypass-enter-local:
	@echo "Enter image local..."
	@docker exec -it main_etl_mobilidade bash

phoenix:
	@echo "[PHOENIX]"
	@echo ""
	@echo "docker compose down"
	@docker compose down --remove-orphans
	@echo "remove all stopped containers"
	command docker ps -aqf status=exited | xargs -r docker rm
	@echo ""
	@echo ""
	@echo "remove all dangling volumes"
	@# The dangling filter matches on all volumes not referenced by any containers
	command docker volume ls -qf dangling=true | xargs -r docker volume rm
	@echo ""
	@echo "Building local image docker..."
	@docker build -t etl_mobilidade:1.0 -f "./Dockerfile" "."
	@echo "docker compose up -d"
	@docker compose up -d

pc:
	@echo "pre-commit"
	@pre-commit run --all-files
