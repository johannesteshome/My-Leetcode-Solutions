class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        playerPtr = len(players) - 1
        trainerPtr = len(trainers) - 1
        counter = 0
        
        while playerPtr >= 0 and trainerPtr >= 0:
            # print(playerPtr, trainerPtr, "pointer")
            # print(players[playerPtr], trainers[trainerPtr])
            if players[playerPtr] <= trainers[trainerPtr]:
                counter += 1
                playerPtr -= 1
                trainerPtr -= 1
            else:
                playerPtr -= 1
                
        return counter
                
        