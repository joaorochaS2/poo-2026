import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);


        ArrayList<Personagem> herois = new ArrayList<>();
        Mago h1=null; 
        Guerreiro h2=null;
        Chefe chefe=null;
        herois.add(new Mago("Elara", 60, 5, 1));
        herois.add(new Mago("Elsa", 700, 3, 1));
        while (true) { System.out.println("\n=== ESCOLHA SEU HERÓI ==="); 
        for (int i = 0; i < herois.size(); i++) { 
            System.out.println(i + " - " + herois.get(i).getNome()); 
        } 
        System.out.print("Digite o número do herói: "); 
        try {
            int q = scanner.nextInt();
            Personagem h = herois.get(q); 
            System.out.println("Herói escolhido: " + h.getNome()); break; 
        } 
        catch (NumberFormatException e) { System.out.println("digite um número!"); 
        } 
        catch (IndexOutOfBoundsException e) { System.out.println("Esse herói não existe!"); 

        } 
    }

        try {

            h1 = new Mago("Elara", 60, 5, 1);
            System.out.println(h1.getNome() + " Personagem criado!");

            h2 = new Guerreiro("Bran", 100, 4, 1);
            System.out.println(h2.getNome() + " Personagem criado!");

            chefe = new Chefe("Rei Julian");
            System.out.println("Chefe criado!");

            Personagem h3 = new Mago("Merida", -60, 5, 1);
            System.out.println("Personagem criado!");

        } catch (IllegalArgumentException e) {

            System.out.println("Erro ao criar personagem!");
            System.out.println(e.getMessage());
        }

        try {

            System.out.println("\nBatalha!!!");

            for (int i = 0; i <= 5; i++) {

                h1.habilidade();
                h1.atacar(chefe);
            }

        } catch (SemManaException e) {
            try{
                System.out.println(e.getMessage());
            System.out.println("O Mago perde o turno, e o Guerreiro ataca no lugar dele");
            h2.habilidade();
            h2.atacar(chefe);
            }
            catch (ForcaInsuficienteException i){
            System.out.println(i.getMessage());
            System.out.println("Ninguem pode batalhar.");
        }
        }
        finally{
            System.out.println("\nFim do turno!\n");
        }

    }
}