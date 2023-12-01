import scala.io.Source
import scala.util.matching.Regex

def numberWordToInt(numberWord: String): Int = 
  try 
    numberWord.toInt
  catch 
    case e: NumberFormatException =>
      Array("one", "two", "three", "four", "five", "six", "seven", "eight", "nine").indexOf(numberWord) + 1

def lineToNumber(line: String): Int =
  val numberWords = Array("1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
  val allMatches = numberWords.foldLeft(List[Regex.Match]()) { (acc, numberWord) =>
    acc ::: numberWord.r.findAllMatchIn(line).toList
  }
  val sortedMatches = allMatches.sortBy(m => m.start)
  val ints = sortedMatches.map(m => numberWordToInt(m.matched))
  ints.head * 10 + ints.last

@main def calibration() = 
  val bufferedSource = Source.fromFile("input.txt")
  val sum = bufferedSource.getLines.foldLeft(0) { (acc, line) =>
    acc + lineToNumber(line)
  }
  println(sum)

  bufferedSource.close