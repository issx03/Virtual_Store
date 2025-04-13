import os
import sys

# Add the src directory to the Python path
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
print(f"Adding to path: {src_path}")
sys.path.insert(0, src_path)

# Try to import the modules
try:
    import models
    print("Successfully imported models")
except ImportError as e:
    print(f"Failed to import models: {e}")

try:
    import modules
    print("Successfully imported modules")
except ImportError as e:
    print(f"Failed to import modules: {e}")

# Print the Python path
print("\nPython path:")
for path in sys.path:
    print(path)

