public class Veterinario extends Pessoa {
    private String crm;
    private String especializacao;
    
    public Veterinario(String n, String c, int t, String crm, String es){
        super(n, c, t);
        setCrm(crm);
        setEspecializacao(es);
    }
    public void setCrm(String c){
        this.crm = c;
    }
    public void setEspecializacao(String es){
        this.especializacao = es;
    }
    public String getCrm(){
        return this.crm;
    }
    public String getEspecializacao(){
        return this.especializacao;
    }
    @Override
    public void ficha(){
        System.out.println("\n====Ficha====\nNome: " + getNome() + " \nCPF: " + getCpf() + "\nTelefone: " + getTelefone() + "\nCRM: " + getCrm() + "\nEspecialização: " + getEspecializacao());
    }
    public void habilidade(){
        System.out.println("O Veterinario [" + getNome() + "] avaliou o paciente.");
    }
}
