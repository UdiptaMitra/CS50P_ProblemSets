import sys

# Basic attributes
print("Version:", sys.version)
print("Version info:", sys.version_info)
print("Executable path:", sys.executable)
print("Platform:", sys.platform)
print("Byte order:", sys.byteorder)
print("Max size of int:", sys.maxsize)

# Command-line arguments
print("Command-line args:", sys.argv)

# Standard I/O
print("Writing to stdout using sys.stdout.write -> ", end="")
sys.stdout.write("Hello from stdout\n")

sys.stderr.write("This is stderr (error stream example)\n")

# Recursion limit
old_limit = sys.getrecursionlimit()
print("Old recursion limit:", old_limit)
sys.setrecursionlimit(1200)
print("New recursion limit:", sys.getrecursionlimit())

# Modules loaded
print("Number of modules currently loaded:", len(sys.modules))

# Path for module search
print("Module search paths (sys.path):")
for p in sys.path:
    print(" ", p)

# System flags
print("System flags:", sys.flags)

# System float info
print("Float info:", sys.float_info)

# System integer info
print("Integer info:", sys.int_info)

# Implementation details
print("Python implementation:", sys.implementation)

# Checking if stdin is interactive
print("Is stdin interactive:", sys.stdin.isatty())

# Getting current filesystem encoding
print("Filesystem encoding:", sys.getfilesystemencoding())

# Display default encoding
print("Default encoding:", sys.getdefaultencoding())

# Show the refcount of an object
a = []
print("Reference count of a list object:", sys.getrefcount(a))

# Exit example (won’t actually exit here)
print("Exit code example -> sys.exit(0)  # Not executed")
