
public class Iterador<Tipo> {
	
	private NodoLista<Tipo> cabLista;
	private NodoLista<Tipo> actual;
	
	public Iterador(NodoLista<Tipo> c){
		cabLista = c ;
		actual = c ;
	}
	
	public boolean hasNext() {
		return (actual.next != null) 
				//retorna el puntero del siguiente elemento si este es nulo 
	}	

}