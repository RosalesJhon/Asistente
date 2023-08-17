import java.util.Scanner;

public class Prim {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Hola, En qué puedo ayudarte?");
        String userInput;

        do {
            System.out.print("Usuario: ");
            userInput = scanner.nextLine();

            String botResponse = getBotResponse(userInput);
            System.out.println("Bot: " + botResponse);

        } while (!userInput.equalsIgnoreCase("adios"));

        System.out.println("Bot: Hasta luego. ¡Que tengas un buen día!");
    }

    public static String getBotResponse(String input) {
        // Implementa aquí la lógica para generar respuestas del bot
        // Puedes usar condicionales, bases de datos, APIs, etc.

        if (input.contains("hola")) {
            return "¡Hola! ¿Cómo estás?";
        } else if (input.contains("nombre")) {
            return "Soy un bot sin nombre, pero puedes llamarme Bot.";
        } else if (input.contains("clima")) {
            return "Lo siento, no tengo información sobre el clima en este momento.";
        } else {
            return "Lo siento, no entiendo tu pregunta.";
        }
    }
}
