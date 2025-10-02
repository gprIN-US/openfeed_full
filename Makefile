up:
	docker compose up -d

down:
	docker compose down

topics:
	bash scripts/create_topics.sh

gen:
	python data_gen/generator.py

consume:
	python tests/consumer_test.py

train:
	python training/train_baseline.py

serve-local:
	uvicorn serving.api.main:app --host 0.0.0.0 --port 8092

