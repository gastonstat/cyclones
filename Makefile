# phony target is a target that is always out-of-date,
.PHONY: data test analysis report

data:
	cd data && make download_all

test:
	nosetests code/tests

analysis:
	cd code/scripts && python count_cyclones_script.py

report:
	cd report && make all
	cd report && make clean
