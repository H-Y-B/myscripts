dir:=$(shell pwd)
#------------------------------------------------------------------------
SCALA_VERSION=2.12.10
SCALA_VERSION_MAJOR=$(basename $(SCALA_VERSION))
#$(basename NAMES…) 
#函数名称：取前缀函数—basename。 
#函数功能：从文件名序列“NAMES…”中取出各个文件名的前缀部分（点号之前的
#部分）。前缀部分指的是文件名中最后一个点号之前的部分。 
#------------------------------------------------------------------------
path=/home/temp/a.txt
a=$(basename $(path))
b=$(shell basename $(path))
c=$(shell dirname $(path))
#------------------------------------------------------------------------
main:
	@echo $(dir)
	@echo $(SCALA_VERSION_MAJOR)
	@echo "path:" $(path)
	@echo $(a)
	@echo $(b)
	@echo $(c)
