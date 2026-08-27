public class Dono {
    private String nome;
    private int telefone;
    private String endereco;

    public Dono(){
        setNome("Sem Nome");
        setTelefone(0);
        setEndereco("Sem Endereco");
    }
    public Dono(String n, int t, String e){
        setNome(n);
        setTelefone(t);
        setEndereco(e);
    }

    public void setNome(String n){
        if (n!=""){
            nome = n;
        }
        else{
            System.out.println("Nome inválido.");
        }
    }
    public void setTelefone(int t){
        telefone = t;
    }
    public void setEndereco(String e){
        endereco = e;
    }

    public String getNome(){
        return nome;
    }
    public int getTelefone(){
        return telefone;
    }
    public String getEndereco(){
        return endereco;
    }

    public void exibir(){
        System.out.println("\nDados do Dono \nNome: " + nome + "\nTelefone: " + telefone + "\nEndereco: " + endereco);
    }
}
