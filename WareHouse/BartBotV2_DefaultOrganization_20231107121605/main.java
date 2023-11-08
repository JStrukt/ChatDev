'''
This class is the entry point of the application. It creates an instance of the Game class and starts the game. It now includes user interaction, allowing the user to choose a character and perform actions. It also breaks the infinite loop when the game ends.
'''
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Game game = new Game();
        game.start();
        Scanner scanner = new Scanner(System.in);
        String characterName = scanner.nextLine();
        game.chooseCharacter(characterName);
        while (true) {
            String action = scanner.nextLine();
            game.performAction(action);
            if (game.character.isCritical()) {
                break;
            }
        }
    }
}
