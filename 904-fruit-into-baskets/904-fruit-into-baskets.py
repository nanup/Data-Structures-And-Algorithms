class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitDict = {}
        numOfFruits = 0
        startTree = 0
        
        for endTree in range(len(fruits)):
          fruit = fruits[endTree]
          
          fruitDict[fruit] = fruitDict.get(fruit, 0) + 1
          
          while len(fruitDict) > 2:
            fruitToRemove = fruits[startTree]
            fruitDict[fruitToRemove] -= 1
            startTree += 1
            
            if fruitDict[fruitToRemove] == 0:
              del fruitDict[fruitToRemove]
              
          numOfFruits = max(numOfFruits, endTree - startTree + 1)
          
        return numOfFruits