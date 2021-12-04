.PHONY: flake8

flake8:
	flake8 */*.py

clean:
	rm -fr *~ */*~ */__pycache__
