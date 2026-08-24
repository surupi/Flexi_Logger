import org.example.ColorCodes;
import org.example.Logger;
import org.example.Emoji;

import java.time.ZoneId;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Function;
import java.util.function.Predicate;

public class LoggerTest {
    public static void main(String[] args) {
        Logger redlogger = Logger.getRedDefaultLogger();
        redlogger.log("This is a red message!");

        Logger logger = Logger.getDefaultLogger();

        // Leetspeak Logging
        Logger leetLogger = Logger.getLeetLogger();
        leetLogger.log("Hello world!");

        // Caesar Cipher Logging
        Logger caesarLogger = Logger.getCaesarCipherLogger(3);
        caesarLogger.log("attack at dawn");

        // Colored and Styled Logging
        Logger styledLogger = Logger.getStyledLogger(ColorCodes.GREEN, ColorCodes.BLUE_BG, ColorCodes.BOLD);
        styledLogger.log("This is a bold green message on a blue background");

        // Using Function for message transformation
        Function<String, String> transformation = message -> message.replace("Hello", "Hi");
        Logger transformationLogger = (message) -> System.out.println(transformation.apply(message));
        transformationLogger.log("Hello world!");

        // Using Predicate for message filtering
        Predicate<String> filter = message -> true;
        String messageToLog = "This is a normal message.";
        if (filter.test(messageToLog)) {
            logger.log(messageToLog);
        }

        // Using composed transformations
        Function<String, String> upperCase = String::toUpperCase;
        Function<String, String> leet = message -> message
                .replace("o", "0")
                .replace("s", "5")
                .replace("e", "3");
        Function<String, String> combinedTransformation = upperCase.andThen(leet);
        logger.logWithTransformation(combinedTransformation, "Hello leetspeak");

        // Timestamped logging
        logger.logWithTimestamp("This message has a timestamp.");

        // Log execution time
        logger.logExecutionTime(() -> {
            try {
                Thread.sleep(150);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        // Multi-Language Logging
        logger.logInLanguage("Hello", "en");
        logger.logInLanguage("Goodbye", "es");
        logger.logInLanguage("Unknown", "fr");
        logger.logInLanguage("Hello", "de");

        // Sentiment-Based Logging
        logger.logWithSentimentHighlight("This is a fantastic day!");
        logger.logWithSentimentHighlight("This is a terrible mistake.");
        logger.logWithSentimentHighlight("This is just a normal message.");
        logger.logWithSentimentHighlight("bad, good");

        Map<String, Object> logData = new HashMap<>();
        logData.put("message", "Hello world!");
        logData.put("level", "INFO");
        logData.put("timestamp", "2024-10-06T14:32:00Z");
        logger.logAsJson(logData);

        System.setProperty("app.environment", "development");
        Logger envlogger = Logger.getEnvironmentAwareLogger();
        envlogger.log("User login attempt successful.");
        envlogger.log("Loading user preferences...");

        System.setProperty("app.environment", "production");
        Logger plogger = Logger.getEnvironmentAwareLogger();
        plogger.log("User login attempt successful.");
        plogger.log("Loading user preferences...");

        // Emoji Logger
        Logger emojiLogger = Logger.getDefaultLogger();
        emojiLogger.logWithEmoji("You are correct!", Emoji.CORRECT);
        emojiLogger.logWithEmoji("This is an error", Emoji.ERROR);

        // HTML/CSS Logger
        Logger htmlLogger = Logger.getDefaultLogger();
        htmlLogger.logWithHtmlStyle("Hello world!", "color: blue; font-weight: bold");

        // File-Based Logger
        Logger fileLogger = Logger.getFileLogger("log.txt");
        fileLogger.log("This is a file-based log message.");

        // Log Categorization
        Logger categorizedLogger = Logger.getDefaultLogger();
        categorizedLogger.logWithCategory("Unauthorized access attempt detected", "SECURITY");

        logger.logAndHighlightPalindromes("Radar detected a level of civic level responsibility", ColorCodes.RED);

        // Testing Base64 Encoding
        logger.logBase64Encoded("Hello world!"); // SGVsbG8gd29ybGQh

        // Testing Base64 Decoding
        logger.logBase64Decoded("SGVsbG8gd29ybGQh"); // Hello world!

        Logger mlogger = message -> System.out.println("Log: " + message);
        mlogger.log("Hello World");
        mlogger.logInMorseCode("Hello World");

        logger.logInPigLatin("hello world");
        logger.logInPigLatin("This is an apple");
        logger.logInPigLatin("Quick brown fox jumps over the lazy dog");

        // Test ROT13 Logger
        System.out.println("Testing ROT13:");
        logger.logWithRot13("hello");
        logger.logWithRot13("Hello, World!");

        // Test Palindrome Word Filter
        System.out.println("Testing Palindrome Words:");
        logger.logPalindromeWords("madam racecar level noon hello");

        // Test Word Frequency Logger
        System.out.println("Testing Word Frequency:");
        logger.logWordFrequency("hello world hello");

        // Test Word Length Scrambler
        logger.logWithLengthScrambledWords("I love programming in Java");
        logger.logWithLengthScrambledWords("The quick brown fox");

        logger.logWithConditionalReversedWords("The quick brown fox jumps over the lazy dog", 4);

        logger.logWithCharacterScrambledWords("Hello world");
        logger.logWithSynonyms("happy");

        logger.logWithMarkovChainTransformation("the quick brown fox jumps over the lazy dog");
        logger.logWithMarkovChainTransformation("error");
                String message = "Error occurred while processing";
        logger.logIf(message, msg -> msg.contains("Error"));
        // Expected Output: Error occurred while processing
        logger.logIf("Success", msg -> msg.contains("Error"));
        // Expected Output: (No output since the condition is not met)
        logger.logIf("Error occurred", msg -> msg.contains("Error"));

        Logger levelBasedLogger = Logger.getLevelBasedLogger(Logger.INFO);

        System.out.println("Log Level Test:");
        levelBasedLogger.error("This is an error message");
        levelBasedLogger.warn("This is a warning message");
        levelBasedLogger.info("This is an info message");
        levelBasedLogger.debug("This is a debug message");  // Should not print
        levelBasedLogger.trace("This is a trace message");  // Should not print

        System.out.println("\n----- Timestamp Test -----");
        logger.logWithTimestamp("Service started successfully");

        System.out.println("\n----- Elapsed Time Test -----");
        logger.logWithElapsedTime("Executing task", () -> {
            try {
                Thread.sleep(1500);  // Simulate task execution
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        System.out.println("\n----- Contextual Logging Test -----");
        Map<String, String> context = Map.of("userId", "12345", "sessionId", "abc123");
        logger.logWithContext("User logged in", context);

        System.out.println("\n----- Pattern Matching Test -----");
        logger.logIfMatchesPattern("Error 404", "Error [0-9]+");  // Should match and log
        logger.logIfMatchesPattern("All good", "Error [0-9]+");   // Should not log

        System.out.println("\n----- Progress Bar Test -----");
        for (int i = 0; i <= 10; i++) {
            logger.logWithProgressBar("Downloading...", i, 10);
            try {
                Thread.sleep(500);  // Simulate progress
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }

        System.out.println("\n----- Time Zone Logging Test -----");
        logger.logWithTimeZone("Server started", ZoneId.of("America/New_York"));
        logger.logWithTimeZone("User logged in", ZoneId.of("Europe/London"));
        logger.logWithTimeZone("Backup completed", ZoneId.of("Asia/Tokyo"));

        System.out.println("\n----- PII Masking Test -----");
        logger.logWithMaskedPii("Contact user at user@example.com or phone 123-456-7890 with card 1234-5678-9012-3456");

        System.out.println("\n----- SHA-256 Hash Test -----");
        logger.logSha256Hash("Secret message to hash");

        System.out.println("\n----- NATO Phonetic Test -----");
        logger.logInNatoPhonetic("SOS");

        System.out.println("\n----- Hex & Binary Test -----");
        logger.logInHex("Hello");
        logger.logInBinary("Hi");

        System.out.println("\n----- Composite Logger Test -----");
        Logger consoleLogger = Logger.getDefaultLogger();
        Logger redLogger = Logger.getRedDefaultLogger();
        Logger composite = Logger.getCompositeLogger(consoleLogger, redLogger);
        composite.log("Broadcast to multiple loggers!");
    }
}