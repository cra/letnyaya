# Takes conf rules from ./conf, can be overrided by pass conf variable:
# make conf=custom.conf
# writted for GNU Make, so:
# IMPORTANT: should be run by gmake under FreeBSD

conf = conf

# allow comments that start with #
define sed-rules
	$(shell cat $(conf) | egrep -v "^\s*#")
endef

all: conf.py httpd.conf issl.wsgi 

conf.py: conf.py.template conf Makefile
	@echo Создаем conf.py
	@sed $(foreach rule, $(sed-rules), -e $(rule)) < conf.py.template > conf.py

httpd.conf: httpd.conf.template conf Makefile
	@echo Создаем httpd.conf
	@sed $(foreach rule, $(sed-rules), -e $(rule)) < httpd.conf.template > httpd.conf

archive.wsgi: issl.wsgi.template conf Makefile
	@echo Создаем issl.wsgi
	@sed $(foreach rule, $(sed-rules), -e $(rule)) < issl.wsgi.template > issl.wsgi

.PHONY : clean
clean :
	rm -f conf.py httpd.conf issl.wsgi

temp_dist_dir = temp_dist_dir
distr_branch = trunk
distr_name = archive

.PHONY : distr
distr :
	rm -rf ${temp_dist_dir}
	mkdir ${temp_dist_dir}
	svn export http://svn.chtd.org/${distr_branch}/archive ${temp_dist_dir}/archive
	svn export http://svn.chtd.org/${distr_branch}/lib ${temp_dist_dir}/lib
	zip -r ${distr_name}.zip ${temp_dist_dir}
	rm -rf ${temp_dist_dir}
