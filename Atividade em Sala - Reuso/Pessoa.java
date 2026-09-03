public abstract  class Pessoa {
    private String nome;
    private String cpf;
    private int telefone;

    public Pessoa(String nome, String cpf, int telefone){
        setNome(nome);
        setCpf(cpf);
        setTelefone(telefone);
    }
    public abstract void habilidade();
    public void setNome(String n){
        if (n!=""){
            nome = n;
        }
        else{
            System.out.println("Nome inválido.");
        }
    }
    public void setCpf(String cpf){
        this.cpf = cpf;
    }
    public void setTelefone(int t){
        this.telefone = t;
    }
    public String getNome(){
        return this.nome;
    }
    public int getTelefone(){
        return this.telefone;
    }
    public String getCpf(){
        return this.cpf;
    }
    public void ficha(){
        System.out.println("\n====Ficha====\nNome: " + getNome() + " \nCPF: " + getCpf() + "\nTelefone: " + getTelefone());
    }
}
