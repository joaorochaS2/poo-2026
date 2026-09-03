class Guerreiro extends Personagem{
    private int defesa;

    public Guerreiro(String nome, int vida, int forca, int nivel){
        super(nome, vida, forca, nivel);
        setDefesa(5);
    }

    public int getDefesa(){
        return this.defesa;
    }
    public void setDefesa(int d){
        if (d>=0){
            this.defesa = d;
        }
    }

    @Override
    public void receberDano(int dano){
        int dano_efetivo = dano - getDefesa();
        if (dano_efetivo<0){
            dano_efetivo = 0;
        }
        setVida(getVida() - dano_efetivo);
        System.out.println(getNome() + " recebeu " + dano_efetivo + " de dano");
    }
    @Override
    public void ficha(){
        System.out.println("\n====FICHA==== \nNome: " + getNome() + "\nVida: " + getVida() + "\nForça: " + getForca() + "\nNivel: " + getNivel() + "\nDefesa: " + getDefesa() + "\nInventario:");
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
    @Override
    public String habilidade(){
        return "escudo de aço";
    }
}