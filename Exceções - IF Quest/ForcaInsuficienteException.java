public class ForcaInsuficienteException extends Exception{

    public ForcaInsuficienteException(int forca){
        super("força insuficiente: "
            + forca);
    }
}
