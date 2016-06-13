FILES :=              \
    Hello             \
    UnitTests3        \
    Coverage1         \
    Coverage2         \
    Coverage3         \
    Exceptions        \
    Types             \
    Operators         \
    Variables         \
    Cache             \
    Copy

ifeq ($(CI), true)
    PYLINT := pylint
else
	PYLINT := pylint3
endif

.pylintrc:
	$(PYLINT) --disable=bad-whitespace,missing-docstring,invalid-name,locally-disabled,pointless-string-statement --reports=n --generate-rcfile > $@

%.pyx: %.py .pylintrc
	-$(PYLINT) $<
	./$<

clean:
	rm -f  *.pyc
	rm -f  .pylintrc
	rm -rf __pycache__

test: $(FILES:=.pyx)
