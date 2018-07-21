class WriteData:
	def __init__(self, list, output_file):
		self.player_list = list
		self.output_file = output_file

	def write_player_data(self):
		file = open(self.output_file, 'w')

		for p in self.player_list:
			line = str(p.first_name) + ", " + str(p.last_name) + ", " + str(p.AB) + ", " + str(p.H) + ", " + str(p.DOUBLE) + ", " + str(p.TRIPLE) + ", " + str(p.HR) + ", " + str(p.BB) + ", " + str(p.HBP) + ", " + str(p.IBB) + ", " + str(p.SB) + ", " + str(p.CS) + ", " + str(p.GIDP) + ", " + str(p.SH) + ", " + str(p.SF) + ", " + str(p.BA) + ", " + str(p.OBP) + ", " + str(p.SLG) + ", " + str(p.OPS) + ", " + str(p.TB) + ", " + str(p.RC) + ", " + str(p.TA) + ", " + str(p.ISO) + ", " + str(p.SECA) + ", " + str(p.RC27) + ", " + str(p.get_hit)
			file.write(line)
			file.write("\n")

		file.close()
