public class Personagem{
    private String nome;
    private int vida;
    private int nivel;

    public Personagem(){
    }
    public Personagem(String n, int v, int ni){
        setNome(n);
        setVida(v);
        setNiveL(ni);
    }

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

    public void atacar(){
        atacar(10);
    }
    public void atacar(int f){
        System.out.println(nome + " atacou com " + f + " de força");
    }

    public static void main(String[] args) {
        Personagem p1 = new Personagem();
        p1.setNome("Raquel");
        p1.setVida(50);
        p1.setNiveL(1);
        Personagem p2 = new Personagem("Barbie", 100, 40);

        p1.atacar();
        p2.atacar(40);
    }
}
