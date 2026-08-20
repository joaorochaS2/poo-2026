public class Personagem{
    private String nome;
    private int vida;
    private int nivel;

    public String getNome(){
        return nome;
    }
    public int getVida(){
        return vida;
    }
    public int getNivel(){
        return nivel;
    }
    public void setNome(String n){
        if (n!=null){
            nome = n;
        }
        else{
            System.out.println("Nome inválido!");
        }
    }
    public void setVida(int v){
        if (v>=0 && v<=100){
            vida=v;
        }
        else{
            System.out.println("Vida inválida!");
        }
    }
    public void setNiveL(int n){
        if (n>=1){
            nivel=n;
        }
        else{
            System.out.println("Nível inválida!");
        }
    }
}
