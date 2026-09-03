public class Dono extends Pessoa {
    private String endereco;

    public Dono(String n, String c, int t, String e){
        super(n, c, t);
        setEndereco(e);
    }

    public void setEndereco(String e){
        this.endereco = e;
    }

    public String getEndereco(){
        return this.endereco;
    }

    @Override
    public void ficha(){
        System.out.println("\n====Ficha====\nNome: " + getNome() + " \nCPF: " + getCpf() + "\nTelefone: " + getTelefone() + "\nEndereço: " + getEndereco());
    }
    public void habilidade(){
        System.out.println("O Dono [" + getNome() + "] levou o animal ao veterinario.");
    }
}
