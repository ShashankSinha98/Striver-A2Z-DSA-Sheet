/* class Monster
 * author: Thomas Wilde
 * This file is for private use only.
 */

 public class Monster implements IMonster {
    // --- final members
    private final String name;
    private final int max_health;
    private final float weight;
    // ---
    private int health = 0;
    private int base_atk = 0;
    private float atk_multplier = 1.0f;
  
    // --------------------------------------------------------------- //
    public Monster(String name, int max_health, float weight, int base_atck,
                   float multiplier) {
      // --- init final members
      this.name = name;
      this.max_health = Math.max(1, max_health);
      this.weight = Math.max(0.1f, weight);
      // --- init other members
      this.health = this.max_health;
      this.base_atk = base_atck;
      this.atk_multplier = multiplier;
      capMultiplier();
    }
  
    // --------------------------------------------------------------- //
    private void capMultiplier() {
      if (atk_multplier < -2.0f)
        atk_multplier = -2.0f;
      if (atk_multplier > 5.0f)
        atk_multplier = 5.0f;
    }
  
    private void clipHealth() {
      if (health < 0)
        health = 0;
      if (health > max_health)
        health = max_health;
    }
  
    // --------------------------------------------------------------- //
    @Override
    public String getName() {
      return name;
    }
  
    @Override
    public int getHealth() {
      return health;
    }
  
    @Override
    public int getMaxHealth() {
      return max_health;
    }
  
    @Override
    public boolean isAlive() {
      return health > 0;
    }
  
    @Override
    public void receiveDamage(int damage) {
      // ---
      if (weight > 13.37f) {
        int reduction = (int)(damage * 0.2);
        damage -= reduction;
      }
      health -= damage;
      clipHealth();
    }
  
    @Override
    public int getBaseAttack() {
      return base_atk;
    }
  
    @Override
    public int getAttack() {
      return (int)(base_atk * atk_multplier);
    }
  
    @Override
    public float getWeight() {
      return weight;
    }
  
    @Override
    public void setAttackMultiplier(float multiplier) {
      atk_multplier = multiplier;
      capMultiplier();
    }
  
    @Override
    public String toString() {
      StringBuilder data = new StringBuilder();
      data.append("Name:   ").append(name).append("\n");
      data.append("maxHP:  ").append(max_health).append("\n");
      data.append("HP:     ").append(health).append("\n");
      data.append("attack: ").append(base_atk).append("\n");
      data.append("weight: ").append(weight).append("\n");
      data.append("multi:  ").append(atk_multplier).append("\n");
      return data.toString();
    }
  }
  