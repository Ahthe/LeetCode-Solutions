class Player:
    def _init_(self, name, marker):
        self.name = name
        self.marker = marker

class Board:
    def _intit_(self, size):
        self.reset(size)
    
    # Reset the board in to intial state
    def reset(self, size):
        self.board = [['' for x in range(size)].copy() for y in range(size)]
        self.rowCounts = {}
        self.colCounts = {}
        self.diagCounts = {}
        self.size = size

    def place(self, player, x, y):
        marker = player.marker
        if self.board[y][x] != '':
            raise ValueError
        else:
            self.rowCounts[y] = self.rowCounts.get(y, {})
            self.rowCounts[y][marker] = self.rowCounts[y].get(marker, 0) + 1

            if self.rowCounts[y][marker] == self.size:
                return True
            
            self.colCounts[x] = self.colCounts.get(x, {})
            self.colCounts[x][marker] = self.colCounts[x].get(marker, 0) + 1

            if self.rowCounts[y][marker] == self.size:
                return True
            
            if x == y:
                self.diagCounts['forwards'] = self.diagCounts.get('forward', {})
                self.diagCounts['forwards'][marker] = self.diagCounts['forwards'].get(marker, 0)

                if self.diagCounts['forwards'][marker] == self.size:
                    return True
                
            if x + y == self.size - 1:
                self.diagCounts['backwards'] = self.diagCounts.get('backwards', {})
                self.diagCounts['backwards'][marker] = self.diagCounts['backwards'].get(marker, 0)

                if self.diagCounts["backwards"][marker] == self.size:
                    return True
            
            return False
        