
# Windows nmake makefile

CXX=cl
LINK=link

FLAGS=/EHsc /std:c++17 /I./src/ /c /Fo:./obj/
TESTFLAGS=/EHsc /std:c++17 /I/lib/boost/ /I./src/ /I./test/ /c /Fo:./obj/

SRC=./src/frog.cpp
OBJ=./obj/frog.obj

TESTSRC=./test/test.cpp ./src/frog.cpp
TESTOBJ=./obj/test.obj ./obj/frog.obj

INC=./src/frog.hpp
TESTINC=./test/test-frog.hpp

TARGET=frog.dll
TEST=test.exe

all: dir $(TARGET)
test: dir $(TEST)

dir: 
	-@ if NOT EXIST "./bin/" mkdir "./bin/"
	-@ if NOT EXIST "./obj/" mkdir "./obj"

$(TARGET):	$(OBJ)
	$(LINK) /DLL /OUT:./bin/$(TARGET) $(OBJ)

$(TEST):	$(TESTOBJ)
	$(LINK) /OUT:./bin/$(TEST) $(TESTOBJ)

obj/frog.obj: ./src/frog.cpp $(INC)
	$(CXX) $(FLAGS) ./src/frog.cpp

obj/test.obj: ./test/test.cpp $(INC) $(TESTINC)
  $(CXX) $(TESTFLAGS) ./test/test.cpp
