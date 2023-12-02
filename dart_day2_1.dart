import 'dart:io';
Future<int> main() async {
  Map<String, int> rules = {"red": 12, "green": 13, "blue": 14};
  Iterable<Iterable<List<String>>> inp =
      (await File("./input_day2.txt").readAsLines()).map((e) => (e
          .substring(e.indexOf(": ") + 2)
          .replaceAll(";", ",")
          .replaceAll(", ", ",")
          .split(",")
          .map((x) => x.split(" "))));

  int sum = 0;
  for (int i = 1; i < inp.length + 1; i++) {
    if (inp.skip(i - 1).first.every((element) =>
        int.parse(element.first) <= rules[element.skip(1).first]!)) {
      sum += i;
    }
  }
  print(sum);

  return 0;
}