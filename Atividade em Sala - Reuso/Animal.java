public class Animal{
    private String nome;
    private String especie;
    private int idade;
    private Dono dono;

    public Animal(){
        setNome("Sem Nome");
        setEspecie("Não informado");
        setIdade(0);
        setDono(null);
    }
    public Animal(String n, String e, int i, Dono d){
        setNome(n);
        setEspecie(e);
        setIdade(i);
        setDono(d);
    }

    public void setNome(String n){
        if (n!=""){
            nome = n;
        }
        else{
            System.out.println("Nome inválido.");
        }
    }
    public void setEspecie(String e){
        especie = e;
    }
    public void setIdade(int i){
        if (i>=0){
            idade = i;
        }
        else{
            System.out.println("Idade inválida.");
            setNome("Sem nome");
        }
    }
    public void setDono(Dono d){
        dono = d;
    }
    

    public String getNome(){
        return nome;
    }
    public String getEspecie(){
        return especie;
    }
    public int getIdade(){
        return idade;
    }
    public Dono getDono(){
        return dono;
    }

    public void ficha(){
        System.out.print("\n====Ficha==== \nNome: " + nome + "\nEspecie: " + especie + "\nIdade: " + idade + "\nDono: ");
        if (dono == null){
            System.out.println("Sem dono");
        }
        else{
            System.out.println(dono.getNome());
        }
    }
}