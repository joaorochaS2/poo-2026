public class Chefe extends Personagem{
    
    public Chefe(String nome){
        super(nome, 200, 20, 1);
    }
    @Override
    public String habilidade(){
        return "ataque devastador";
    }
    @Override
    public void ficha(){
        System.out.println("\n[CHEFE] " + getNome() + " (vida: " + getVida() + ",  forca: " + getForca() +")");
    }
}
