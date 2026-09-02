import java.util.ArrayList;

public class Personagem{
    private String nome;
    private int vida;
    private int forca;
    private int nivel;
    private ArrayList<Item> inventario = new ArrayList<>();

    public Personagem(){
    }
    public Personagem(String n, int v, int f, int ni){
        setNome(n);
        setVida(v);
        setForca(f);
        setNiveL(ni);
    }

    public String getNome(){
        return nome;
    }
    public int getVida(){
        return vida;
    }
    public int getForca(){
        return this.forca;
    }
    public int getNivel(){
        return nivel;
    }
    public ArrayList<Item> getInventario(){
        return this.inventario;
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
    public void setForca(int f){
        this.forca = f;
    }
    public void setNiveL(int n){
        if (n>=1){
            nivel=n;
        }
        else{
            System.out.println("Nível inválida!");
        }
    }
    public void setInventario(ArrayList<Item> i){
        this.inventario = i;
    }
    public void pegarItem(Item i){
        this.inventario.add(i);
        calcular_forca();
    }
    public void calcular_forca(){
        for (int i=0; i<getInventario().size(); i++){
            setForca(getForca() + getInventario().get(i).getBonus());
        }
    }

    public void receberDano(int d){
        this.vida = this.vida - d;
        if (this.vida<0){
            this.vida=0;
        }
        System.out.println(getNome() + " recebeu " + d + " de dano");
    }
    public void atacar(){
        atacar(10);
    }
    public void atacar(int f){
        System.out.println(nome + " atacou com " + f + " de força");
    }

    public void ficha(){
        System.out.println("\n====FICHA==== \nNome: " + getNome() + "\nVida: " + getVida() + "\nForça: " + getForca() + "\nNivel: " + getNivel() + "\nInventario:");
        if (getInventario().size() == 0){
            System.out.println("Inventario Vazio.");
        }
        else{
            for (int i=0; i<getInventario().size(); i++){
                System.out.println(getInventario().get(0).descricao());
            }
        }
        System.out.println("===========");
    }
}