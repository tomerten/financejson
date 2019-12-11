## compile requirements file to fix versions
.PHONY: requirements
requirements:
	@if [[ ! -f requirements.txt ]]; then \
		touch requirements.txt; \
	fi
	python3 -m piptools compile --output-file requirements.tmp requirements.in  && \
		cat requirements.tmp > requirements.txt