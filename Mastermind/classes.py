# --- MASTERMIND --- #
import random



class Mastermind():
    colors = ["R", "G", "B", "O", "W", "P", "L", "S", "K", "V"]
    trys = 0
    game = True
    color_number = 4
    color_code = []
    max_retries = 5    
    name = ""
    correct_color = []
    
    def start (self):
        print ("\n ------- MASTERMIND ------- \n")
        self.name=input("Willkommen bei Mastermind. Gib bitte deinen Namen ein:")
        self.ask_for_name()
        self.print_rules(self.color_number)
        self.new_game(self.colors)
        
        while self.game:
            player_guess = input().upper()
            
            if self.is_guess_valid(player_guess) is False:
                continue
            
            right_answer = self.check_guess(player_guess)
            
            if self.is_answer_correct(right_answer)  is "correct":
                self.congratulate(self.trys)
                self.game = False
                
            else: 
                print(right_answer)
                if self.next_round() is True:
                    self.game = False
             
                
            while self.game is False:
                finish_game = input("\nMöchtest du nochmal spielen? J oder N\n").upper()
                if self.retry_or_exit(finish_game) is False:
                    exit()
    
    
    def ask_for_name(self):
        print("Hey "+ self.name +"! Freut mich, dass du hier bist.")
          
    def print_rules(self,color_number):
        print ("Rate die geheimen Farben.")
        if color_number == 1:
            print ("Du kannst nur", color_number ,"Farbe auswählen")
        else:
            print ("Du kannst nur die folgenden", color_number ,"Farben auswählen:")
        print ("rot(R), grün(G), blau(B), orange(O), weiß(W), pink(P), lila(L), silber(S), kupfer(K), violett(V)")

         
    def new_game(self, colors):
        self.trys = 0
        self.game = True
        self.color_code = random.sample(colors,self.color_number)
        print (self.color_code)
        return self.color_code
        
         
    def is_guess_valid (self, player_guess):
        if len(player_guess) != len(self.color_code):
            print ("\nDu kannst" ,self.color_number, "Farben wählen. Versuche nochmal!")
            return False
         
        for guessed_color in player_guess:
            if guessed_color not in self.colors:
                print("\nSchaue bitte nach, welche Farben du wählen kannst.")
                return False
            
        return True
         
    def check_guess (self, player_guess):
        correct_color = ""
        guessed_color = ""
        for i in range(self.color_number):
            if player_guess[i] == self.color_code[i]:
                correct_color += "+"
            else:
                guessed_color += "-"
                
        return guessed_color + correct_color
            
       
    def is_answer_correct(self, right_answer):
        if right_answer == self.color_number * "+":
            return "correct"
         
        return "incorrect"

                     
    def next_round (self):
        self.trys += 1
        if self.trys <self.max_retries:
            print ("Nächster Versuch: ")
            return False
        else:
            print ("\nDu hast leider verloren. Die Farben waren: \n" +str(self.color_code))
            return True
             
        
             
    def congratulate (self,trys):
        if trys == 0:
            print ("Glückwunsch! Du hast es beim ersten Mal geschafft!")
            return True
        elif trys == 1:
            print ("Gut! Du hast  " +str(trys)+ " Versuch gebraucht, um es zu raten.")
            return False   
        else:
            print ("Du könntest dich auf jeden Fall verbessern! Du hast  " +str(trys)+ " Versuche gebraucht, um es zu raten.")
            return False   
        

                     
    def retry_or_exit(self, finish_game):
        if finish_game =="N":
            print ("\nDanke dir " +self.name+ " fürs Spielen! Auf Wiedersehen!\n")
            return False
                    
        elif finish_game =="J":
            print ("Also lass uns noch eine Runde spielen. Rate die geheimen Farben: ")
            self.new_game(self.colors),
            return True