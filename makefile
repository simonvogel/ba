CXX = g++
CXXFLAGS = -std=c++11 -O3

all: plots

plots: data
	python plot.py

data: main
	rm -f -r data1
	rm -f -r data2
	mkdir -p data1
	mkdir -p data2
	./main

main: main.cpp
	$(CXX) $(CXXFLAGS) -o $@ $^
	
clean:
	rm -f -r main
