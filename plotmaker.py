def plotmaker(data, header):

	fig = plt.figure(figsize=(14, 4))

	for i in range(1, len(data) ):

		plt.plot( data[0, :], data[i, :], label = header[i -1])

	plt.xlabel("C stężenie")
	plt.ylabel("Y sygnał")

	plt.legend()
	plt.show()

	fig, ax = plt.subplots()

if __name__ == "__main__":
	data = np.array([OX, OY_1, OY_2])

	header = ["Miejsce1", "Miejsce2"]

	print(plotmaker(data, header))

#cześć
