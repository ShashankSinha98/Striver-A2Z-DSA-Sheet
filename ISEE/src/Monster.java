public class Monster implements IMonster {

	private final String name;
	private final int maxHealth;
	private final float weight;
	private final int baseAttackValue;
	private float attackMultiplier;
	
	private int currentHealth;
	
	
	public Monster(String name, int maxHealth, float weight, int baseAttackValue, float attackMultiplier) {
		this.name = name;
		this.maxHealth = (maxHealth > 1) ? maxHealth : 1 ;
		this.currentHealth = this.maxHealth;
		this.weight = (weight > 0.1) ? weight : 0.1f;
		this.baseAttackValue = baseAttackValue;
		this.attackMultiplier = validateAttackMultiplier(attackMultiplier);
	}
	
	private float validateAttackMultiplier(float attackMultiplier) {
		if(attackMultiplier < -2.0f) {
			return -2.0f;
		} else if(attackMultiplier > 5.0f) {
			return 5.0f;
		} else return attackMultiplier;
	}
	
	private int validateHealth(int health) {
		if(health < 0) {
			return 0;
		} else if(health > this.maxHealth) {
			return this.maxHealth;
		} else return health;
	}
	
	@Override
	public String getName() {
		return this.name;
	}

	@Override
	public int getHealth() {
		return this.currentHealth;
	}

	@Override
	public int getMaxHealth() {
		return this.maxHealth;
	}

	@Override
	public boolean isAlive() {
		return this.currentHealth > 0;
	}

	@Override
	public void receiveDamage(int damage) {
		if (this.weight > 13.37f) {
			damage = (int) Math.floor(0.8 * damage);
		}
		this.currentHealth = validateHealth(this.currentHealth - damage);
	}

	@Override
	public int getBaseAttack() {
		return this.baseAttackValue;
	}

	@Override
	public int getAttack() {
		return Math.round(this.baseAttackValue * this.attackMultiplier);
	}

	@Override
	public float getWeight() {
		return this.weight;
	}

	@Override
	public void setAttackMultiplier(float multiplier) {
		this.attackMultiplier = validateAttackMultiplier(multiplier);
	}
  }