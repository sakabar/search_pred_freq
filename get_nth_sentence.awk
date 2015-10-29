#1文目、2文目… (1-base)
BEGIN {
  sentence = 0
  # n = 0
}

$0 == "EOS" {
  sentence += 1
}

$0 != "EOS" && n == sentence+1 {
  print $0
}
