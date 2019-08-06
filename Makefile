CXXFLAGS=
all: unicode
unicode: unicode.o
	$(CXX) $(CXXFLAGS) unicode.o -o unicode
unicode.o: unicode.cpp
	$(CXX) $(CXXFLAGS) -c unicode.cpp -o unicode.o
clean:
	rm unicode *.o
.PHONY: clean
