y0 = {"year": "2023-24", "season_total": 213, "sept/oct": 6,   "nov": 33,  "dec": 91,   "jan":	83}
y1 = {"year": "2022-23", "season_total": 617, "sept/oct": 16,  "nov": 75,  "dec": 135,  "jan":	81,   "feb": 126, 	"mar": 103, "apr":   81}
y2 = {"year": "2021-22", "season_total": 648, "sept/oct": 12,  "nov": 59,  "dec": 189,  "jan":	93,   "feb": 74,  	"mar": 93, "apr":    128}
y3 = {"year": "2020-21", "season_total": 704, "sept/oct": 8,   "nov": 122, "dec": 142,  "jan":	155,  "feb": 133, 	"mar": 104, "apr":   40}
y4 = {"year": "2019-20", "season_total": 686, "sept/oct": 13,  "nov": 22,  "dec": 90,   "jan":	294,  "feb": 115, 	"mar": 129, "apr":   23}
y5 = {"year": "2018-19", "season_total": 538, "sept/oct": 5,   "nov": 31,  "dec": 205,  "jan":	90,   "feb": 130, 	"mar": 36, "apr":    41}
y6 = {"year": "2017-18", "season_total": 844, "sept/oct": 15,  "nov": 126, "dec": 125,  "jan":	225,  "feb": 156, 	"mar": 111, "apr":   86}
y7 = {"year": "2016-17", "season_total": 866, "sept/oct": 5,   "nov": 115, "dec": 207,  "jan":	70,   "feb": 133, 	"mar": 269, "apr":   67}
y8 = {"year": "2015-16", "season_total": 622, "sept/oct": 0,   "nov": 94,  "dec": 186,  "jan":	103,  "feb": 109.5, "mar": 114.5, "apr": 15}
y9 = {"year": "2014-15", "season_total": 303, "sept/oct": 21,  "nov": 41,  "dec": 83,   "jan":	48,   "feb": 18.5, "mar":  42.5, "apr":  49}
ya = {"year": "2013-14", "season_total": 623, "sept/oct": 40,  "nov": 46,  "dec": 66,   "jan":	87,   "feb": 157.5, "mar": 164, "apr": 	 62.5}
yb = {"year": "2012-13", "season_total": 740, "sept/oct": 21,  "nov": 84,  "dec": 251,  "jan":	119,  "feb": 110, "mar":   103, "apr":   52}
yc = {"year": "2011-12", "season_total": 808, "sept/oct": 0,   "nov": 147, "dec": 47,   "jan":	197,  "feb": 126, "mar":   260, "apr":   31}
yd = {"year": "2010-11", "season_total": 857, "sept/oct": 0,   "nov": 103, "dec": 176,  "jan":	109,  "feb": 118, "mar":   227, "apr":   124}


def calculate_edit_dist(year_a, year_b):
	"""Calculates the "snowfall edit distance" between two years"""
	months = ["sept/oct", "nov", "dec", "jan"]
	dist_arr = []
	id_str = year_b["year"] + " / " + year_a["year"]
	for month in months:
		dist_arr.append(abs(year_a[month] - year_b[month]))
	return (sum(dist_arr), id_str, dist_arr)

def main():
	for year in [y1, y2, y3, y4, y5, y6, y7, y8, y9, ya, yb, yc, yd]:
		print(calculate_edit_dist(y0, year))

if __name__ == '__main__':
	main()
