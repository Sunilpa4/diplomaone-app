"""DI04000021 Unit 5 extras: syntax sheet, viva, exam questions."""
from java_content import SXE, VE, XE, G

SYNTAX = [
    G("Java 7+ features", [
        SXE("try-with-resources", """try (Scanner sc =
    new Scanner(line)) {
  use(sc);
}   // sc.close() automatic""",
            "resource in the try header - self-closing"),
        SXE("switch on String + diamond", """switch (day) {
  case "Monday": return "fresh";
}
ArrayList<String> l =
    new ArrayList<>();""",
            "Java 7: String cases; <> reads the left side"),
        SXE("var (Java 10)", """var name = "Suresh";   // String
var list = new ArrayList<String>();
for (var i = 0; i < n; i++) { }
// locals only, init required""",
            "javac infers local types from the value"),
    ]),
    G("Lambdas", [
        SXE("lambda shapes", """() -> 42                 // no params
n -> n * n              // one param
(x, y) -> x + y         // two params
n -> { int s = n*n; return s; }""",
            "(params) -> body; braces for many lines"),
        SXE("functional interface", """@FunctionalInterface
interface Calc {
  int op(int x, int y);
}
Calc add = (x, y) -> x + y;""",
            "exactly ONE abstract method = lambda target"),
        SXE("forEach with lambda", """team.forEach(t ->
    System.out.println(t));
team.forEach(t -> {
  String u = t.toUpperCase();
  System.out.println(u);
});""",
            "Collections.visit-all, lambda style"),
    ]),
    G("Streams", [
        SXE("filter + forEach (P15a)", """nums.stream()
    .filter(n -> n % 2 == 0)
    .forEach(n ->
        System.out.println(n));""",
            "keep evens, print each - list untouched"),
        SXE("map + forEach (P15b)", """langs.stream()
    .map(s -> s.toUpperCase())
    .forEach(s ->
        System.out.println(s));""",
            "transform each, print - source unchanged"),
        SXE("full pipeline", """marks.stream()
    .filter(m -> m >= 50)
    .sorted()
    .map(m -> "pass: " + m)
    .collect(Collectors.toList());""",
            "source -> ops -> terminal collect/count"),
    ]),
]

_VIVA = [
    VE("What new features did Java 7 introduce?", "try-with-resources, strings in switch, the diamond operator <>, and multi-catch (catch (A | B e))."),
    VE("Name the headline features of Java 8.", "Lambda expressions, the Stream API, java.time, and default/static methods in interfaces."),
    VE("What is an LTS release? Give examples.", "A Long-Term Support version industry commits to - 8, 11, 17 and 21."),
    VE("What do records achieve (Java 16)?", "One line declares an immutable data class: constructor, accessors, equals, hashCode and toString all generated."),
    VE("What is pattern matching for instanceof?", "if (o instanceof String t) tests the type AND binds the cast variable in a single step."),
    VE("What does text block syntax look like?", "Triple quotes \"\"\" ... \"\"\" - multi-line strings without escape gymnastics (Java 15)."),
    VE("What does the try-with-resources header do?", "Any AutoCloseable declared in try(...) is closed automatically on every exit path - normal, caught or crashing."),
    VE("try-with-resources vs finally for closing?", "finally needs hand-written null checks and close(); try-with-resources is shorter and exception-safe by construction."),
    VE("What does the diamond operator do?", "new ArrayList<>() infers the element type from the left-hand declaration - no repetition."),
    VE("What is multi-catch used for?", "One catch block for several unrelated exception types: catch (NullPointerException | ArithmeticException e)."),
    VE("What does var infer, and where can it be used?", "The type of a local variable from its initialiser; locals and loops only - not fields, parameters or return types."),
    VE("Is Java with var dynamically typed?", "No - the real type is frozen at compile time into the .class; var x = \"s\" can never hold an int later."),
    VE("What is a functional interface?", "An interface with EXACTLY ONE abstract method - the unique shape a lambda can implement."),
    VE("What is the lambda syntax?", "(parameters) -> body. One expression needs no braces/return; multi-statements use braces."),
    VE("Why can a lambda omit parameter types?", "javac infers them from the single abstract method's signature - (x, y) -> x + y typed by Calc.op."),
    VE("What does @FunctionalInterface do?", "Asks the compiler to ERROR OUT if a second abstract method is added - protecting every lambda of that type."),
    VE("Lambda vs anonymous inner class?", "Same power; lambda removes the class ceremony, keeps only the interesting body - jv5_4 shows both."),
    VE("Can a lambda be stored in a variable?", "Yes - lambdas are values of their functional-interface type; store them, pass them, call them later."),
    VE("Name four built-in functional interfaces.", "Runnable (run), Supplier<T> (get), Consumer<T> (accept), Predicate<T> (test); plus Function<T,R> (apply)."),
    VE("Which interface powers forEach?", "Consumer<T> - its accept(t) receives each element."),
    VE("Write the lambda to print every team member.", "team.forEach(t -> System.out.println(t));"),
    VE("What is a stream in Java?", "A conveyor-belt VIEW over a collection: a pipeline of operations, not a storage and not a loop."),
    VE("What do filter, map and forEach do?", "filter keeps elements passing a Predicate; map transforms each via a Function; forEach consumes each via a Consumer."),
    VE("Does a stream modify its source collection?", "Never - streams compute views; the source list stays untouched (see jv5_8 output)."),
    VE("What does it mean that streams are lazy?", "Intermediate steps (filter/map/sorted) do nothing until a terminal step (forEach/collect/count) triggers the pipeline."),
    VE("Why can't you re-use a stream?", "A stream is consumed once; for a second pipeline open a fresh collection.stream()."),
    VE("Practical 15: which two operations are demonstrated?", "filter to keep even numbers, and map to convert strings to uppercase - both displayed with forEach."),
    VE("What does collect(Collectors.toList()) do?", "Terminal step pouring the surviving stream elements back into a new, modifiable List."),
    VE("What is AI, in one exam sentence?", "Machines performing tasks that normally require human intelligence - recognition, decisions, prediction, language."),
    VE("What is Machine Learning?", "Programs that learn their behaviour from DATA/examples rather than hand-written rules - change the data, change the behaviour."),
    VE("How does Deep Learning fit inside AI?", "DL is a branch of ML using layered neural networks; ML is inside AI; classic rule-based AI needs no learning."),
    VE("Contrast a rule-based program with an ML one.", "Rules: if mark < 33 then fail (hand-written). ML: like jv5_13 - verdict comes from the most similar past example."),
    VE("What is the role of Java in AI?", "Java runs the enterprise backends where AI features get deployed: strong data handling (collections/streams/JDBC) and API integration at scale."),
    VE("Name two AI libraries for Java.", "Deeplearning4j (train and run neural nets on the JVM) and TensorFlow Java API (run pre-trained TF models from Java)."),
    VE("What is Deeplearning4j used for?", "Building and training neural networks natively in Java/JVM languages, with GPU acceleration - the Java answer to deep learning."),
    VE("What is TensorFlow Java API used for?", "Loading pre-trained TensorFlow models and scoring them from Java code - the 'deploy in Java' half of a Python-training workflow."),
    VE("What does k-NN do? (jv5_13)", "Classifies a new case by the CLOSEST stored example - predicting pass/fail from hours-studied and attendance without any if-rule."),
    VE("Why is jv5_13 genuinely ML and not just if-else?", "Because its verdicts are derived from the example table: edit the data and the answers change - behaviour learned, not coded."),
    VE("What is the industry split between Python and Java AI?", "Python typically TRAINS models; Java DEPLOYS them inside large-scale services."),
    VE("Mention two more post-8 conveniences students should recognise.", "switch expressions with arrow labels (Java 14) and sealed classes (Java 17) - listed for theory; run on later JDKs."),
    VE("Which Java feature makes Scanner/file closing safest, and since when?", "try-with-resources, since Java 7."),
]

assert len(_VIVA) == 41
VIVA = [
    G("Java Version Updates (7-21)", _VIVA[0:14]),
    G("Lambdas and Functional Interfaces", _VIVA[14:21]),
    G("Stream API", _VIVA[21:27]),
    G("AI, ML and Java's Role", _VIVA[27:41]),
]

EXAM_QS = [
    XE("Explain any four features introduced since Java 7 (try-with-resources, diamond, multi-catch, var).", 4),
    XE("Draw a timeline of Java releases (7 to 21) with one highlight per version.", 4),
    XE("What is try-with-resources? Compare it with the traditional try-finally approach.", 4),
    XE("Write a program using try-with-resources to read tokens from a Scanner.", 4),
    XE("What is var? State its scope of use and its limitations.", 3),
    XE("Explain records, text blocks and pattern-matching instanceof briefly (Java 14-17 features).", 4),
    XE("What is a functional interface? Explain with an example.", 3),
    XE("Explain lambda expression syntax with two examples (no-param and with-param).", 4),
    XE("Write a program that prints list elements using forEach and a lambda.", 4),
    XE("Explain the Stream API pipeline: filter, map, forEach.", 4),
    XE("Write a program to filter even numbers and to map strings to uppercase using streams. (Practical 15)", 6),
    XE("Differentiate intermediate and terminal stream operations with two examples each.", 4),
    XE("Define AI and Machine Learning. How are they related?", 4),
    XE("Explain the role of Java in AI. Name two AI libraries for Java and their purpose.", 4),
    XE("Describe the k-nearest-neighbour idea used in the mini-ML program (jv5_13).", 3),
]
