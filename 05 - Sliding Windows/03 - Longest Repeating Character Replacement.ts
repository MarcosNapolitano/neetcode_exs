function characterReplacement(s: string, k: number): number{
    
    let index: Map<string, number> = new Map()
    let low: number = 0
    let high: number = 0
    let mostFrequent: number = 0
    let result: number = 0

    while (low<s.length){

        if(!index.get(s[high]))index.set(s[high], 1)


        for (const element of index) {
            mostFrequent = Math.max(element[1], mostFrequent)
        }   
        
        if((high-low)+1-mostFrequent<=k) {
            result = Math.max(result, (high-low)+1)//convert from index to value
                        
            if(high==s.length-1){
                if((high-low)<result) break
                else low++
            }
            else {
                high++
                index.set(s[high], index.get(s[high])+1)
            }
        }
        else{
         index.set(s[low], index.get(s[low])-1)
         low++
        }

    }



    return result
};
