SRCS:= $(wildcard */body.md)
OBJS:= $(patsubst %.md,%.html,$(SRCS))

all: $(OBJS)

%.html: %.md
	pandoc --mathjax $< -o $@
