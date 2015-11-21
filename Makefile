help:
	@echo "Available commands:"
	@echo ""
	@echo "test: run tests for neigefr"

test:
	tox -- flakes
