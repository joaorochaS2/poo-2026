public class Main{
    public static void main(String[] args) {
        Item item = new Item("Espada de Aço", 3);

        Mago m = new Mago("Elara", 65, 15, 4);
        m.pegarItem(item);
        m.ficha();

        Guerreiro g = new Guerreiro("Bran", 100, 5, 3);
        g.receberDano(8);
        g.ficha();

        m.setMana(-10);
    }
}