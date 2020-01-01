
# LeapingFrog

Simulating an equiprobable leaping frog

## Pupose

This programme was developed after watching [a video](https://www.youtube.com/watch?v=ZLTyX4zL2Fc) made by [Matt Parker](https://www.youtube.com/user/standupmaths) ([standupmaths](http://standupmaths.com/)). The video contains a puzzle expounded as that of a frog crossing a river, with nine lily pads betweeen the bank it is on and the other. The frog is able to leap to any of the lily pads in front of it or the other bank and is equally likely to leap to any of them. Once it has leapt forward, it is equally likely to jump to any of the remaining pads in front of it or the other bank. The frog only moves forward. The question, thence, is what is the average number of leaps taken by the frog crossing the river.

## Output

The following visualisation is an example of that made by the programme, showing the approximation of the tenth harmonic number.

![Simulation Results](https://drive.google.com/uc?id=1SG7Xxey8d979ZHCJCyhAGkb-lOllLvHp)

Each of the blue lines on the above plot is the moving average of the number of leaps needed to cross the river in one simulation. Each simulation repeats the experiment 1,000,000 times, and there are 150 simulations. As can be seen, each simulation approaches the true value, given by the solid red line,
