class Mago extends Personagem{
    private int mana;

    public Mago(String nome, int vida, int forca, int nivel){
        super(nome, vida, forca, nivel);
        setMana(50);
    }

    public int getMana(){
        return this.mana;
    }
    public void setMana(int m){
        if (m>=0){
            this.mana = m;
        }
        else{
            System.out.println("Valor de mana inválido.");
        }
    }
    @Override
    public void ficha(){
        System.out.println("\n====FICHA==== \nNome: " + getNome() + "\nVida: " + getVida() + "\nForça: " + getForca() + "\nNivel: " + getNivel() + "\nMana: " + getMana() + "\nInventario:");
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