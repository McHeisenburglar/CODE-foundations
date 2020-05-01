var currentTurn = 'x';
var tiles = document.getElementsByClassName('tile empty');
console.log("PAGE LOAD SUCCESS.")
console.log(tiles)

// const x_axis = ['b_left', 'b_middle', 'b_right'];
// const y_axis = ['b_top', 'b_center', 'b_bottom'];

var tile1 = document.getElementsByClassName('b_left');
console.log(tile1.length);
// var tile01 = document.getElementsByClassName(x_axis[1], y_axis[0])[0];
// var tile02 = document.getElementsByClassName(x_axis[2], y_axis[0])[0];
// var tile10 = document.getElementsByClassName(x_axis[0], y_axis[1])[0];
// var tile11 = document.getElementsByClassName(x_axis[1], y_axis[1])[0];
// var tile12 = document.getElementsByClassName(x_axis[2], y_axis[1])[0];
// var tile20 = document.getElementsByClassName(x_axis[0], y_axis[2])[0];
// var tile21 = document.getElementsByClassName(x_axis[1], y_axis[2])[0];
// var tile22 = document.getElementsByClassName(x_axis[2], y_axis[2])[0];

// console.log(tile1[0].textContent)
// console.log("Example: Tile 2-1 is " + tile1[0])

function changeTurn() {
	let header = document.getElementById('turn');
	if (currentTurn == 'x') {
		header.childNodes.item(1).textContent = "Player O's";
		header.className = 'o';
		currentTurn = 'o';
	} else {
		header.childNodes.item(1).textContent = "Player X's";
		header.className = 'x';
		currentTurn = 'x';
	}
	// console.log("Changed turn to " + currentTurn)
};

function placeTurn(tileId) {
	let tile = document.getElementById(tileId);
	tile.className = 'tile ' + currentTurn;
	console.log(tile.className + " placed.");
	changeTurn();
};


function areEqual(){
   var len = arguments.length;
   for (var i = 1; i< len; i++){
      if (arguments[i] === null || arguments[i] !== arguments[i-1])
         return false;
   }
   return true;
}

function checkTurn() {
	console.log("Current turn is: " + currentTurn)
}