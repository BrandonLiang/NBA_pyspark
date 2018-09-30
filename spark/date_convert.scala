// Courtesy to https://spark.apache.org/docs/1.5.2/ml-ann.html
import org.apache.spark.sql.SQLContext
import org.apache.spark.sql.SQLContext.implicits
import org.apache.spark.sqlContext.implicits._
import org.apache.spark.sql.types._
import org.apache.spark.sql.types.StructType
import org.apache.spark.ml.classification.MultilayerPerceptronClassifier
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator
import org.apache.spark.mllib.util.MLUtils
import org.apache.spark.sql.Row
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._


object date_convert {
  val conf = new SparkConf().setAppName("NBA Margin Timeseries").setMaster("local")
  val sc = new SparkContext(conf)
  def main(args: Array[String]){
    // Load training data
    //val data = MLUtils.loadLibSVMFile(sc, "NN_Each_Game_Distribution_4_15_ready.csv").toDF()
    val data_header = sc.textFile(args(0))
    val header = data_header.first
    val fields = header.split(',').map(fieldName => StructField(fieldName, StringType, nullable = true))
    val schema = StructType(fields)
    val data = sc.textFile(args(0))
    
    val rowRDD = data.map(_.split(','))
                      .map(attributes => Row(attributes))
                      
    //val dataDF = sqlContext.createDataFrame(rowRDD, schema)
    rowRDD.toDF().show()
    }
}
