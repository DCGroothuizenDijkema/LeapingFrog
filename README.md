
# LeapingFrog

Simulating an equiprobable leaping frog

## Pupose

This programme was developed after watching [a video](https://www.youtube.com/watch?v=ZLTyX4zL2Fc) made by [Matt Parker](https://www.youtube.com/user/standupmaths) ([standupmaths](http://standupmaths.com/)). The video contains a puzzle expounded as that of a frog crossing a river, with nine lily pads betweeen the bank it is on and the other. The frog is able to leap to any of the lily pads in front of it or the other bank and is equally likely to leap to any of them. Once it has leapt forward, it is equally likely to jump to any of the remaining pads in front of it or the other bank. The frog only moves forward. The question, thence, is what is the average number of leaps taken by the frog crossing the river.

## Output

The following visualisation is an example of that made by the programme, showing the approximation of the tenth harmonic number.

![Simulation Results](https://drive.google.com/uc?id=1SG7Xxey8d979ZHCJCyhAGkb-lOllLvHp)

Each of the blue lines on the above plot is the moving average of the number of leaps needed to cross the river in one simulation. Each simulation repeats the experiment 1,000,000 times, and there are 150 simulations. As can be seen, each simulation approaches the true value, given by the solid red line.

## Building

The programme can be built with the provided Makefile and nmake, with the following command:

```shell
nmake all
```

The tests can be built with the provided Makefile and nmake, with the following command:

```shell
nmake test
```

Note the following two build commands require ```./bin/``` and ```./obj/``` directories to be created before executing either of the commands.

Further, the programme can be built using MSVC on the command line with the following command:

```shell
cl /EHsc /LD /std:c++17 /Fo:./obj/ /I./src/ ./src/*.cpp /link/OUT:./bin/frog.dll /IMPLIB:./bin/frog.lib
```

The tests can be built on the command line with:

```shell
cl /EHsc /std:c++17 /Fo:./obj/ /Fe:./bin/test /I/lib/boost/ /I./src/ /I./test/ @./test/test_files.txt
```

In all instances, you may have to change the specification of the Boost library, given by ```/I/lib/boost/```, depending on where it is stored on your system.

## Dependencies

This project uses the Boost C++ libraries for testing, version 1.71.0, which can be found at <https://www.boost.org/>.

This project also uses my huygens Python library, which can he found at <https://github.com/DCGroothuizenDijkema/huygens/>, as well as the [num2words](https://pypi.org/project/num2words/) Python package.

## Tests

The source for testing this programme can be found in ```./test/``` and the tests can be run, once compiled, with ```./bin/test```.
