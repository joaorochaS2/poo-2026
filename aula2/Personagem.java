public class Personagem{
    String nome;
    int vida;
    int forca;
    
    public void receberDano(int dano) {
        vida = vida - dano;
        System.out.println(nome + " sofreu " + dano + " de dano");
        if (vida<0){
            vida=0;
        }
    }
    public boolean estaVivo(){
        if (vida>0){
            return true;
        }
        else{
            return false;
        }
    }
    public void ficha(){
        System.out.println("\nNome: " + nome);
        System.out.println("Vida: " + vida);
        System.out.println("Força: " + forca);
    }
    public void atacar(Personagem alvo){
        System.out.println(nome + " ataca " + alvo.nome);
        alvo.receberDano(forca);
        
    }
}

public class Main{
    public static void main(String[] args){
        Personagem jogador = new Personagem();
        jogador.nome = "Raquel";
        jogador.vida = 100;
        jogador.forca = 10;
        
        Personagem chefe = new Personagem();
        chefe.nome = "Barbie";
        chefe.vida = 500;
        chefe.forca = 40;
        
        System.out.println("\n===Ficha===");
        jogador.ficha();
        chefe.ficha();
        System.out.println("\n===Batalha===");
        while(jogador.estaVivo() && chefe.estaVivo()){
            jogador.atacar(chefe);
            
            if (! chefe.estaVivo()){
                System.out.println(chefe.nome + " derrotado.");
                break;
            }
            chefe.atacar(jogador);

            if (! jogador.estaVivo()){
                System.out.println("\n" + jogador.nome + " derrotado!!!");
                break;
            }
        }
        System.out.println("\n===Ficha===");
        jogador.ficha();
        chefe.ficha();
    }
}
