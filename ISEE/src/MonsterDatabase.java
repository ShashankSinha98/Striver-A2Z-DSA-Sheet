import java.util.ArrayList;
import java.util.Iterator;

public class MonsterDatabase implements Iterable<Monster> {
  // --- atributes
  private ArrayList<Monster> monsters = new ArrayList<>();

  // --------------------------------------------------------------- //
  /**
   * Load a file that contains monster data.
   * @return true, if the loading process was successful.
   */
  public boolean initDatabase(String file_path) {
    monsters.clear();
    return MonsterLoader.loadMonsterFile(file_path, monsters);
  }

  // --------------------------------------------------------------- //
  /**
   * Access the monster via an index.
   *
   * @param idx - 0-based index of the monster
   * @return A reference to the monster or null if that index does not exist.
   */
  public Monster getMonster(int idx) {
    if (idx < 0 || idx >= monsters.size())
      return null;
    return monsters.get(idx);
  }

  // --------------------------------------------------------------- //
  /**
   * Return the number of existing monsters.
   */
  public int getCount() { return monsters.size(); }

  // --------------------------------------------------------------- //
  public Iterator<Monster> iterator() { return this.monsters.iterator(); }
}
