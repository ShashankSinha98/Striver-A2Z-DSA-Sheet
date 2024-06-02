/* class Monster
 * author: Thomas Wilde
 * This file is for private use only.
 */

 import java.io.IOException;
 import java.nio.file.Files;
 import java.nio.file.Paths;
 import java.util.ArrayList;
 import java.util.List;
 
 public class MonsterLoader {
   // --------------------------------------------------------------- //
   /* hide constructor */
   private MonsterLoader() {}
 
   // --------------------------------------------------------------- //
   private static boolean loadMonster(List<String> data, int index,
                                      List<Monster> monsters) {
     String name = "";
     int maxHP = 0;
     int attack = 0;
     float weight = 0.0f;
     float multi = 1.0f;
 
     // --- load name
     String[] name_line = data.get(index + 1).split(" ");
     if (name_line[0].compareTo("name") != 0)
       return false;
     name = data.get(index + 1).substring(4);
     name = name.trim();
 
     // --- load maxHP
     String[] hp_line = data.get(index + 2).split(" ");
     if (hp_line[0].compareTo("maxHP") != 0)
       return false;
     maxHP = Integer.parseInt(hp_line[1]);
 
     // --- load attack
     String[] atk_line = data.get(index + 3).split(" ");
     if (atk_line[0].compareTo("attack") != 0)
       return false;
     attack = Integer.parseInt(atk_line[1]);
 
     // --- load weight
     String[] weight_line = data.get(index + 4).split(" ");
     if (weight_line[0].compareTo("weight") != 0)
       return false;
     weight = Float.parseFloat(weight_line[1]);
 
     // --- load multiplier
     String[] multi_line = data.get(index + 5).split(" ");
     if (multi_line[0].compareTo("multi") != 0)
       return false;
     multi = Float.parseFloat(multi_line[1]);
 
     // --- create monster
     Monster mon = new Monster(name, maxHP, weight, attack, multi);
     monsters.add(mon);
     return true;
   }
 
   // --------------------------------------------------------------- //
   /**
    * Load the monsters from the given file. If something is wrong with a
    * monster, it is not loaded. The loading process continues with the next
    * monster.
    *
    * \return true, if at lest one monster was loaded
    */
   public static boolean loadMonsterFile(String file_path,
                                         List<Monster> monsters) {
     try {
       List<String> data = Files.readAllLines(Paths.get(file_path));
       // --- search monster
       int line_idx = 0;
       for (String line : data) {
         String[] content = line.split(" ");
         // --- check for blank line
         if (content.length == 0)
           continue;
         // --- check for monster and load it
         if (content[0].equals("Monster"))
           try {
             if (loadMonster(data, line_idx, monsters))
               System.out.println("load monster");
             else
               System.out.println("load monster failed");
           } catch (Exception e) {
             System.out.println("load monster threw exception");
           }
         ++line_idx;
       }
     } catch (IOException e) {
       e.printStackTrace();
     }
     return monsters.size() > 0;
   }
 }
 