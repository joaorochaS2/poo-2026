/*
Dominio: PetShop
Classes: 
    Animal:
        -Nome
        -Especie
        -Idade (em anos)
        -Dono
    
    Dono:
        -Nome
        -Telefone
        -Endereço

    Validações:
        1 - Nome (Animal e Dono) não podem ser vázio ""
        2 - Idade (Animal) não pode ser negativa

    Tempo:
        Documentação e leitura: 15 min
        Criação das classes - 25 min
        Criação Main - 5 min
        Execução e testes - 5 min
        Ajustes - 10 min

*/ 

public class Main {
    public static void main(String[] args) {
        //Criação válida
        Dono d1 = new Dono("João", 80228922, "IF Goiano");
        Animal a1 = new Animal("Tedy", "cachorro", 9, d1);

        //Criação recusa
        Animal a2 = new Animal("", "gato", -4, d1); //Nome inválido e Idade inválida

        //Criação sem dados
        Animal a3 = new Animal();

        d1.exibir();
        a1.exibir();
        a2.exibir();
        a3.exibir();
    }
}
/*
Considerações finais

Todos os critérios desejados foram atendidos. Atributos e métodos funcionam como planejado.
Não foi utilizado IA.

Dificuldades: print na classe Animal no método "exibir()", quando o atributo "dono = null" não era possivel usar "dono.getNome" para imprimir o nome do dono.
*/
