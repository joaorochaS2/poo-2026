import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JPanel;
import java.awt.BorderLayout;
import java.awt.GridLayout;

public class TelaCriacaoHeroi extends JFrame {

    private JTextField campoNome;
    private JTextField campoVida;
    private JTextField campoForça;
    private JButton botaoCriar;

    public TelaCriacaoHeroi() {
        super("IF Quest");

        setSize(600, 250);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        JLabel titulo = new JLabel(
            "Criação de Herói",
            JLabel.CENTER
        );

        add(titulo, BorderLayout.NORTH);

        JPanel painel = new JPanel(
            new GridLayout(3, 2, 5, 5)
        );

        JLabel rotuloNome = new JLabel("Nome:");
        campoNome = new JTextField(5);

        JLabel rotuloVida = new JLabel("Vida:");
        campoVida = new JTextField(5);

        JLabel rotuloForça = new JLabel("Força:");
        campoForça = new JTextField(15);

        painel.add(rotuloNome);
        painel.add(campoNome);
        painel.add(rotuloVida);
        painel.add(campoVida);
        painel.add(rotuloForça);
        painel.add(campoForça);

        add(painel, BorderLayout.CENTER);

        botaoCriar = new JButton("Criar Herói");
        botaoCriar.setEnabled(false);

        add(botaoCriar, BorderLayout.SOUTH);

        titulo.setText("Criação de Herói - IF Quest");
    }

    public static void main(String[] args) {
        TelaCriacaoHeroi tela = new TelaCriacaoHeroi();
        tela.setVisible(true);
    }
}