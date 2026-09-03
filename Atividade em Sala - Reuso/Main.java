
import java.util.ArrayList;

/*
Dominio: PetShop
Classes: 
    Animal:
        -Nome
        -Especie
        -Idade (em anos)
        -Dono
    
    Pessoa (nome, cpf, telefone) - metedo abstrato (habilidade)
        Dono:
            -Endereço
            =Metodo sobrescrito (ficha)
        Veterinario:
            -CRM
            -especialização
            =Metodo sobrescrito (ficha)

    Validações:
        1 - Nome (Animal e Pessoa) não podem ser vázio ""
        2 - Idade (Animal) não pode ser negativa


*/ 

public class Main{
    public static void main(String[] args) {
        ArrayList<Pessoa> pessoas = new ArrayList<>();
        Dono dono = new Dono("João", "07456", 85564, "IF Goiano");
        pessoas.add(dono);
        pessoas.add(new Veterinario("Cristiano", "154996", 645789, "5478961", "Pediatra"));
        Animal a = new Animal("Ted", "cachorro", 5, dono);

        System.err.println("Animal [" + a.getNome() + "] passou mal.");
        for (Pessoa p : pessoas) {
            p.habilidade();
        }
        a.ficha();
        for (Pessoa p : pessoas) {
            if (p instanceof Dono) {
                Dono d = (Dono)p;
                d.ficha();
            }
            if (p instanceof Veterinario) {
                Veterinario v = (Veterinario)p;
                v.ficha();
            }
        }
}
}
/*
Declarações finais

Todos os critérios desejados foram atendidos. Atributos e métodos funcionam como planejado.
Não foi utilizado IA.

Dificuldades: O tempo. Planejar como cada classe vai funcionar.
*/