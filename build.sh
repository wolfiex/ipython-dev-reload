if [ -z "$PYTHON" ]; then PYTHON=$(which python); fi
$PYTHON setup.py install     # Python command to install the script.
