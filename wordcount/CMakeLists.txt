CMAKE_MINIMUM_REQUIRED(VERSION 2.8.3)
PROJECT(PythonCppExt)

FIND_PACKAGE(PythonLibs)
FIND_PACKAGE(Boost COMPONENTS python)

INCLUDE_DIRECTORIES(${Boost_INCLUDE_DIRS} ${PYTHON_INCLUDE_DIRS})

PYTHON_ADD_MODULE(cppExtUtil util.cpp)

TARGET_LINK_LIBRARIES(cppExtUtil ${Boost_LIBRARIES})
TARGET_LINK_LIBRARIES(cppExtUtil ${PYTHON_LIBRARIES})
