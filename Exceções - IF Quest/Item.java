public class Item {
    private String nome="Sem nome";
    private int bonus;

    public Item(){

    }
    public Item(String n, int b){
        setNome(n);
        setBonus(b);
    }

    public String getNome(){
        return this.nome;
    }
    public int getBonus(){
        return this.bonus;
    }
    public void setNome(String n){
        this.nome = n;
    }
    public void setBonus(int b){
        if (b>=0){
            this.bonus = b;
        }
        else{
            throw new IllegalArgumentException("Bonus inválido, digite um valor maior que 0");
        }
    }

    public String descricao(){
        return getNome() + " (+" + getBonus() + ")";
    }
}