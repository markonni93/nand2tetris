import os, subprocess as sp
print("Starting all test")
success_response = b'End of script - Comparison ended successfully\n'
for file in os.listdir("."):
	if file.endswith(".tst"):
		cmd = "HardwareSimulator.sh " + file
		out = sp.check_output(cmd.split())
		print('-' * 30)
		print("Checking out " + file)
		print(out)
		if out != success_response:
			print("Done: Error")
			break;
		print("Done: Test ok")
print("All tests done")