SRCS:= $(wildcard *.md)
OBJS:= $(patsubst %.md,%.html,$(SRCS))

all: $(OBJS)

%.html: %.md
	pandoc $< -o $@
