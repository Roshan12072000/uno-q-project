import subprocess
import os
from datetime import datetime

# Project paths
SOURCE_FILE = "src/unoq_info.c"
OUTPUT_FILE = "unoq_info"
LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

# Build log
build_log = open(f"{LOG_DIR}/build.log", "w")

print("Starting build process...")

build = subprocess.run(
    ["gcc", SOURCE_FILE, "-o", OUTPUT_FILE],
    capture_output=True,
    text=True
)

build_log.write("Build started: " + str(datetime.now()) + "\n")
build_log.write(build.stdout)
build_log.write(build.stderr)
build_log.write(f"Build return code: {build.returncode}\n")
build_log.close()

if build.returncode != 0:
    print("BUILD FAILED")
    exit(1)

print("BUILD SUCCESSFUL")

# Test execution
test_log = open(f"{LOG_DIR}/test.log", "w")

print("Starting test execution...")

test = subprocess.run(
    ["./" + OUTPUT_FILE],
    capture_output=True,
    text=True
)

expected_output = [
    "Arduino UNO Q Project",
    "Embedded Linux Development",
    "Git Workflow Practice on UNO Q",
    "Git modification and update practice",
    "Feature branch testing on UNO Q"
]

test_log.write("Test started: " + str(datetime.now()) + "\n")
test_log.write("Program output:\n")
test_log.write(test.stdout)
test_log.write(test.stderr)

if test.returncode == 0 and all(
    line in test.stdout.splitlines() for line in expected_output
):
    test_log.write("\nTEST PASSED\n")
    print("TEST PASSED")
else:
    test_log.write("\nTEST FAILED\n")
    print("TEST FAILED")

test_log.write(f"Test return code: {test.returncode}\n")
test_log.close()
if test.returncode != 0 or not all(
    line in test.stdout.splitlines() for line in expected_output
):
    exit(1)
