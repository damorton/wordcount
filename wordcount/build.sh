#!/bin/bash

mkdir -p build
cd build

PYTHON_VERSION=`python -c "import sys;t='{v[0]}.{v[1]}'.format(v=list(sys.version_info[:2]));sys.stdout.write(t)";`
PYTHON_LIBRARY=/usr/local/Frameworks/Python.framework/Versions/$PYTHON_VERSION/lib/libpython$PYTHON_VERSION.dylib
PYTHON_INCLUDE_DIR=/usr/local/Frameworks/Python.framework/Versions/$PYTHON_VERSION/Headers/
cmake -DPYTHON_LIBRARY=$PYTHON_LIBRARY -DPYTHON_INCLUDE_DIR=$PYTHON_INCLUDE_DIR -DCMAKE_BUILD_TYPE=DEBUG .. && make
