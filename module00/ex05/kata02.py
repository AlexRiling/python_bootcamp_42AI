# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

# Formatting and printing the output
formatted_output = "{:02}/{:02}/{:04} {:02}:{:02}".format(kata[1], kata[2], kata[0], kata[3], kata[4])
print(formatted_output)
