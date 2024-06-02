
public class ConsoleVisualizer {

	public void visualize(Object obj) {
		if(obj instanceof Monster) {
			
			Monster monster = (Monster) obj;
			System.out.println(monster.getName());

		}
	}
}

interface IMonster {
    /** Return the name of the Monster */
    public String getName();
  
    /** Return the current health points; returnd value is positive or 0. */
    public int getHealth();
  
    /** Access the maximum value for health points. Value must be bigger than 0. */
    public int getMaxHealth();
  
    /** Return true if the number of health points is bigger than 0. */
    public boolean isAlive();
  
    /** Remove the damage from health points. */
    public void receiveDamage(int damage);
  
    /** Access the base attack. */
    public int getBaseAttack();
  
    /** Access the attack value. */
    public int getAttack();
  
    /** Access the weight in kg. */
    public float getWeight();
  
    /** Set the scale factor for the attack value. */
    public void setAttackMultiplier(float multiplier);
  }
  
