SRCS:= $(wildcard static/blog/*/body.md)
OBJS:= $(patsubst %.md,%.html,$(SRCS))

all: static/main/main.html $(OBJS)

%.html: %.md
	pandoc --mathjax $< -o $@
