const util = require('util');
const data = require('./data.json');

const flights = data.reduce((all,curr) => ({...all, [curr.origin]: all[curr.origin] ? [...all[curr.origin], curr]: [curr]}), {});
const backFlights = flights.LHR.reduce((all,curr) => ({...all, [curr.destination]: all[curr.destination] ? [...all[curr.destination], curr]: [curr]}), {});

// Remove unwated destination
delete flights.LHR;
delete flights.SXF;
delete backFlights.LHR;

const solutions = generateRandomSolution();

console.log(util.inspect(solutions, false, 2, true));
solutions.sort((a, b) => a.cost - b.cost);
console.log(util.inspect(solutions[0], false, 1, true));

function generateRandomSolution() {
	const nbSol = 1000;
	const solutions = [];

	for (let i = 0; i < nbSol; i++) {
		const sol = [];
		Object.keys(flights).forEach(key => {
			element = flights[key];
			if(element === undefined) return;

			const indexAll = Math.floor(Math.random() * (element.length - 2));
			const indexRet = Math.floor(Math.random() * (backFlights[key].length - 2));
			sol.push([element[indexAll], backFlights[key][indexRet]]);
		});
		
		solutions.push({
			cost : cost(sol),
			flights: sol
		});
	}

	return solutions;
}

function cost(solution) {
	var cost = 0;

	solution.forEach(f => {
		cost += f.reduce((accumulator, object) => {
			return accumulator + object.price;
		  }, 0);
	});

	return cost;
}