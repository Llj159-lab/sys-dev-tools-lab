import subprocess

subprocess.Popen("echo first", shell=True)

subprocess.Popen(
    "echo second",
    shell=True,
)
