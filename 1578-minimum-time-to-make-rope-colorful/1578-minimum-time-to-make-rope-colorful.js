/**
 * @param {string} colors
 * @param {number[]} neededTime
 * @return {number}
 */
var minCost = function(colors, neededTime) {
    
    let cost = 0 ;
    
    for(let i=0;i<colors.length;i++){
        if(colors[i] != colors[i+1]) continue;
        else {
            if (neededTime[i] < neededTime[i+1]) cost += neededTime[i];
            else{
                cost += neededTime[i+1];
    var t = neededTime[i];
    neededTime[i] = neededTime[i+1];
    neededTime[i+1] = t;
 


            }
        }
    }
    return cost;
    
};