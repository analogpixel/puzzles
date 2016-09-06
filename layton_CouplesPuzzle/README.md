
This is a simple logic puzzle that requires you use the clues given to determine where a couple is sitting.  Seems easy enough... UNTIL YOU TRY TO DO IT IN PROLOG!

Although I did get prolog to give me the correct answer, It wasn't provided with ALL the information in the puzzle, and if you kept asking for more answers to the puzzle, it was more than happy to give them out.

I started out defining what I knew:
```prolog
woman(a).
woman(e).
woman(d).
woman(g).

man(b).
man(c).
man(f).
man(h).

% this is always ordered so the male is first then the female
% this makes the compat check easier
besides(b,a).
besides(c,d).
besides(h,g).
besides(f,e).
% acrossfrom(f,b). % we know a,b are together so this doesn't make sense
acrossfrom(c,g).
acrossfrom(h,d).

```

Then I created a rule stating what it meant for a couple to be compatible in the Nintendo world of puzzle games (this puzzle gets much harder in the real world...)

```prolog
% to be compatible you have to be a man and a woman (for this puzzle)
% and you have to either sit beside or across from your partner
compat(X,Y) :- man(X),woman(Y), ( besides(X,Y) ; (acrossfrom(X,Y))).
```


Once I got all that together, I built my solving rule which I figured out from reading [this page](http://www.cis.upenn.edu/~matuszek/cis554-2011/Assignments/prolog-01-logic-puzzle.html) over and over and over...

```prolog
solve :-
	% have the variables P1-P8 assign to the actual data
	man(P1), man(P5), man(P7),
	woman(P2), woman(P6), woman(P8),

	% create the list that will hold the answer
	Triples = [ [jones, P1, P2],
		    [oconnars,b,a],
		    [lamberts,P5,P6],
		    [hadleys,P7,P8]
		  ],

	% make sure the answeres selected are valid.
	compat(P1,P2), compat(P5,P6), compat(P7,P8),

	% make sure that everything returned is unique
	all_different([P1,P2,P5,P6,P7,P8]),

	% start filling variables into the list
	% to see if we can get some values
	member([jones,P1,P2], Triples) ,
	member([lamberts, P5,P6], Triples),
	member([hadleys, P7,P8], Triples),

	% print out the answer
	tell(hadleys, P7,P8).

tell(X, Y, Z) :-
    write('Couple. '), write(X), write(' : '), write(Y),
    write(Z), write('.'), nl.

```

The trick that the link above helped me figure out for solving logic puzzles, is to build a list of lists, and then fill in the parts of the list you know.  Once the list is full, you have your answer.

What this solution is currently lacking, is inputting the relationships we were given (Joneses are across from each other, O'Connors sit beside each other....), to lock the puzzle down to just one solution.   Hopefully once I get a better grasp on prolog, I can come back to this puzzle and add in the rest of the data to lock it down.

With the current setup, the first two solutions are EF, which makes E the answer.
