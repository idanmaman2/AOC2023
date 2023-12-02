import 'dart:io';
import 'dart:math';

Future<int> main() async {
  List<String> colors = ["red", "green", "blue"];
  Iterable<Iterable<List<String>>> inp =
      (await File("./input_day2.txt").readAsLines()).map((e) => (e
          .substring(e.indexOf(": ") + 2)
          .replaceAll(";", ",")
          .replaceAll(", ", ",")
          .split(",")
          .map((x) => x.split(" "))));
  int sum  = inp.map((i)=>colors
        .map((e) => i
            .where((x) => x.skip(1).first == e)
            .map((e) => int.parse(e.first))
            .followedBy([0]).reduce(max))
        .reduce((a, b) => a * b)).reduce((a,b)=>a+b) ; 
  print(sum);
  return 0;
}
