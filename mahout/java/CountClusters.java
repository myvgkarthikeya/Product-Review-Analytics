import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.SequenceFile;

import java.util.HashMap;
import java.util.Map;

public class CountClusters {

    public static void main(String[] args) throws IOException {

        Configuration conf = new Configuration();

        Path inputPath = new Path(args[0]);

        Map<Integer, Long> clusterCounts = new HashMap<>();

        try (SequenceFile.Reader reader = new SequenceFile.Reader(
                conf,
                SequenceFile.Reader.file(inputPath))) {

            IntWritable key = new IntWritable();

            while (reader.next(key)) {

                int clusterId = key.get();

                clusterCounts.put(
                    clusterId,
                    clusterCounts.getOrDefault(clusterId, 0L) + 1
                );
            }
        }

        System.out.println("\nCLUSTER DISTRIBUTION");

        long total = 0;

        for (Map.Entry<Integer, Long> entry : clusterCounts.entrySet()) {

            System.out.println(
                "Cluster " + entry.getKey()
                + " : " + entry.getValue() + " products"
            );

            total += entry.getValue();
        }

        System.out.println("-----------------------");
        System.out.println("Total products: " + total);
    }
}
