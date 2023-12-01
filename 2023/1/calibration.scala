import scala.io.Source

@main def calibration() = 
  val bufferedSource = Source.fromFile("input.txt")
  val sum = bufferedSource.getLines.foldLeft(0) { (acc, line) =>
    val matches = """\d""".r.findAllMatchIn(line).toList
    val ints = matches.map(m => m.matched.toInt)
    acc + ints.head * 10 + ints.last
  }
  println(sum)

  bufferedSource.close