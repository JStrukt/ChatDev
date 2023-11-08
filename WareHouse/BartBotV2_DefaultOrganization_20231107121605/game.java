'''
This class represents the game itself. It has methods to start the game, choose a character, and perform actions on the character. It also checks if the game should end after each action.
'''
public class Game {
    private Character character;
    public void start() {
        System.out.println("Welcome to the Simpsons Tamagotchi Game!");
        System.out.println("Please choose your character: Bart, Lisa, Maggie, Homer or Marge");
    }
    public void chooseCharacter(String name) {
        this.character = new Character(name);
        System.out.println("You have chosen " + name + " as your pet.");
    }
    public void performAction(String action) {
        if (action.equals("feed")) {
            this.character.feed();
        } else if (action.equals("play")) {
            this.character.play();
        } else if (action.equals("clean")) {
            this.character.clean();
        }
        if (this.character.isCritical()) {
            System.out.println("Game Over. Your character's condition has reached a critical level.");
            System.exit(0);
        }
    }
}
