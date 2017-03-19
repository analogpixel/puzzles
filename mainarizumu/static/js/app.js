
var constraintList = {};
var puzSize = 2;
var allLetters = ['a','b','c','d','e','f','g','h','i','j','k','l'];
var letters = ['a','b'];
//var numbers = [1,2,3,4];
var numbers = range(1, puzSize);
var allSolutions = false;
var currentSolution = 0;

function setSize(n) {
	puzSize = n;
	letters = allLetters.slice(0,n);
	constraintList = {};
	numbers = range(1, puzSize);
	console.log( puzSize, numbers, letters);
	$("#solution").html("");
	buildPuzzle();

}

function nextSolution() {
	currentSolution++;
	if (currentSolution >= allSolutions.length) { currentSolution = 0; }
	fillInSolution();
}

function prevSolution() {
	currentSolution = currentSolution - 1;
	if (currentSolution < 0) { currentSolution = allSolutions.length -1; }
	fillInSolution();
}

function fillInSolution() {
	posSolutions = allSolutions[currentSolution];


	console.log( currentSolution, posSolutions);
	$("#solution").html("<button class='btn btn-md btn-default' onclick='prevSolution()'>prev</button> Solution " + (currentSolution+1) + " of " + (allSolutions.length) + " <button class='btn btn-md btn-default' onclick='nextSolution()'>next</button><br><br>" );

	// now fill in the values
	Object.keys( posSolutions).forEach( (d) => {
		//console.log(d, posSolutions[d].join(","))
		$("#" + d).html( posSolutions[d] );
	} );
}

function solvePuzzle() {
	console.log("solving");
	
	var puz = [];

	for  (k in constraintList) {

		var tmp = constraintList[k];
		var cmd = "";

		if (tmp == 0 ) {
			continue;
		} else if (tmp == 1) {
			cmd = "gt";
			puz.push( ['gt', k.split("_") ])
		} else if (tmp == 2) {
			cmd = "lt";
			puz.push( ['lt', k.split("_") ])
		} else {
			cmd = "dif";
			puz.push( ['dif', k.split("_"), tmp -2])
		}
		//console.log(k, cmd, tmp);
	}

	letters.forEach( (letter) => {
			numbers.forEach ( (number) => {
				var tmp = $("#" + letter + number).html();
				if (tmp != "") {
					puz.push( ['eq', letter + number, parseInt(tmp)] );
				}
			});
		});

	console.log("puzzle:", puz);

	var puzdata = JSON.stringify(puz);
	//console.log(puzdata);

	$.blockUI({ message: '<h1>Solving puzzle please wait</h1><br><img src=static/img/loading.gif><br><br>' }); 

	$.post("/solve", {'puzzleData': puzdata, 'puzSize': puzSize},  
		(d) => { 
			d = JSON.parse(d);
			$.unblockUI();
			//console.log(d);
			//console.log(typeof(d));
			var posSolutions = {};

			console.log(d);
			
			allSolutions = d;
			currentSolution = 0;
			fillInSolution();
			/*
			d.forEach( (el) => {
				//console.log( typeof(el) );
				Object.keys(el).forEach( (okeys) => {
					if (okeys in posSolutions) {
						//console.log(typeof(posSolutions[okeys] ));
						if (  posSolutions[okeys].indexOf( el[okeys] ) == -1) {
							posSolutions[okeys].push( el[okeys]);
						}
					} else {
						posSolutions[okeys] = [ el[okeys] ] ;
					}
				});
			} );
			*/

			//console.log(posSolutions);

			


		} );

}

function range(start, count) {
      return Array.apply(0, Array(count))
        .map(function (element, index) { 
          return index + start;  
      });
    }

function updateNumBlock(t) {

	var tmp = $("#" + t).html();

	if (tmp == "") { 
		$("#" + t).html("1");
	} else {
		var n = parseInt(tmp);
		n++;
		if (n > puzSize) { n = "";}
		$("#" + t).html(n);

	}
}

function updateConstraint(t,ctype) {
	// console.log(t,ctype);

	var hoptions = ['','>','<'].concat(  numbers);
	var voptions = ['','&or;','&and;'].concat(  numbers);
	var c = 0;

	if (t in constraintList) {
		c = constraintList[t];
	} 

	c++;
	if (c > hoptions.length-1) { c = 0; };


	if (ctype == 'v') {
		$("#" + t).html( voptions[c] );
	} else {
		$("#" + t).html( hoptions[c] );
	}

	constraintList[t] = c;

}

$( function() { buildPuzzle(); } );

function buildPuzzle() { 

	html = "<table border=0>\n";
	for (var j=0; j < puzSize; j++) {
		
		var l1 = letters[j];
		var l2 = letters[j+1];

		// horizontal constraints
		html += "<tr>\n";

		for (var i=1; i < puzSize; i++) {
			html += '<td><div onclick="updateNumBlock(this.id)" class=num id="' + l1 + i + '"></div></td>\n';
			html += '<td><div onclick="updateConstraint(this.id, \'h\')" class=hconstraint id="' + l1 + i + "_" + l1 + (i+1) + '"></div></td>\n'
		}
		html += '<td><div class=num onclick="updateNumBlock(this.id)" id="' + l1 + puzSize + '"></div></td>\n';
		html += "</tr>\n";

		if (j < puzSize -1) {
			// vertial constrains
			html += "<tr>\n";
			for (var i=1; i < puzSize; i++) {
				html += '<td><div onclick="updateConstraint(this.id, \'v\')" class=vconstraint id="' + l1 +  i + "_" + l2 + i + '"></div></td>\n';
				html += '<td><div class=null></div></td>\n';
			}
			html += '<td><div onclick="updateConstraint(this.id, \'v\')" class=vconstraint id="' + l1  +  i + "_" + l2 + i + '"></div></td>\n';
			html += "</tr>\n";
		}
	}

	html += "</table>";

	$("#puzzle").html(html);
	//console.log(html);

} 