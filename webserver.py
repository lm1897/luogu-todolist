import spider

def read(path):
	f = open(path, 'r+')
	t = f.read()
	f.close()
	return t

def index():
	spider.update()
	table = read('web/table.html')
	text = read('web/index.html').replace('{{ table main }}', table)
	return text