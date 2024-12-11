all:
	@echo "#### functions implemented"
	@echo "make build-img-local ............... build image"


build-img-local:
	@echo "Building local image docker..."
	@docker build -t etl_mobilidade:1.0 -f "./Dockerfile" "."

up:
	@echo "[UP]"
	@echo "docker compose up -d"
	@docker compose up -d
	@echo "wait 10 seconds and go -> http://localhost:9000/ for minio"

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
