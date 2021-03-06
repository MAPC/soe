from PIL import Image
import glob, os

size = 270, 540

for infile in glob.glob("graphs/*"):
	file, ext = os.path.splitext(infile)
	format = ext[1:].upper()
	if format in ("JPG", "PNG", "GIF", "BMP"):
		if format == "JPG":
			format = "JPEG"
		im = Image.open(infile)
		im.thumbnail(size, Image.ANTIALIAS)
		im.save(file + ".270x540" + ext, format)