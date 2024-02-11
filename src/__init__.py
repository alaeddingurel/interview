import os
import sys

# Get the path to the parent directory of 'src'
project_root = os.path.dirname(os.path.dirname(__file__))

# Add the parent directory of 'src' to the Python path
sys.path.append(project_root)