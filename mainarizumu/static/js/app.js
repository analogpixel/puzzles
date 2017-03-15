
var constraintList = {};
var puzSize = 6;
var letters = ['a','b','c','d','e','f'];
//var numbers = [1,2,3,4];
var numbers = range(1, puzSize);

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
	var puzdata = JSON.stringify(puz);
	//console.log(puzdata);

	$.post("/solve", {'puzzleData': puzdata, 'puzSize': puzSize},  
		(d) => { 
			d = JSON.parse(d);
			//console.log(d);
			//console.log(typeof(d));
			var posSolutions = {};

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
			//console.log(posSolutions);

			// now fill in the values
			Object.keys( posSolutions).forEach( (d) => {
				//console.log(d, posSolutions[d].join(","))
				$("#" + d).html( posSolutions[d].join(",") );
			} );


		} );

}

function range(start, count) {
      return Array.apply(0, Array(count))
        .map(function (element, index) { 
          return index + start;  
      });
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

$( function() { 

	html = "<table border=0>\n";
	for (var j=0; j < puzSize; j++) {
		
		var l1 = letters[j];
		var l2 = letters[j+1];

		// horizontal constraints
		html += "<tr>\n";

		for (var i=1; i < puzSize; i++) {
			html += '<td><div class=num id="' + l1 + i + '"></div></td>\n';
			html += '<td><div onclick="updateConstraint(this.id, \'h\')" class=hconstraint id="' + l1 + i + "_" + l1 + (i+1) + '"></div></td>\n'
		}
		html += '<td><div class=num id="' + l1 + puzSize + '"></div></td>\n';
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

} );