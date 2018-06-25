
public class Main {

	public static void main(String[] args) {
		// se definen las Listas
		Lista<String> listaA  = new Lista<String>();
		Lista<String> listaB  = new Lista<String>();
		
		listaA.insert("taza");
		listaA.insert("libro");
		listaA.insert("computadora");
		listaA.insert("casa");
		
		listaB.insert("papel");
		listaB.insert("taza");
		listaB.insert("pelota");
		listaB.insert("casa");
		listaB.insert("libro");
		listaB.insert("telefono");
		
		System.out.print("\n Contenido de la lista A: {");
		Iterador<String> it = listaA.getIterador();
		while (it.hasNext()) {
			String val = it.next();
			System.out.println(val + " ");
		}
		System.out.print("}\n");
		
		System.out.println("\nContenido de la Lisa B:");
		Iterador<String> itB = listaB.getIterador();
		while (itB.hasNext()){
			String val = itB.next();
			System.out.println(val + " ");
		}
		System.out.println("}\n");
		
		Lista<String> listaC = new Lista<String>();
		it = listaA.getIterador();
		while (it.hasNext()){
			String X = it.next();
			if(listaB.search(X) > 0){
				listaC.insert(X);
			}
		}
		System.out.println("\nContenido de la Lisa C:");
		Iterador<String> itC = listaC.getIterador();
		while (itC.hasNext()){
			String val = itC.next();
			System.out.println(val + " ");
		}
		System.out.println("}\n");
	}

}
