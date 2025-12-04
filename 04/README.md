# Day 4

![Python code](python.png)

Part 1 is fairly simple, I wasted some time by implementing 'looping' logic because I misunderstood the problem, but aside from that it's fairly trivial to check surrounding spaces, just have to avoid overflows.

Part 2 was a fun one, I implemented a hashmap (though a list would likely work just as well) that would keep track of 'to be removed' rolls), then removed them after going through the entire room, and looped until I never removed one.

Python - input

real	0m0.249s
user	0m0.246s
sys	0m0.002s

