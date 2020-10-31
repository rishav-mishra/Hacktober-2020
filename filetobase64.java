import java.util.*;
import java.io.*;
import java.lang.*;

public class FileToBase64StringConversionUnitTest {
 
    private String inputFilePath = "test_image.jpg";
    private String outputFilePath = "test_image_copy.jpg";
 
    public void fileToBase64StringConversion() throws IOException {
        ClassLoader classLoader = getClass().getClassLoader();
        File inputFile = new File(classLoader
          .getResource(inputFilePath)
          .getFile());
 
        byte[] fileContent = FileUtils.readFileToByteArray(inputFile);
        String encodedString = Base64
          .getEncoder()
          .encodeToString(fileContent);
 
        File outputFile = new File(inputFile
          .getParentFile()
          .getAbsolutePath() + File.pathSeparator + outputFilePath);
 
        byte[] decodedBytes = Base64
          .getDecoder()
          .decode(encodedString);
        FileUtils.writeByteArrayToFile(outputFile, decodedBytes);
 
        assertTrue(FileUtils.contentEquals(inputFile, outputFile));
    }
}
