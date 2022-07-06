# AlgoRecomandation
### Abdel Rahim DEBECHE
https://github.com/Rimsoo/AlgoRecomandation/

Usage :  
```  
git clone git@github.com:Rimsoo/AlgoRecomandation.git  
cd AlgoRecomandation  
npm i  
node index.js  
```  

To change the number of the generated solution, edit the variable `nbSol` in the function `generateRandomSolution` :  

```
function generateRandomSolution() {
	const nbSol = 1000;
...
```
Change the int value in the console log to show more details :  
``` 
//----------------------------------->here |
console.log(util.inspect(solutions, false, 2, true));
solutions.sort((a, b) => a.cost - b.cost);
//-------------------------------------->here |
console.log(util.inspect(solutions[0], false, 1, true));
