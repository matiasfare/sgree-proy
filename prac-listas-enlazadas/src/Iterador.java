
public class Iterador<Tipo> {
	
	private NodoLista<Tipo> actual;
	
	public Iterador(NodoLista<Tipo> c){
		actual = c ;
	}
	
	public boolean hasNext() {
		return (actual.next != null); 
				//retorna el puntero del siguiente elemento si este es nulo 
	}
	
	public Tipo next() {
		actual = actual.next;
		return actual.dato;
	}
}