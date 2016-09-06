It's always fun to submit your "right" answer, only to have the game come back and say "WRONG!"  and then you are like: wha? but my lisp program, it's flawless, there is no way it could be flawed, except... wait... Crap, I forgot to add a node to the map!

Lisp is one of those funny languages that force you to think in lisp to get things done; this is probaly a good thing, but when you flop around from language to language all the time, it takes some time to get back into the lisp groove; "what do you mean there is no foreach!"

To solve the problem I just created a recursive function that first checks that the incoming nodes weren't already in the solution, and then called itself again with the incoming nodes while counting the path length.  When the recursive function gets to the finish, it'll check the current largest path with what it has and update it if needed.

This isn't the cleanest program in the world, but it got the job done:
