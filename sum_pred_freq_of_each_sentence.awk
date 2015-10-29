BEGIN {
  sum = 0
}

$0 == "EOS" {
  print sum
  sum = 0
}

$0 != "EOS" {
  sum += $4
}
