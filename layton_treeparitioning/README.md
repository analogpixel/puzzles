For some reason this puzzle seemed to be harder than is should have been.  It could have been the less than optimal solution I went for, but it took me about a week of on and off work to finally finish it.  But even if this solution doesn't land me a job a Google (but hey if you need someone to clean your blackboards [here](http://analogpixel.org/contact) is my contact info), I learned few things solving it:

* <p>A debugger is a must; coding without a debugger is like driving a car with a blind fold and readjusting your course when you bump into things.</p>
* <p>Don't try to string along huge strings of lisp code;  just break things into little functions and string those together.  If you get stuck somewhere, try breaking something into separate functions so you can better see how your code is working.</p>
* <p>map(cat) and filter are your friends; your best f'n friends.  Use them whenever you can.</p>
* <p>Restructure your data to best match how you plan to process it.</p>

## Solving the problem
To solve the problem I took this path:

* <p>First, I setup the data as a linked(ish) list(ish) type of thing.  Each square had it's type (of tree 0-4) and what connections it had.  Initial I just had a row/col setup, and was calculating x,y and movement around, but this got tedious fast.  Being able to just ask what connections a square has and then move based on that is much easier.</p>
* <p>next, for EVERY square, I found every possible combination of moves that would give you 4 tiles (even if they aren't valid solutions.)</p>
* <p>Then I filtered out all only valid solutions (4 distinct trees)</p>
* <p>I did this for every square, and then I did I took all possible combinations of mixing 4 groups together.</p>
* <p>from those combinations, I flattened the list, took a distinct of them to get non repeating tiles, and the found the answer(s) that had exactly 16 non repeating tiles.</p>

## Other issues
Initial I was just walking from square to square recursively (because everything in clojure is recursively), but since my walking never walked back on itself correctly, I could never make a T shape, which was needed to solve the puzzle.  Then I realized I could just take all combinations of the cross that intersects the square you care about, and merge that with another cross of a nearby square, and continue doing that until you have a bunch of possible solutions to try.

I also ran into some self imposed road blocks trying to loopy loop over stuff, until I realized I could just call a function recursively from mapcat and have it apply multiple values recursively for me.

