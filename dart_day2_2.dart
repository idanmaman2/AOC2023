import 'dart:io';
import 'dart:math';

Future<int> main() async {
  List<String> colors = ["red", "green", "blue"];
  int sum = (await File("./inps/input_day2.txt").readAsLines())
      .map((e) => (e
          .substring(e.indexOf(": ") + 2)
          .replaceAll(";", ",")
          .replaceAll(", ", ",")
          .split(",")
          .map((x) => x.split(" "))))
      .map((i) => colors
          .map((e) => i
              .where((x) => x.skip(1).first == e)
              .map((e) => int.parse(e.first))
              .reduce(max))
          .reduce((a, b) => a * b))
      .reduce((a, b) => a + b);
  print(sum);
  return 0;
}
