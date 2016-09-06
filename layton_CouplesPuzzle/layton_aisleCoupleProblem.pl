
% http://www.cis.upenn.edu/~matuszek/cis554-2011/Assignments/prolog-01-logic-puzzle.html

% set stack to 2 gig
set_prolog_stack(global, limit(8*10**9)).

all_different([H | T]) :- member(H, T), !, fail.
all_different([_ | T]) :- all_different(T).
all_different([_]).

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

% to be compatible you have to be a man and a woman (for this puzzle)
% and you have to either sit beside or across from your partner
compat(X,Y) :- man(X),woman(Y), ( besides(X,Y) ; (acrossfrom(X,Y))).

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





