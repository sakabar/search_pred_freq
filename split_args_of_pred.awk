$0 == "EOS" {
    print $0
}

$0 != "EOS" {
    for(i=2;i<=NF;i++){
	print $1" "$i
    }
}
