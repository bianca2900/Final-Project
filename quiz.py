
class Quiz: 
    def __init__(self):
        self.italian = {
            'yes': 0,
            'no': 0 
        }  

    def add_point(self, catagory: str) -> None: 
        if category == 'yes':
            self.italian["yes"] = self.italian.get('yes') + 1
        if category == 'no':
            self.italian["no"] = self.italian.get('no') + 1

    def score(self) -> str: 
        greatest = 0 
        result = '' 
        for italian, points in self.italians.items():
            if points > greatest: 
                result = italian  
                greatetst = points

        return result 