import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.SequenceFile;
import org.apache.hadoop.io.Text;

import org.apache.mahout.math.DenseVector;
import org.apache.mahout.math.VectorWritable;

public class CSVToSequenceFile {

    public static void main(String[] args) throws IOException {

        String inputFile = args[0];
        String outputFile = args[1];

        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(conf);

        Path outputPath = new Path(outputFile);

        if (fs.exists(outputPath)) {
            fs.delete(outputPath, true);
        }

        Text key = new Text();

        DenseVector vector = new DenseVector(7);
        VectorWritable value = new VectorWritable(vector);

        long count = 0;

        try (
            BufferedReader reader = new BufferedReader(
                new FileReader(inputFile)
            );

            SequenceFile.Writer writer = SequenceFile.createWriter(
                conf,
                SequenceFile.Writer.file(outputPath),
                SequenceFile.Writer.keyClass(Text.class),
                SequenceFile.Writer.valueClass(VectorWritable.class)
            )
        ) {

            String line;

            reader.readLine(); // Skip CSV header

            while ((line = reader.readLine()) != null) {

                String[] fields = line.split(",");

                if (fields.length != 8) {
                    continue;
                }

                key.set(fields[0]);

                for (int i = 0; i < 7; i++) {
                    vector.set(i, Double.parseDouble(fields[i + 1]));
                }

                writer.append(key, value);

                count++;

                if (count % 200 == 0) {
                    System.out.println("Processed: " + count);
                }
            }
        }

        System.out.println("Conversion completed!");
        System.out.println("Total product vectors: " + count);
        System.out.println("Output: " + outputFile);
    }
}
