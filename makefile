clean:
	cd examples; make clean
	@echo
	cd exercises; make clean
	@echo
	cd collatz; make clean

config:
	git config -l

init:
	touch README
	git init
	git add README
	git commit -m 'first commit'
	git remote add origin git@github.com:gpdowning/cs373.git
	git push -u origin master

pull:
	make clean
	@echo
	git pull
	git status

push:
	make clean
	@echo
	git add .travis.yml
	git add examples
	git add exercises
	git add collatz
	git add makefile
	git commit -m "another commit"
	git push
	git status

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

sync:
	@rsync -r -t -u -v --delete              \
    --include "Hello.py"                     \
    --include "Assertions.py"                \
    --include "UnitTests1.py"                \
    --include "UnitTests2.py"                \
    --include "UnitTests3.py"                \
    --include "Coverage1.py"                 \
    --include "Coverage2.py"                 \
    --include "Coverage3.py"                 \
    --include "Exceptions.py"                \
    --include "Types.py"                     \
    --include "Operators.py"                 \
    --include "Variables.py"                 \
    --include "Cache.py"                     \
    --include "Copy.py"                      \
    --exclude "*"                            \
    ../../examples/python/ examples
	@rsync -r -t -u -v --delete              \
    --include "IsPrime1.py"                  \
    --include "IsPrime1T.py"                 \
    --include "IsPrime2.py"                  \
    --include "IsPrime2T.py"                 \
    --include "FactorialT.py"                \
    --include "ReduceT.py"                   \
    --exclude "*"                            \
    ../../exercises/python/ exercises
	@rsync -r -t -u -v --delete              \
    --include "Collatz.py"                   \
    --include "RunCollatz.in"                \
    --include "RunCollatz.py"                \
    --include "RunCollatz.out"               \
    --include "TestCollatz.py"               \
    --include "TestCollatz.out"              \
    --exclude "*"                            \
    ../../projects/python/collatz/ collatz

test:
	make clean
	@echo
	cd examples; make test
	@echo
	cd exercises; make test
	@echo
	cd collatz; make test
