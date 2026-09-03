import java.util.ArrayList;

public class Main{

    public static void main(String[] args) {

        ArrayList<Personagem> herois = new ArrayList<>();
        herois.add(new Mago("Elara", 60, 5, 1));
        herois.add(new Guerreiro("Bran", 100, 3, 1));

        Chefe chefe = new Chefe("Rei Julian");

        for (Personagem p : herois){
            p.ficha();
            System.out.println("\n" + p.getNome() + " usou " + p.habilidade());
            p.atacar(chefe);
        }
        chefe.ficha();
        for (Personagem p : herois){
            if (p instanceof Mago) {
                Mago m = (Mago)p;
                System.out.println("\n" + m.getNome() + " tem " + m.getMana() + " de mana");
                
            }
        }
        if (chefe.getVida()>0){
            System.out.println("\nChefe [" + chefe.getNome() + "] não foi derrotado.");
        }
    }
}