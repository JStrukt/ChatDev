'''
This class represents a character from the Simpsons. It has attributes for the character's name, health, happiness, hunger, and cleanliness. It also has methods to feed, play with, and clean the character. Additionally, it checks if the character's condition has reached a critical level.
'''
public class Character {
    private String name;
    private int health;
    private int happiness;
    private int hunger;
    private int cleanliness;
    public Character(String name) {
        this.name = name;
        this.health = 100;
        this.happiness = 100;
        this.hunger = 0;
        this.cleanliness = 100;
    }
    public void feed() {
        this.hunger = Math.max(0, this.hunger - 10);
        this.health = Math.min(100, this.health + 5);
    }
    public void play() {
        this.happiness = Math.min(100, this.happiness + 10);
        this.health = Math.max(0, this.health - 5);
        this.hunger = Math.min(100, this.hunger + 10);
        this.cleanliness = Math.max(0, this.cleanliness - 10);
    }
    public void clean() {
        this.cleanliness = Math.min(100, this.cleanliness + 10);
        this.health = Math.min(100, this.health + 5);
    }
    public boolean isCritical() {
        return health <= 0 || happiness <= 0 || hunger >= 100 || cleanliness <= 0;
    }
}
